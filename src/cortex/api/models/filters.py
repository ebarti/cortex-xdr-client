from typing import List


class Filter:
    field: str
    operator: str
    value: object

    def __init__(self, field: str, operator: str, value: object) -> None:
        self.field = field
        self.operator = operator
        self.value = value


class Sort:
    field: str
    keyword: str

    def __init__(self, field: str, keyword: str) -> None:
        self.field = field
        self.keyword = keyword


class FilterRequestDataItem:
    search_from: int
    search_to: int
    sort: Sort
    filters: List[Filter]

    def __init__(self, search_from: int = None, search_to: int = None, sort: Sort = None, filters: List[Filter] = None) -> None:
        self.search_from = search_from
        self.search_to = search_to
        self.sort = sort
        self.filters = filters


class FilterRequestData:
    request_data: FilterRequestDataItem

    def __init__(self, request_data: FilterRequestDataItem = None) -> None:
        if request_data is None:
            self.request_data = {}
        else:
            self.request_data = request_data


class GetIncidentExtraDataItem:
    incident_id: str
    alerts_limit: int

    def __init__(self, incident_id: str, alerts_limit: int) -> None:
        self.incident_id = incident_id
        self.alerts_limit = alerts_limit


class GetIncidentExtraDataRequestData:
    request_data: GetIncidentExtraDataItem

    def __init__(self, request_data: GetIncidentExtraDataItem = None) -> None:
        if request_data is None:
            self.request_data = {}
        else:
            self.request_data = request_data
