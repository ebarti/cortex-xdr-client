from typing import Any, List, Tuple, Union

from cortex_xdr_client.api.operation import UNSET, UnsetType

from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.version import APIVersion


class AssetsAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int],
                 api_version: APIVersion = APIVersion.V3) -> None:
        super(AssetsAPI, self).__init__(auth, fqdn, 'assets', timeout, api_version)

    def bulk_update_vulnerability_tests(self, *,
                                        test_names: Union[List[str], None, UnsetType] = UNSET,
                                        status: Union[str, None, UnsetType] = UNSET) -> Any:
        """Bulk Update Vulnerability Tests

        POST /public_api/v1/assets/bulk_update_vulnerability_tests
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param test_names: body field test_names.
        :param status: body field status.
        """
        self._require_versions((5,))
        body = self._values({'test_names': test_names, 'status': status})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/assets/bulk_update_vulnerability_tests', method='post',
            body=body,
        )

    def get_public_api_v1_assets_by_id(self, *,
                                       id: str) -> Any:
        """Get asset by ID

        GET /public_api/v1/assets/{id}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param id: path field id.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/v1/assets/{id}', method='get',
            path_params={'id': id},
            body=body,
        )

    def get_public_api_v1_assets_raw_fields_by_id(self, *,
                                                  id: str) -> Any:
        """Get raw fields of asset by ID

        GET /public_api/v1/assets/{id}/raw_fields
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param id: path field id.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/v1/assets/{id}/raw_fields', method='get',
            path_params={'id': id},
            body=body,
        )

    def schema(self) -> Any:
        """Get schema of asset inventory

        GET /public_api/v1/assets/schema
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/v1/assets/schema', method='get',
            body=body,
        )

    def get_public_api_v1_assets_get_enum_by_field_name(self, *,
                                                        field_name: str) -> Any:
        """Get enum values of specified field

        GET /public_api/v1/assets/enum/{field_name}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param field_name: path field field_name.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/public_api/v1/assets/enum/{field_name}', method='get',
            path_params={'field_name': field_name},
            body=body,
        )
