"""Explicit operations from the pinned Cortex XDR documentation snapshot."""
from typing import Any, Tuple, Union

from cortex_xdr_client.api.operation import UNSET, UnsetType
from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.version import APIVersion


class DetectionRulesAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int],
                 api_version: APIVersion = APIVersion.V3) -> None:
        super(DetectionRulesAPI, self).__init__(auth, fqdn, 'detection_rules', timeout, api_version)

    def create_detection_rule(self, *,
            asset_types: list,
            name: str,
            query: dict,
            severity: str,
            class_value: Union[str, None, UnsetType] = UNSET,
            compliance_metadata: Union[list, None, UnsetType] = UNSET,
            description: Union[str, None, UnsetType] = UNSET,
            enabled: Union[bool, None, UnsetType] = UNSET,
            labels: Union[list, None, UnsetType] = UNSET,
            metadata: Union[dict, None, UnsetType] = UNSET,
            type: Union[str, None, UnsetType] = UNSET) -> Any:
        """Create Detection Rule

        POST /public_api/v1/rule
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param asset_types: body field asset_types.
        :param name: body field name.
        :param query: body field query.
        :param severity: body field severity.
        :param class_value: body field class.
        :param compliance_metadata: body field compliance_metadata.
        :param description: body field description.
        :param enabled: body field enabled.
        :param labels: body field labels.
        :param metadata: body field metadata.
        :param type: body field type.
        """
        self._require_versions((5,))
        body = self._values({
            'asset_types': asset_types,
            'name': name,
            'query': query,
            'severity': severity,
            'class': class_value,
            'compliance_metadata': compliance_metadata,
            'description': description,
            'enabled': enabled,
            'labels': labels,
            'metadata': metadata,
            'type': type,
        })
        return self._operation(
            '/public_api/v1/rule', method='post',
            body=body,
        )

    def search_detection_rules(self, *,
            filter: Union[dict, None, UnsetType] = UNSET,
            search_from: Union[int, None, UnsetType] = UNSET,
            search_to: Union[int, None, UnsetType] = UNSET,
            sort: Union[list, None, UnsetType] = UNSET) -> Any:
        """Get Detection Rules

        POST /public_api/v1/rule/search
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param filter: body field filter.
        :param search_from: body field search_from.
        :param search_to: body field search_to.
        :param sort: body field sort.
        """
        self._require_versions((5,))
        body = self._values({
            'filter': filter,
            'search_from': search_from,
            'search_to': search_to,
            'sort': sort,
        })
        return self._operation(
            '/public_api/v1/rule/search', method='post',
            body=body,
        )

    def get_detection_rule_by_id(self, *, id: str) -> Any:
        """Get Rule By Id

        GET /public_api/v1/rule/{id}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param id: path field id.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/v1/rule/{id}', method='get',
            path_params={'id': id},
            body=body,
        )

    def delete_detection_rule(self, *, id: str) -> Any:
        """Delete Detection Rule

        DELETE /public_api/v1/rule/{id}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param id: path field id.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/v1/rule/{id}', method='delete',
            path_params={'id': id},
            body=body,
        )

    def update_detection_rule(self, *,
            id: str,
            rule_class: str,
            asset_types: Union[list, None, UnsetType] = UNSET,
            compliance_metadata: Union[list, None, UnsetType] = UNSET,
            description: Union[str, None, UnsetType] = UNSET,
            enabled: Union[bool, None, UnsetType] = UNSET,
            labels: Union[list, None, UnsetType] = UNSET,
            metadata: Union[dict, None, UnsetType] = UNSET,
            name: Union[str, None, UnsetType] = UNSET,
            query: Union[dict, None, UnsetType] = UNSET,
            severity: Union[str, None, UnsetType] = UNSET,
            type: Union[str, None, UnsetType] = UNSET) -> Any:
        """Update Detection Rule

        PATCH /public_api/v1/rule/{id}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param id: path field id.
        :param rule_class: body field rule_class.
        :param asset_types: body field asset_types.
        :param compliance_metadata: body field compliance_metadata.
        :param description: body field description.
        :param enabled: body field enabled.
        :param labels: body field labels.
        :param metadata: body field metadata.
        :param name: body field name.
        :param query: body field query.
        :param severity: body field severity.
        :param type: body field type.
        """
        self._require_versions((5,))
        body = self._values({
            'rule_class': rule_class,
            'asset_types': asset_types,
            'compliance_metadata': compliance_metadata,
            'description': description,
            'enabled': enabled,
            'labels': labels,
            'metadata': metadata,
            'name': name,
            'query': query,
            'severity': severity,
            'type': type,
        })
        return self._operation(
            '/public_api/v1/rule/{id}', method='patch',
            path_params={'id': id},
            body=body,
        )
