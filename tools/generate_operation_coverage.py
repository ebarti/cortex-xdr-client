"""Regenerate the supplementary explicit API methods from pinned GitBook blocks.

The snapshot is committed in tests/fixtures/indexed_openapi_blocks.json. Refresh it
separately after reviewing upstream changes; this generator never reads the network.
Existing hand-written methods and the initial coverage checkpoint are not rewritten.
"""

import json
import keyword
import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT = ROOT / 'tests/fixtures/indexed_openapi_blocks.json'
CATALOG = ROOT / 'cortex_xdr_client/api/operation_catalog.json'
CONTRACTS = ROOT / 'tests/fixtures/operation_contracts.json'

FAMILIES = {
    'broker-vm-tenant-side': ('brokers_v5', 'BrokersV5API'),
    'cloud-infrastructure-entitlement-management-ciem': ('ciem', 'CiemAPI'),
    'cloud-onboarding': ('cloud_onboarding', 'CloudOnboardingAPI'),
    'cloud-workload-protection': ('cloud_workload_protection', 'CloudWorkloadProtectionAPI'),
    'compliance-controls': ('compliance_controls', 'ComplianceControlsAPI'),
    'data-security-posture-management': ('data_security', 'DataSecurityAPI'),
    'detection-rules-management': ('detection_rules', 'DetectionRulesAPI'),
    'disable-injection-and-prevention-rules': ('prevention_rules_v5', 'PreventionRulesV5API'),
    'disable-prevention-rule': ('prevention_rules_v5', 'PreventionRulesV5API'),
    'external-application-management': ('external_applications', 'ExternalApplicationsAPI'),
    'forensics': ('forensics', 'ForensicsAPI'),
    'identity-and-access-management-iam': ('iam', 'IamAPI'),
    'logging-and-collection-service-management': ('clcs', 'ClcsAPI'),
    'managed-services': ('managed_services', 'ManagedServicesAPI'),
    'netscan': ('netscan', 'NetscanAPI'),
    'policies': ('cloud_security_policies', 'CloudSecurityPoliciesAPI'),
    'restore-distributions': ('restore_distributions', 'RestoreDistributionsAPI'),
    'unified-rules': ('unified_rules', 'UnifiedRulesAPI'),
    'vulnerability-intelligence': ('vulnerability_intelligence', 'VulnerabilityIntelligenceAPI'),
    'vulnerability-management': ('vulnerability_management', 'VulnerabilityManagementAPI'),
}
HTTP_METHODS = {'get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace'}
AUTH_HEADERS = {'authorization', 'x-xdr-auth-id', 'x-xdr-timestamp', 'x-xdr-nonce', 'content-type'}


def resolve(schema, spec, depth=0):
    if not isinstance(schema, dict) or depth > 12:
        return schema
    ref = schema.get('$ref')
    if ref and ref.startswith('#/'):
        value = spec
        try:
            for part in ref[2:].split('/'):
                value = value[part.replace('~1', '/').replace('~0', '~')]
            return resolve(value, spec, depth + 1)
        except (KeyError, TypeError):
            return schema
    if 'allOf' in schema:
        parts = [resolve(item, spec, depth + 1) for item in schema['allOf']]
        combined = dict(schema)
        combined.pop('allOf')
        combined['properties'] = {key: val for part in parts for key, val in part.get('properties', {}).items()
                                  if not (val.get('readOnly') and 'omitted on insert' in val.get('description', '').lower())}
        combined['required'] = list(dict.fromkeys(x for part in parts for x in part.get('required', [])))
        return combined
    return schema


def python_name(name):
    name = re.sub(r'^(get|post|put|delete|patch)(v\d+)', r'\1_\2', name, flags=re.I)
    name = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', name)
    name = re.sub(r'[^A-Za-z0-9]+', '_', name).strip('_').lower()
    if not name or name[0].isdigit():
        name = 'field_' + name
    if keyword.iskeyword(name) or name in {'self', 'body', 'data', 'files'}:
        name += '_value'
    return name


def annotation(schema, spec):
    schema = resolve(schema, spec)
    kind = schema.get('type') if isinstance(schema, dict) else None
    if isinstance(kind, list):
        kind = next((x for x in kind if x != 'null'), None)
    if not kind and isinstance(schema, dict):
        kind = 'object' if 'properties' in schema else None
    return {'string': 'str', 'integer': 'int', 'number': 'float', 'boolean': 'bool',
            'object': 'dict', 'array': 'list'}.get(kind, 'Any')


def operation_name(operation, path, method, used):
    operation_id = operation.get('operationId') or ''
    source = (operation_id if re.fullmatch(r'[A-Za-z][A-Za-z0-9]*', operation_id)
              else operation.get('summary') or operation_id or method + ' ' + path.rsplit('/', 1)[-1])
    name = python_name(source)
    if len(name) > 72 or name in {'get', 'post', 'put', 'delete', 'patch'}:
        name = python_name(operation.get('operationId', ''))
    if name in used:
        name = name + '_' + python_name(path.strip('/').rsplit('/', 1)[-1])
    if name in used:
        name += '_request'
    suffix = 2
    while name in used:
        name = name + '_' + str(suffix)
        suffix += 1
    used.add(name)
    return name


