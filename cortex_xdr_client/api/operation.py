"""Shared wire handling for the explicit operation methods."""
from enum import Enum
from typing import Any
from urllib.parse import quote

from pydantic import BaseModel


class UnsetType(Enum):
    UNSET = 'UNSET'


UNSET = UnsetType.UNSET


def json_value(value):
    """Serialize models/enums without changing false, zero, empty values or null."""
    if isinstance(value, BaseModel):
        return value.model_dump(mode='json', by_alias=True, exclude_unset=True)
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, dict):
        return {key: json_value(item) for key, item in value.items() if item is not UNSET}
    if isinstance(value, (list, tuple)):
        return [json_value(item) for item in value]
    return value


def wire_value(value):
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if isinstance(value, Enum):
        return wire_value(value.value)
    if value is None:
        return ''
    return str(value)


class OperationAPI:
    def _require_versions(self, versions):
        if self._api_version.value not in versions:
            supported = ', '.join(str(version) + '.x' for version in versions)
            raise NotImplementedError(f'This operation requires Cortex XDR {supported}')

    def _reject_fields(self, **fields):
        supplied = [name for name, value in fields.items() if value is not UNSET]
        if supplied:
            raise ValueError(f'Fields not supported in Cortex XDR {self._api_version.value}.x: {", ".join(supplied)}')

    @staticmethod
    def _values(values):
        return {key: value for key, value in values.items() if value is not UNSET}

    def _operation(self, path: str, method: str, body=UNSET, path_params=None,
                   query=None, headers=None, data=UNSET, files=None) -> Any:
        for key, value in (path_params or {}).items():
            if value is None or value is UNSET or str(value) in ('', '.', '..'):
                raise ValueError(f'Invalid path parameter: {key}')
            path = path.replace('{' + key + '}', quote(str(value), safe=''))
        params = []
        for name, value, explode in query or []:
            if value is UNSET:
                continue
            if isinstance(value, (list, tuple)):
                values = [wire_value(item) for item in value]
                if explode:
                    params.extend((name, item) for item in values)
                else:
                    params.append((name, ','.join(values)))
            elif isinstance(value, dict):
                # OpenAPI's default query encoding is form with explode=true.
                if explode:
                    params.extend((key, wire_value(item)) for key, item in value.items())
                else:
                    params.append((name, ','.join(part for key, item in value.items()
                                                  for part in (str(key), wire_value(item)))))
            else:
                params.append((name, wire_value(value)))
        header_values = {name: wire_value(value) for name, value in (headers or {}).items()
                         if value is not UNSET}
        kwargs = {'method': method, 'params': params, 'header_params': header_values}
        if body is not UNSET:
            # Requests treats json=None as "no body". Preserve an explicit JSON null.
            if body is None:
                kwargs['data'] = 'null'
                header_values.setdefault('Content-Type', 'application/json')
            else:
                kwargs['json_value'] = json_value(body)
        if data is not UNSET:
            kwargs['data'] = json_value(data)
        if files is not None:
            kwargs['files'] = self._values(files)
        response = self.request(path, **kwargs)
        if response.status_code in (204, 205) or not response.content:
            return None
        media = response.headers.get('Content-Type', '').split(';', 1)[0].lower()
        if media == 'application/json' or media.endswith('+json'):
            return response.json()
        if media.startswith('text/'):
            return response.text
        if not media:
            # Several documented endpoints omit a response media type.
            try:
                return response.json()
            except ValueError:
                return response.content
        return response.content
