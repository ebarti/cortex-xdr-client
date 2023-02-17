from typing import Optional, Tuple

from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.models.action_status import GetActionStatus
from cortex_xdr_client.api.models.filters import new_request_data


class DownloadAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int]) -> None:
        super(DownloadAPI, self).__init__(auth, fqdn, "download", timeout)

    # https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR/Cortex-XDR-API-Reference/File-Retrieval-Details
    def download_file(self,
                          file_api_value: str
                          ):
        """
        Downloads the file at the given URI, previously requested by get_file_retrieval_details function

        :file_api_value: UID assigned to the file that is requested to be downloaded
        :return: Contents of the file
        """
        response = self._call(call_name=file_api_value)
        return response.content
