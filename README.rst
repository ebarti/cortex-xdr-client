About the cortex-xdr-client
################################

A python-based client for the `Cortex XDR 3.x
<https://cortex-docs.paloaltonetworks.com/xdr-3-api>`__ and `Cortex XDR 5.x
<https://cortex-docs.paloaltonetworks.com/xdr-5-api>`__ APIs.

The client keeps its hand-written API classes, request helpers and Pydantic
v2 models and requires Python 3.11+. Standard and Advanced API key authentication work with both versions.

Getting started
===============

.. code-block:: python

    from cortex_xdr_client.api.authentication import Authentication
    from cortex_xdr_client.client import CortexXDRClient

    auth = Authentication(api_key="your-key", api_key_id=123)

    # Existing usage continues to select XDR 3.x.
    legacy = CortexXDRClient(auth, "tenant.example.com")
    incidents = legacy.incidents_api.get_incidents()

    # Select the product version explicitly for an XDR 5.x tenant.
    platform = CortexXDRClient(auth, "api-tenant.example.com", api_version=5)
    endpoints = platform.endpoints_api.get_endpoint()
    cases = platform.cases_api.get_cases(search_from=0, search_to=100)
    issues = platform.issues_api.get_issues(search_from=0, search_to=100)

``api_version`` accepts ``3``, ``5``, ``APIVersion.V3`` or ``APIVersion.V5``
(from ``cortex_xdr_client.api.version``). It selects the **product generation**,
not the number in the URL. Both generations use many ``/public_api/v1/`` routes;
some operations use other prefixes or endpoint versions.

Use the tenant FQDN from the API key examples. A hostname without ``api-``, an
``api-`` hostname, or an HTTPS origin such as ``https://api-tenant.example.com``
is accepted. Do not include an API path. The existing third positional argument
still sets the connect/read timeout, for example ``(10, 60)``.

Supported APIs
==============

The following APIs have dedicated methods and response parsing:

* **Both versions:** endpoints (list, filter, isolate, unisolate, scan, alias,
  retrieve and quarantine files), response action status, file retrieval details,
  downloads, scripts (list, metadata, execution status/results/files, run and
  snippets), XQL queries/results/streams, and JSON indicator insertion.
* **XDR 3.x:** alerts with multiple events, incidents and extra incident data.
* **XDR 5.x:** case search/update/artifacts/schema/timeline; issue
  search/create/update/schema; issue exception creation/search/disable.

On v5, use ``cases_api`` and ``issues_api``. Legacy ``incidents_api`` and
``alerts_api`` methods raise ``NotImplementedError`` with migration guidance
before making a request. Cases and Issues have different fields, filters and
response envelopes, so they have their own models. Their methods likewise
reject v3 clients. No automatic tenant detection or cross-version fallback is
performed.

Searching cases and issues
==========================

.. code-block:: python

    from cortex_xdr_client.api.models.filters import request_filter

    cases = platform.cases_api.get_cases(
        filters=[request_filter("status_progress", "in", ["New"])],
        search_from=0,
        search_to=100,
        sort={"field": "creation_time", "keyword": "desc"},
    )
    for case in cases.reply.data:
        print(case.case_id, case.case_name, case.status_progress)

    issues = platform.issues_api.get_issues(
        filters=[request_filter("severity", "in", ["HIGH", "CRITICAL"])],
        include_fields=["normalized_fields", "custom_fields"],
    )
    for issue in issues.reply.data:
        print(issue.id, issue.detection_method, issue.status_progress)

Case severities are lowercase; issue severities are uppercase. Case and Issue
search results expose ``reply.total_count``, ``reply.filter_count`` and
``reply.data``, corresponding to ``TOTAL_COUNT``, ``FILTER_COUNT`` and ``DATA``.
Dotted issue fields have Python names, for example ``status.progress`` becomes
``status_progress``. Use ``model_dump(by_alias=True)`` to recover the wire names.
Custom and additional response fields are preserved in the new models.

Case/Issue updates return ``None`` on HTTP 204. Case artifacts return the
unwrapped list from the API. Other new methods return their complete JSON
response unless they have a dedicated response model. Pagination is explicit;
methods retrieve one page per call.

Additional API families
=======================

The client has dedicated methods for the audited XDR 3.x/5.x operation
inventory, including Broker tenant operations, Agent Configurations,
Application Security, Compliance Controls, Forensics, IAM, Cloud Onboarding,
Cloud Workload Protection, Managed Services and Vulnerability Management.
They use keyword-only parameters for documented fields, omit ``UNSET`` values,
and return the complete JSON response, text, bytes, or ``None`` for an empty
response. Only the established model-backed methods return Pydantic models;
new operation methods do not claim universal schema validation.

.. code-block:: python

    brokers = legacy.brokers_api.get_brokers(name=["broker-eu-01"])
    configuration = platform.agent_configurations_api.get_content_management()
    investigations = platform.forensics_api.get_forensics_investigations()

