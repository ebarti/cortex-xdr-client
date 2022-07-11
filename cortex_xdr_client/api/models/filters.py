from enum import Enum
from typing import List, Any


def request_filter(field: str, operator: str, value: Any) -> dict:
    """
    Creates a filter.

    :param field: Identifies the alert field the filter is matching.
    :param operator: String that identifies the comparison operator you want to use for this filter.
    :param value: Value that this filter must match
    :return: the filter
    """
    return {
        'field': field,
        'operator': operator,
        'value': get_value_for_filter(value)
    }


def request_gte_lte_filter(name: str, value: Any, gte: bool) -> dict:
    operator = "lte"
    if gte:
        operator = "gte"

    return request_filter(name, operator, value)


def request_eq_neq_filter(name: str, value: Any, eq: bool) -> dict:
    operator = "neq"
    if eq:
        operator = "eq"

    return request_filter(name, operator, value)


def request_in_contains_filter(name: str, value: Any, contains: bool) -> dict:
    operator = "in"
    if contains:
        operator = "contains"

    return request_filter(name, operator, value)


def request_field_keyword(field: str, keyword: str) -> dict:
    """
    Creates a sort filter that identifies the sort order for the result set

    :param field: field to sort by
    :param keyword: type of sorting (asc or desc)
    :return:
    """
    return {
        'field': field,
        'keyword': keyword
    }


def get_value_for_filter(value: Any) -> Any:
    if isinstance(value, List):
        return [get_value_for_filter(v) for v in value]
    elif isinstance(value, Enum):
        return value.value
    else:
        return value


def new_request_data(filters: List[dict] = None,
                     sort: dict = None,
                     search_from: int = None,
                     search_to: int = None,
                     other: dict = None) -> dict:
    """

    Creates a new filter request data.
    :param filters: a list of previously created filters
    :param sort: a previously created sort filter
    :param search_from: An integer representing the start offset within the result set from which you want alerts returned.
    :param search_to: An integer representing the end offset within the result set after which you do not  want alerts returned.
    :param other: other filters that will be used to extend request_data
    :return: the filter request data
    """
    request_data = {}
    if filters is not None and len(filters) > 0:
        request_data['filters'] = filters
    if sort is not None:
        request_data['sort'] = sort
    if search_from is not None:
        request_data['search_from'] = search_from
    if search_to is not None:
        request_data['search_to'] = search_to
    if other is not None:
        request_data.update(other)

    return {
        'request_data': request_data
    }
