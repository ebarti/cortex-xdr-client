from typing import List

import requests


class InvalidResponseException(Exception):
    def __init__(self, response: requests.Response, missing_items: List[str]):
        self.response = response
        self.missing_items = missing_items
        super().__init__(self.response, self.missing_items)

    def __str__(self):
        return f'Invalid response from server. \n Got: {self.response.json()}. Missing items: {self.missing_items}'


class UnsuccessfulQueryStatusException(Exception):
    def __init__(self, status: str):
        self.status = status
        super().__init__(self.status)

    def __str__(self):
        return f'Query status was not successful. Got: {self.status}'