def fields_for(operation, spec, path):
    all_params = [resolve(x, spec) for x in operation.get('parameters', [])]
    body = resolve(operation.get('requestBody', {}), spec)
    content = body.get('content', {}) if isinstance(body, dict) else {}
    media = next(iter(content), None)
    schema = resolve(content.get(media, {}).get('schema', {}), spec) if media else {}
    fields = []
    for p in all_params:
        location = p.get('in')
        name = p.get('name')
        if not name or location not in {'path', 'query', 'header'}:
            continue
        if location == 'header' and name.lower() in AUTH_HEADERS:
            continue
        fields.append((location, name, resolve(p.get('schema', {}), spec), bool(p.get('required')),
                       p.get('explode', True)))
    declared_path = {name for location, name, *_ in fields if location == 'path'}
    for name in re.findall(r'\{([^{}]+)\}', path):
        if name not in declared_path:
            # GitBook omits several path parameter declarations while retaining
            # their literal placeholders in the published route.
            fields.append(('path', name, {'type': 'string'}, True, True))
    envelope = None
    if schema.get('type') == 'object' or 'properties' in schema:
        props = schema.get('properties', {})
        if len(props) == 1 and next(iter(props), None) in {'request', 'request_data'}:
            envelope = next(iter(props))
            schema = resolve(props[envelope], spec)
    if schema.get('type') == 'object' or 'properties' in schema:
        if schema.get('properties'):
            for name, item in schema['properties'].items():
                fields.append(('body', name, resolve(item, spec), name in schema.get('required', []), True))
        elif media and not (schema.get('type') == 'object' and
                            (envelope or 'empty' in schema.get('description', '').lower()) and
                            not schema.get('additionalProperties')):
            fields.append(('raw_body', 'payload', schema, bool(body.get('required')), True))
    elif media:
        fields.append(('raw_body', 'payload', schema, bool(body.get('required')), True))
    return fields, envelope, media, body


def render_method(name, operation, path, http_method, spec, version):
    fields, envelope, media, body_spec = fields_for(operation, spec, path)
    used = set()
    named = []
    for loc, wire, schema, required, explode in fields:
        py = python_name(wire)
        while py in used:
            py += '_field'
        used.add(py)
        named.append((loc, wire, py, schema, required, explode))
    named.sort(key=lambda x: (not x[4], {'path': 0, 'query': 1, 'header': 2, 'body': 3, 'raw_body': 4}[x[0]]))
    params = []
    for loc, wire, py, schema, required, explode in named:
        typ = annotation(schema, spec)
        if required:
            params.append(f'{py}: {typ}')
        else:
            params.append(f'{py}: Union[{typ}, None, UnsetType] = UNSET')
    sig = '*, ' + ', '.join(params) if params else ''
    signature = f'    def {name}(self{", " if sig else ""}{sig}) -> Any:'
    if len(signature) > 100:
        signature = (f'    def {name}(self, *,\n' +
                     '\n'.join('            ' + part + (',' if pos < len(params) - 1 else '')
                               for pos, part in enumerate(params)) + ') -> Any:')
    summary = (operation.get('summary') or operation.get('operationId') or name).replace('"', "'").replace('\n', ' ')
    lines = [signature,
             f'        """{summary}', '', f'        {http_method.upper()} {path}',
             f'        Available in Cortex XDR {version}.x.',
             '        Returns the complete JSON response, text, bytes, or None for an empty response.',
             '        Optional fields use UNSET for omission; None is explicit null.',
             '        The source snapshot records this operation and its parameter schema.']
    for loc, wire, py, *_ in named:
        lines.append(f'        :param {py}: {loc} field {wire}.')
    lines += ['        """', f'        self._require_versions(({version},))']
    path_fields = {wire: py for loc, wire, py, *_ in named if loc == 'path'}
    query_fields = [(wire, py, explode) for loc, wire, py, _, _, explode in named if loc == 'query']
    header_fields = {wire: py for loc, wire, py, *_ in named if loc == 'header'}
    body_fields = {wire: py for loc, wire, py, *_ in named if loc == 'body'}
    raw = next((py for loc, wire, py, *_ in named if loc == 'raw_body'), None)
    if body_fields:
        body_line = '        body = self._values({' + ', '.join(f'{wire!r}: {py}' for wire, py in body_fields.items()) + '})'
        if len(body_line) > 100:
            body_line = ('        body = self._values({\n' +
                         '\n'.join(f'            {wire!r}: {py},' for wire, py in body_fields.items()) +
                         '\n        })')
        lines.append(body_line)
        if envelope:
            lines.append(f'        body = {{{envelope!r}: body}}')
    elif raw:
        lines.append(f'        body = {raw}')
        if envelope:
            lines.append(f'        body = {{{envelope!r}: body}}')
    elif media and (body_spec.get('required') or envelope):
        lines.append(f'        body = {{{envelope!r}: {{}}}}' if envelope else '        body = {}')
    else:
        lines.append('        body = UNSET')
    lines += ['        return self._operation(', f'            {path!r}, method={http_method!r},']
    if path_fields:
        lines.append('            path_params={' + ', '.join(f'{wire!r}: {py}' for wire, py in path_fields.items()) + '},')
    if query_fields:
        lines.append('            query=[' + ', '.join(f'({wire!r}, {py}, {explode})' for wire, py, explode in query_fields) + '],')
    if header_fields:
        lines.append('            headers={' + ', '.join(f'{wire!r}: {py}' for wire, py in header_fields.items()) + '},')
    if media and not media.lower().startswith('application/json'):
        if media.startswith('text/'):
            lines.append('            data=body,')
        else:
            lines.append('            body=body,')
    else:
        lines.append('            body=body,')
    lines += ['        )', '']
    return '\n'.join(lines), {f'{loc}:{wire}': py for loc, wire, py, *_ in named}


