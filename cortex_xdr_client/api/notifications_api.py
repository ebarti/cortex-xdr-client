from typing import Any, List, Tuple, Union

from cortex_xdr_client.api.operation import UNSET, UnsetType

from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.version import APIVersion


class NotificationsAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int],
                 api_version: APIVersion = APIVersion.V3) -> None:
        super(NotificationsAPI, self).__init__(auth, fqdn, 'notifications', timeout, api_version)

    def list_rules(self) -> Any:
        """List all rules

        GET /platform/notifications/v1/list-rules
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/platform/notifications/v1/list-rules', method='get',
            body=body,
        )

    def create_rule(self, *,
                    name: Union[str, None, UnsetType] = UNSET,
                    description: Union[str, None, UnsetType] = UNSET,
                    forward_type: Union[str, None, UnsetType] = UNSET,
                    filter: Union[dict, None, UnsetType] = UNSET,
                    forward_source: Union[dict, None, UnsetType] = UNSET,
                    applications: Union[List[str], None, UnsetType] = UNSET,
                    time_zone: Union[str, None, UnsetType] = UNSET,
                    mail_format: Union[str, None, UnsetType] = UNSET,
                    syslog_format: Union[str, None, UnsetType] = UNSET,
                    slack_format: Union[str, None, UnsetType] = UNSET) -> Any:
        """Create a new rule

        POST /platform/notifications/v1/rule
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param name: body field name.
        :param description: body field description.
        :param forward_type: body field forward_type.
        :param filter: body field filter.
        :param forward_source: body field forward_source.
        :param applications: body field applications.
        :param time_zone: body field time_zone.
        :param mail_format: body field mail_format.
        :param syslog_format: body field syslog_format.
        :param slack_format: body field slack_format.
        """
        self._require_versions((5,))
        body = self._values({'name': name, 'description': description, 'forward_type': forward_type, 'filter': filter, 'forward_source': forward_source, 'applications': applications, 'time_zone': time_zone, 'mail_format': mail_format, 'syslog_format': syslog_format, 'slack_format': slack_format})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/platform/notifications/v1/rule', method='post',
            body=body,
        )

    def get_rule_by_uuid(self, *,
                         rule_uuid: str) -> Any:
        """Retrieve a specific alert notification rule

        GET /platform/notifications/v1/rule/{rule_uuid}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param rule_uuid: path field rule_uuid.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/platform/notifications/v1/rule/{rule_uuid}', method='get',
            path_params={'rule_uuid': rule_uuid},
            body=body,
        )

    def delete_rule(self, *,
                    rule_uuid: str) -> Any:
        """Delete an existing Alert Notification Rule

        DELETE /platform/notifications/v1/rule/{rule_uuid}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param rule_uuid: path field rule_uuid.
        """
        self._require_versions((5,))
        body = UNSET
        return self._operation(
            '/platform/notifications/v1/rule/{rule_uuid}', method='delete',
            path_params={'rule_uuid': rule_uuid},
            body=body,
        )

    def edit_rule(self, *,
                  rule_uuid: str,
                  name: Union[str, None, UnsetType] = UNSET,
                  description: Union[str, None, UnsetType] = UNSET,
                  forward_type: Union[str, None, UnsetType] = UNSET,
                  filter: Union[dict, None, UnsetType] = UNSET,
                  forward_source: Union[dict, None, UnsetType] = UNSET,
                  applications: Union[List[str], None, UnsetType] = UNSET,
                  time_zone: Union[str, None, UnsetType] = UNSET,
                  mail_format: Union[str, None, UnsetType] = UNSET,
                  syslog_format: Union[str, None, UnsetType] = UNSET,
                  slack_format: Union[str, None, UnsetType] = UNSET) -> Any:
        """Edit an existing Alert Notification Rule

        PUT /platform/notifications/v1/rule/{rule_uuid}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param rule_uuid: path field rule_uuid.
        :param name: body field name.
        :param description: body field description.
        :param forward_type: body field forward_type.
        :param filter: body field filter.
        :param forward_source: body field forward_source.
        :param applications: body field applications.
        :param time_zone: body field time_zone.
        :param mail_format: body field mail_format.
        :param syslog_format: body field syslog_format.
        :param slack_format: body field slack_format.
        """
        self._require_versions((5,))
        body = self._values({'name': name, 'description': description, 'forward_type': forward_type, 'filter': filter, 'forward_source': forward_source, 'applications': applications, 'time_zone': time_zone, 'mail_format': mail_format, 'syslog_format': syslog_format, 'slack_format': slack_format})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/platform/notifications/v1/rule/{rule_uuid}', method='put',
            path_params={'rule_uuid': rule_uuid},
            body=body,
        )

    def update_rule_status(self, *,
                           rule_uuid: str,
                           status: Union[str, None, UnsetType] = UNSET) -> Any:
        """Edit the status of an existing Alert Notification Rule

        PATCH /platform/notifications/v1/update-rule-status/{rule_uuid}
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, bytes for downloads, or None for an empty response.
        Omit optional fields with UNSET; explicit None is sent as JSON null.
        :param rule_uuid: path field rule_uuid.
        :param status: body field status.
        """
        self._require_versions((5,))
        body = self._values({'status': status})
        body = self._values({'request_data': body, **{}})
        return self._operation(
            '/platform/notifications/v1/update-rule-status/{rule_uuid}', method='patch',
            path_params={'rule_uuid': rule_uuid},
            body=body,
        )
