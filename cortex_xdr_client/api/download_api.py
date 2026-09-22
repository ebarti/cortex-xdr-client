from typing import Tuple
from urllib.parse import quote, urlsplit

from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.version import APIVersion


class DownloadAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int],
                 api_version: APIVersion = APIVersion.V3) -> None:
        super(DownloadAPI, self).__init__(auth, fqdn, "download", timeout, api_version)

    # https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR/Cortex-XDR-API-Reference/File-Retrieval-Details
    def download_file(self,
                          file_api_value: str
                          ):
        """
        Downloads the file at the given URI, previously requested by get_file_retrieval_details function

        :file_api_value: UID assigned to the file that is requested to be downloaded
        :return: Contents of the file
        """
        if file_api_value.startswith('https://'):
            parsed = urlsplit(file_api_value)
            if parsed.scheme + '://' + parsed.netloc != self._base_url:
                raise ValueError("Download URL must belong to the configured tenant")
            if parsed.query or parsed.fragment:
                raise ValueError("Download URL must not contain a query or fragment")
            file_api_value = parsed.path
        if file_api_value.startswith('/'):
            if not file_api_value.startswith('/public_api/v1/download/'):
                raise ValueError("Expected a file retrieval download path")
            response = self.request(file_api_value)
        else:
            response = self._call(call_name=quote(file_api_value, safe=''))
        return response.content