The indexed XDR 5.x documentation also includes 10 **on-appliance** Broker VM
operations. These use a different HTTPS host and a short-lived local Bearer
token. Create this client explicitly; it never uses tenant API keys or the
``api-`` hostname prefix.

.. code-block:: python

    from cortex_xdr_client import BrokerApplianceClient

    broker = BrokerApplianceClient("https://broker.example.local")
    # On a freshly provisioned appliance, reset its factory password first.
    broker.reset_initial_password(current_password="factory", new_password="new-secret")
    token_reply = broker.generate_token(password="new-secret")
    broker.set_token(token_reply["reply"]["api_key"])
    log_bundle = broker.issue_log_bundle()  # bytes

``client.request`` remains available for an exact tenant-relative path and
returns a ``requests.Response``. Supply the full path, method and body; it does
not add a ``request_data`` wrapper or enforce the product version itself.

Supply the **exact path, method and full body** from the documentation for your
tenant version. No prefix is rewritten and no ``request_data`` wrapper is added.
The low-level method does not enforce which product version exposes a path;
the server remains authoritative for availability, licensing and permissions.

.. code-block:: python

    # Low-level XDR 3.x Broker API example: its GET operation accepts a JSON filter body.
    brokers = legacy.request(
        "/public_api/v1/brokers/",
        method="get",
        json_value={"name": ["broker-eu-01"]},
    ).json()

    # XDR 5.x agent configuration.
    configuration = platform.request(
        "/public_api/v1/configurations/agent/content_management",
    ).json()

    applications = platform.request(
        "/public_api/appsec/v1/application", method="get",
    ).json()

    compliance = platform.request(
        "/public_api/v1/compliance/get_asset",
        json_value={"request_data": {"asset_id": "your-asset-id"}},
    ).json()

    rules = platform.request(
        "/platform/notifications/v1/list-rules", method="get",
    ).json()

Use ``params`` for query parameters, ``json_value`` for JSON, or ``data`` and
``files`` for form/multipart operations. HTTP errors propagate as
``requests.HTTPError``; rate-limit responses are not retried automatically.
Authenticated redirects are rejected to keep credentials on the configured
tenant. Download helpers accept either the file token or the tenant's complete
file-retrieval download URL.

API coverage
============

The pinned 2026-09-29 inventory has 124 XDR 3.x operations and 386 XDR 5.x
operations, including the 10 on-appliance Broker VM operations. All 510
version/method/path entries map to dedicated public methods. The inventory,
source hashes, known vendor inconsistencies and offline verification boundary
are in `the coverage inventory <docs/API_COVERAGE.md>`__. Live tenant
compatibility remains unverified.

Migrating from client 1.x
================================

Client 2.0 uses native Pydantic v2 and requires Python 3.11+. Use client 1.x if
an application still needs Python 3.8-3.10 or Pydantic v1 models. The Cortex XDR
product version is independent: client 2.0 still supports both XDR 3.x and 5.x.

* Replace model ``parse_obj(data)`` calls with ``model_validate(data)``,
  ``dict()`` with ``model_dump()``, and ``json()`` with ``model_dump_json()``.
* Use ``model_dump(mode="json", by_alias=True)`` for JSON-compatible dictionaries.
  Ordinary ``model_dump()`` preserves Python types such as enums and datetimes.
* Action status mappings use ``response.reply.data.root`` instead of
  ``response.reply.data.__root__``. Their serialized API shape is unchanged.
* Response models preserve additional fields and accept either Python field
  names or API aliases. Known field types still validate. No blanket conversion
  of lists or dictionaries to strings is performed.
* Optional response fields still default to ``None``. Existing required fields
  stay required. Pydantic v2's validation and model equality rules apply; number
  inputs are not implicitly converted to strings.

See `the Pydantic migration notes <docs/PYDANTIC_V2.md>`__ for details.

Compatibility notes
===================

* Existing constructor calls and shared API method names remain available.
* Endpoint enum filters now serialize the documented lowercase request values,
  while response enums retain their existing values. XDR 5 cloud filters are
  available on ``get_endpoint``.
* File retrieval nests paths under ``request_data.files``. Incident/case IDs
  belong inside ``request_data``; response actions still use the wire field
  ``incident_id`` on v5.
* Alert filters send lowercase severities and accept ``CRITICAL``. Script
  filters preserve ``False`` and use ``modification_date``. Script IDs accept
  strings as well as existing integer values.
* XQL results follow a returned ``stream_id`` and handle compressed files as
  well as streams already decompressed by requests. Limits above 1,000 are
  forwarded to the server.
* Indicators require only ``indicator``, ``type`` and ``severity``. The existing
  ``IoCSeverity.informational`` maps to ``INFO`` on the wire. The legacy
  ``unknown`` severity is rejected locally for v5, whose schema excludes it.

See `the compatibility audit <docs/API_COMPATIBILITY.md>`__ for sources,
documentation inconsistencies and verification limits.

Contributing
============

See `CONTRIBUTING.md <CONTRIBUTING.md>`__ for setup and testing.