def main():
    snapshot = json.loads(SNAPSHOT.read_text())
    catalog = [x for x in json.loads(CATALOG.read_text()) if 'source' not in x]
    contracts = [x for x in json.loads(CONTRACTS.read_text()) if 'summary' not in x]
    seen = {(x['version'], x['path'], x['http_method']) for x in catalog}
    assert len(seen) == len(catalog)
    by_family = defaultdict(list)
    used_names = defaultdict(set)
    for page in snapshot['pages']:
        match = re.search(r'/xdr-([35])-api/([^/]+)/', page['url'])
        if not match:
            continue
        version, section = int(match.group(1)), match.group(2)
        for spec in page['blocks']:
            for path, methods in spec.get('paths', {}).items():
                for http_method, operation in methods.items():
                    if http_method.lower() not in HTTP_METHODS:
                        continue
                    key = (version, path, http_method.lower())
                    if key in seen:
                        continue
                    if section == 'broker-vm-on-appliance':
                        family, class_name = 'broker_appliance', 'BrokerApplianceClient'
                    else:
                        family, class_name = FAMILIES[section]
                    name = operation_name(operation, path, http_method, used_names[family])
                    method_code, args = render_method(name, operation, path, http_method, spec, version)
                    by_family[(family, class_name)].append(method_code)
                    catalog.append({'version': version, 'path': path, 'http_method': http_method.lower(),
                                    'api': family if family == 'broker_appliance' else family + '_api',
                                    'method': name, 'arguments': args, 'wire_path': path,
                                    'source': page['url']})
                    body = operation.get('requestBody', {})
                    if '$ref' in body:
                        body = resolve(body, spec)
                    media = next(iter(body.get('content', {})), None)
                    schema = resolve(body.get('content', {}).get(media, {}).get('schema', {}), spec) if media else {}
                    contracts.append({'version': version, 'source': page['url'], 'path': path,
                                      'http_method': http_method.lower(), 'operation_id': operation.get('operationId'),
                                      'summary': operation.get('summary'), 'parameters': operation.get('parameters', []),
                                      'body': schema, 'media': media, 'responses': operation.get('responses', {})})
                    seen.add(key)
    for (family, class_name), methods in by_family.items():
        if family == 'broker_appliance':
            destination = ROOT / 'cortex_xdr_client/api/broker_appliance_operations.py'
            class_head = 'class BrokerApplianceOperations(OperationAPI):\n'
            imports = 'from typing import Any, Union\n\nfrom cortex_xdr_client.api.operation import OperationAPI, UNSET, UnsetType\n\n\n'
        else:
            destination = ROOT / f'cortex_xdr_client/api/{family}_api.py'
            imports = ('from typing import Any, Tuple, Union\n\n'
                       'from cortex_xdr_client.api.operation import UNSET, UnsetType\n'
                       'from cortex_xdr_client.api.authentication import Authentication\n'
                       'from cortex_xdr_client.api.base_api import BaseAPI\n'
                       'from cortex_xdr_client.api.version import APIVersion\n\n\n')
            class_head = (f'class {class_name}(BaseAPI):\n'
                          '    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int],\n'
                          '                 api_version: APIVersion = APIVersion.V3) -> None:\n'
                          f"        super({class_name}, self).__init__(auth, fqdn, '{family}', timeout, api_version)\n\n")
        destination.write_text('"""Explicit operations from the pinned Cortex XDR documentation snapshot."""\n'
                               + imports + class_head + '\n'.join(methods))
        print(destination.relative_to(ROOT), len(methods))
    CATALOG.write_text(json.dumps(catalog, indent=2) + '\n')
    CONTRACTS.write_text(json.dumps(contracts, indent=2) + '\n')
    print('total', len(catalog))


if __name__ == '__main__':
    main()
