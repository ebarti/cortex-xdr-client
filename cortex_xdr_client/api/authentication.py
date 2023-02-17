import hashlib
import secrets
import string
from datetime import datetime, timezone
from enum import Enum
from typing import Optional


class AuthenticationType(Enum):
    STANDARD = 1
    ADVANCED = 2


class Authentication:
    def __init__(self, api_key: str, api_key_id: int,
                 auth_type: Optional[AuthenticationType] = AuthenticationType.ADVANCED):
        """
        Creates an Authentication object used on authenticated calls against the backend.
        :param api_key_id: The API key ID to use.
        :param api_key: The API key value to use.
        :param auth_type: The type of authentication: either Standard or Advanced
        """
        self._api_key_id = api_key_id
        self._api_key = api_key
        self._auth_type = auth_type

    def get_headers(self):
        if self._auth_type == AuthenticationType.STANDARD:
            return {
                "x-xdr-auth-id": str(self._api_key_id),
                'Authorization': self._api_key
            }
        nonce = "".join([secrets.choice(string.ascii_letters + string.digits) for _ in range(64)])
        timestamp = int(datetime.now(timezone.utc).timestamp()) * 1000
        auth_key = "%s%s%s" % (self._api_key, nonce, timestamp)
        auth_key = auth_key.encode("utf-8")
        api_key_hash = hashlib.sha256(auth_key).hexdigest()
        return {
            "x-xdr-timestamp": str(timestamp),
            "x-xdr-nonce":     nonce,
            "x-xdr-auth-id":   str(self._api_key_id),
            "Authorization":   api_key_hash
        }
