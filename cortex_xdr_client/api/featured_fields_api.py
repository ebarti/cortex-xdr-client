from typing import Any, List, Tuple, Union

from cortex_xdr_client.api.operation import UNSET, UnsetType

from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.version import APIVersion


class FeaturedFieldsAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int],
                 api_version: APIVersion = APIVersion.V3) -> None:
        super(FeaturedFieldsAPI, self).__init__(auth, fqdn, 'featured_fields', timeout, api_version)

    def replace_hosts(self, *,
                      accept_encoding: Union[str, None, UnsetType] = UNSET,
                      fields: Union[List[dict], None, UnsetType] = UNSET) -> Any:
        """Replace Featured Hosts

        POST /public_api/v1/featured_fields/replace_hosts
        Available in Cortex XDR 3.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param accept_encoding: header field Accept-Encoding.
        :param fields: body field fields.
        """
        self._require_versions((3,))
        body = self._values({'fields': fields})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/featured_fields/replace_hosts', method='post',
            headers={'Accept-Encoding': accept_encoding},
            body=body,
        )

    def replace_users(self, *,
                      accept_encoding: Union[str, None, UnsetType] = UNSET,
                      fields: Union[List[dict], None, UnsetType] = UNSET) -> Any:
        """Replace Featured Users

        POST /public_api/v1/featured_fields/replace_users
        Available in Cortex XDR 3.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param accept_encoding: header field Accept-Encoding.
        :param fields: body field fields.
        """
        self._require_versions((3,))
        body = self._values({'fields': fields})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/featured_fields/replace_users', method='post',
            headers={'Accept-Encoding': accept_encoding},
            body=body,
        )

    def replace_ip_addresses(self, *,
                             accept_encoding: Union[str, None, UnsetType] = UNSET,
                             fields: Union[List[dict], None, UnsetType] = UNSET) -> Any:
        """Replace Featured IP Addresses

        POST /public_api/v1/featured_fields/replace_ip_addresses
        Available in Cortex XDR 3.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param accept_encoding: header field Accept-Encoding.
        :param fields: body field fields.
        """
        self._require_versions((3,))
        body = self._values({'fields': fields})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/featured_fields/replace_ip_addresses', method='post',
            headers={'Accept-Encoding': accept_encoding},
            body=body,
        )

    def replace_ad_groups(self, *,
                          accept_encoding: Union[str, None, UnsetType] = UNSET,
                          fields: Union[List[dict], None, UnsetType] = UNSET) -> Any:
        """Replace Featured Active Directory Groups

        POST /public_api/v1/featured_fields/replace_ad_groups
        Available in Cortex XDR 3.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param accept_encoding: header field Accept-Encoding.
        :param fields: body field fields.
        """
        self._require_versions((3,))
        body = self._values({'fields': fields})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/public_api/v1/featured_fields/replace_ad_groups', method='post',
            headers={'Accept-Encoding': accept_encoding},
            body=body,
        )
