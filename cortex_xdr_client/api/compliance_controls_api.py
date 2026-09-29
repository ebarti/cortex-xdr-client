"""Explicit operations from the pinned Cortex XDR documentation snapshot."""
from typing import Any, Tuple, Union

from cortex_xdr_client.api.operation import UNSET, UnsetType
from cortex_xdr_client.api.authentication import Authentication
from cortex_xdr_client.api.base_api import BaseAPI
from cortex_xdr_client.api.version import APIVersion


class ComplianceControlsAPI(BaseAPI):
    def __init__(self, auth: Authentication, fqdn: str, timeout: Tuple[int, int],
                 api_version: APIVersion = APIVersion.V3) -> None:
        super(ComplianceControlsAPI, self).__init__(auth, fqdn, 'compliance_controls', timeout, api_version)

    def get_assessment_profiles(self, *,
            filters: Union[list, None, UnsetType] = UNSET,
            search_from: Union[int, None, UnsetType] = UNSET,
            search_to: Union[int, None, UnsetType] = UNSET,
            sort: Union[dict, None, UnsetType] = UNSET) -> Any:
        """Get assessment profiles

        POST /public_api/v1/compliance/get_assessment_profiles
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param filters: body field filters.
        :param search_from: body field search_from.
        :param search_to: body field search_to.
        :param sort: body field sort.
        """
        self._require_versions((5,))
        body = self._values({
            'filters': filters,
            'search_from': search_from,
            'search_to': search_to,
            'sort': sort,
        })
        body = {'request_data': body}
        return self._operation(
            '/public_api/v1/compliance/get_assessment_profiles', method='post',
            body=body,
        )

    def get_assessment_profile(self, *, id: str) -> Any:
        """Get assessment profile by ID

        POST /public_api/v1/compliance/get_assessment_profile
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param id: body field id.
        """
        self._require_versions((5,))
        body = self._values({'id': id})
        body = {'request_data': body}
        return self._operation(
            '/public_api/v1/compliance/get_assessment_profile', method='post',
            body=body,
        )

    def add_assessment_profile(self, *,
            asset_group_id: str,
            profile_name: str,
            standard_id: str,
            description: Union[str, None, UnsetType] = UNSET,
            evaluation_frequency: Union[str, None, UnsetType] = UNSET,
            report_targets: Union[list, None, UnsetType] = UNSET,
            report_type: Union[str, None, UnsetType] = UNSET) -> Any:
        """Add assessment profile

        POST /public_api/v1/compliance/add_assessment_profile
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param asset_group_id: body field asset_group_id.
        :param profile_name: body field profile_name.
        :param standard_id: body field standard_id.
        :param description: body field description.
        :param evaluation_frequency: body field evaluation_frequency.
        :param report_targets: body field report_targets.
        :param report_type: body field report_type.
        """
        self._require_versions((5,))
        body = self._values({
            'asset_group_id': asset_group_id,
            'profile_name': profile_name,
            'standard_id': standard_id,
            'description': description,
            'evaluation_frequency': evaluation_frequency,
            'report_targets': report_targets,
            'report_type': report_type,
        })
        body = {'request_data': body}
        return self._operation(
            '/public_api/v1/compliance/add_assessment_profile', method='post',
            body=body,
        )

    def edit_assessment_profile(self, *, field_: Union[dict, None, UnsetType] = UNSET) -> Any:
        """Edit assessment profile

        POST /public_api/v1/compliance/edit_assessment_profile
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param field_: body field .
        """
        self._require_versions((5,))
        body = self._values({'': field_})
        return self._operation(
            '/public_api/v1/compliance/edit_assessment_profile', method='post',
            body=body,
        )

    def delete_assessment_profile(self, *, id: str) -> Any:
        """Delete assessment profile

        POST /public_api/v1/compliance/delete_assessment_profile
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param id: body field id.
        """
        self._require_versions((5,))
        body = self._values({'id': id})
        body = {'request_data': body}
        return self._operation(
            '/public_api/v1/compliance/delete_assessment_profile', method='post',
            body=body,
        )

    def get_assessment_profile_results(self, *,
            filters: Union[list, None, UnsetType] = UNSET) -> Any:
        """Get assessment profile results

        POST /public_api/v1/compliance/get_assessment_results
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param filters: body field filters.
        """
        self._require_versions((5,))
        body = self._values({'filters': filters})
        body = {'request_data': body}
        return self._operation(
            '/public_api/v1/compliance/get_assessment_results', method='post',
            body=body,
        )

    def get_categories_and_subcategories(self) -> Any:
        """Get categories and subcategories (v1)

        POST /public_api/v1/compliance/get_control_categories_and_subcategories
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        """
        self._require_versions((5,))
        body = {'request_data': {}}
        return self._operation(
            '/public_api/v1/compliance/get_control_categories_and_subcategories', method='post',
            body=body,
        )

    def get_compliance_assets(self, *,
            assessment_profile_revision: str,
            last_evaluation_time: int,
            filters: Union[list, None, UnsetType] = UNSET,
            search_from: Union[int, None, UnsetType] = UNSET,
            search_to: Union[int, None, UnsetType] = UNSET,
            sort: Union[dict, None, UnsetType] = UNSET) -> Any:
        """Get compliance assets

        POST /public_api/v1/compliance/get_assets
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param assessment_profile_revision: body field assessment_profile_revision.
        :param last_evaluation_time: body field last_evaluation_time.
        :param filters: body field filters.
        :param search_from: body field search_from.
        :param search_to: body field search_to.
        :param sort: body field sort.
        """
        self._require_versions((5,))
        body = self._values({
            'assessment_profile_revision': assessment_profile_revision,
            'last_evaluation_time': last_evaluation_time,
            'filters': filters,
            'search_from': search_from,
            'search_to': search_to,
            'sort': sort,
        })
        body = {'request_data': body}
        return self._operation(
            '/public_api/v1/compliance/get_assets', method='post',
            body=body,
        )

    def get_controls(self, *,
            filters: Union[list, None, UnsetType] = UNSET,
            search_from: Union[int, None, UnsetType] = UNSET,
            search_to: Union[int, None, UnsetType] = UNSET,
            sort: Union[dict, None, UnsetType] = UNSET) -> Any:
        """Get compliance controls (v1)

        POST /public_api/v1/compliance/get_controls
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param filters: body field filters.
        :param search_from: body field search_from.
        :param search_to: body field search_to.
        :param sort: body field sort.
        """
        self._require_versions((5,))
        body = self._values({
            'filters': filters,
            'search_from': search_from,
            'search_to': search_to,
            'sort': sort,
        })
        body = {'request_data': body}
        return self._operation(
            '/public_api/v1/compliance/get_controls', method='post',
            body=body,
        )

    def get_control(self, *, id: str) -> Any:
        """Get compliance control by ID (v1)

        POST /public_api/v1/compliance/get_control
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param id: body field id.
        """
        self._require_versions((5,))
        body = self._values({'id': id})
        body = {'request_data': body}
        return self._operation(
            '/public_api/v1/compliance/get_control', method='post',
            body=body,
        )

    def add_control(self, *,
            category: str,
            control_name: str,
            description: Union[str, None, UnsetType] = UNSET,
            subcategory: Union[str, None, UnsetType] = UNSET) -> Any:
        """Add new control (v1)

        POST /public_api/v1/compliance/add_control
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param category: body field category.
        :param control_name: body field control_name.
        :param description: body field description.
        :param subcategory: body field subcategory.
        """
        self._require_versions((5,))
        body = self._values({
            'category': category,
            'control_name': control_name,
            'description': description,
            'subcategory': subcategory,
        })
        body = {'request_data': body}
        return self._operation(
            '/public_api/v1/compliance/add_control', method='post',
            body=body,
        )

    def edit_control(self, *,
            id: str,
            category: Union[str, None, UnsetType] = UNSET,
            control_name: Union[str, None, UnsetType] = UNSET,
            description: Union[str, None, UnsetType] = UNSET,
            subcategory: Union[str, None, UnsetType] = UNSET) -> Any:
        """Edit existing control (v1)

        POST /public_api/v1/compliance/edit_control
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param id: body field id.
        :param category: body field category.
        :param control_name: body field control_name.
        :param description: body field description.
        :param subcategory: body field subcategory.
        """
        self._require_versions((5,))
        body = self._values({
            'id': id,
            'category': category,
            'control_name': control_name,
            'description': description,
            'subcategory': subcategory,
        })
        body = {'request_data': body}
        return self._operation(
            '/public_api/v1/compliance/edit_control', method='post',
            body=body,
        )

    def delete_control(self, *, id: str) -> Any:
        """Delete control (v1)

        POST /public_api/v1/compliance/delete_control
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param id: body field id.
        """
        self._require_versions((5,))
        body = self._values({'id': id})
        body = {'request_data': body}
        return self._operation(
            '/public_api/v1/compliance/delete_control', method='post',
            body=body,
        )

    def get_control_by_revision(self, *, control_revision: str) -> Any:
        """Get control by revision (v1)

        POST /public_api/v1/compliance/get_control_by_revision
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param control_revision: body field control_revision.
        """
        self._require_versions((5,))
        body = self._values({'control_revision': control_revision})
        body = {'request_data': body}
        return self._operation(
            '/public_api/v1/compliance/get_control_by_revision', method='post',
            body=body,
        )

    def get_reports(self, *,
            filters: Union[list, None, UnsetType] = UNSET,
            search_from: Union[int, None, UnsetType] = UNSET,
            search_to: Union[int, None, UnsetType] = UNSET,
            sort: Union[dict, None, UnsetType] = UNSET) -> Any:
        """Get compliance reports

        POST /public_api/v1/compliance/get_reports
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param filters: body field filters.
        :param search_from: body field search_from.
        :param search_to: body field search_to.
        :param sort: body field sort.
        """
        self._require_versions((5,))
        body = self._values({
            'filters': filters,
            'search_from': search_from,
            'search_to': search_to,
            'sort': sort,
        })
        body = {'request_data': body}
        return self._operation(
            '/public_api/v1/compliance/get_reports', method='post',
            body=body,
        )

    def get_control_failed_results(self, *,
            assessment_profile_revision: str,
            control_revision: str,
            last_evaluation_time: int) -> Any:
        """Get control failed results

        POST /public_api/v1/compliance/get_control_failed_results
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param assessment_profile_revision: body field assessment_profile_revision.
        :param control_revision: body field control_revision.
        :param last_evaluation_time: body field last_evaluation_time.
        """
        self._require_versions((5,))
        body = self._values({
            'assessment_profile_revision': assessment_profile_revision,
            'control_revision': control_revision,
            'last_evaluation_time': last_evaluation_time,
        })
        body = {'request_data': body}
        return self._operation(
            '/public_api/v1/compliance/get_control_failed_results', method='post',
            body=body,
        )

    def get_rule_failed_results(self, *,
            assessment_profile_revision: str,
            control_revision: str,
            last_evaluation_time: int,
            rule_id: str) -> Any:
        """Get rule failed results

        POST /public_api/v1/compliance/get_rule_failed_results
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param assessment_profile_revision: body field assessment_profile_revision.
        :param control_revision: body field control_revision.
        :param last_evaluation_time: body field last_evaluation_time.
        :param rule_id: body field rule_id.
        """
        self._require_versions((5,))
        body = self._values({
            'assessment_profile_revision': assessment_profile_revision,
            'control_revision': control_revision,
            'last_evaluation_time': last_evaluation_time,
            'rule_id': rule_id,
        })
        body = {'request_data': body}
        return self._operation(
            '/public_api/v1/compliance/get_rule_failed_results', method='post',
            body=body,
        )

    def add_rules_to_control(self, *, control_id: str, rules: list) -> Any:
        """Add compliance rules to a compliance control

        POST /public_api/v1/compliance/add_rules_to_control
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param control_id: body field control_id.
        :param rules: body field rules.
        """
        self._require_versions((5,))
        body = self._values({'control_id': control_id, 'rules': rules})
        body = {'request_data': body}
        return self._operation(
            '/public_api/v1/compliance/add_rules_to_control', method='post',
            body=body,
        )

    def delete_rules_from_control(self, *, control_id: str, rules_ids: list) -> Any:
        """Delete rules from control

        POST /public_api/v1/compliance/delete_rules_from_control
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param control_id: body field control_id.
        :param rules_ids: body field rules_ids.
        """
        self._require_versions((5,))
        body = self._values({'control_id': control_id, 'rules_ids': rules_ids})
        body = {'request_data': body}
        return self._operation(
            '/public_api/v1/compliance/delete_rules_from_control', method='post',
            body=body,
        )

    def get_standards(self, *,
            filters: Union[list, None, UnsetType] = UNSET,
            search_from: Union[int, None, UnsetType] = UNSET,
            search_to: Union[int, None, UnsetType] = UNSET,
            sort: Union[dict, None, UnsetType] = UNSET) -> Any:
        """Get compliance standards (v1)

        POST /public_api/v1/compliance/get_standards
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param filters: body field filters.
        :param search_from: body field search_from.
        :param search_to: body field search_to.
        :param sort: body field sort.
        """
        self._require_versions((5,))
        body = self._values({
            'filters': filters,
            'search_from': search_from,
            'search_to': search_to,
            'sort': sort,
        })
        body = {'request_data': body}
        return self._operation(
            '/public_api/v1/compliance/get_standards', method='post',
            body=body,
        )

    def get_standard(self, *, id: str) -> Any:
        """Get single standard by ID (v1)

        POST /public_api/v1/compliance/get_standard
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param id: body field id.
        """
        self._require_versions((5,))
        body = self._values({'id': id})
        body = {'request_data': body}
        return self._operation(
            '/public_api/v1/compliance/get_standard', method='post',
            body=body,
        )

    def add_standard(self, *,
            standard_name: str,
            controls_ids: Union[list, None, UnsetType] = UNSET,
            description: Union[str, None, UnsetType] = UNSET,
            labels: Union[list, None, UnsetType] = UNSET) -> Any:
        """Add new standard (v1)

        POST /public_api/v1/compliance/add_standard
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param standard_name: body field standard_name.
        :param controls_ids: body field controls_ids.
        :param description: body field description.
        :param labels: body field labels.
        """
        self._require_versions((5,))
        body = self._values({
            'standard_name': standard_name,
            'controls_ids': controls_ids,
            'description': description,
            'labels': labels,
        })
        body = {'request_data': body}
        return self._operation(
            '/public_api/v1/compliance/add_standard', method='post',
            body=body,
        )

    def edit_standard(self, *,
            id: str,
            controls_ids: Union[list, None, UnsetType] = UNSET,
            description: Union[str, None, UnsetType] = UNSET,
            labels: Union[list, None, UnsetType] = UNSET,
            standard_name: Union[str, None, UnsetType] = UNSET) -> Any:
        """Edit existing standard (v1)

        POST /public_api/v1/compliance/edit_standard
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param id: body field id.
        :param controls_ids: body field controls_ids.
        :param description: body field description.
        :param labels: body field labels.
        :param standard_name: body field standard_name.
        """
        self._require_versions((5,))
        body = self._values({
            'id': id,
            'controls_ids': controls_ids,
            'description': description,
            'labels': labels,
            'standard_name': standard_name,
        })
        body = {'request_data': body}
        return self._operation(
            '/public_api/v1/compliance/edit_standard', method='post',
            body=body,
        )

    def delete_standard(self, *, id: str) -> Any:
        """Delete standard (v1)

        POST /public_api/v1/compliance/delete_standard
        Available in Cortex XDR 5.x.
        Returns the complete JSON response, text, bytes, or None for an empty response.
        Optional fields use UNSET for omission; None is explicit null.
        The source snapshot records this operation and its parameter schema.
        :param id: body field id.
        """
        self._require_versions((5,))
        body = self._values({'id': id})
        body = {'request_data': body}
        return self._operation(
            '/public_api/v1/compliance/delete_standard', method='post',
            body=body,
        )
