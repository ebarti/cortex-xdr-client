from typing import List


class Filter:
    field: str
    operator: str
    value: List[str]

    def __init__(self, field: str, operator: str, value: List[str]) -> None:
        self.field = field
        self.operator = operator
        self.value = value


class Sort:
    field: str
    keyword: str

    def __init__(self, field: str, keyword: str) -> None:
        self.field = field
        self.keyword = keyword


class RequestData:
    search_from: int
    search_to: int
    sort: Sort
    filters: List[Filter]

    def __init__(self, search_from: int, search_to: int, sort: Sort, filters: List[Filter]) -> None:
        self.search_from = search_from
        self.search_to = search_to
        self.sort = sort
        self.filters = filters