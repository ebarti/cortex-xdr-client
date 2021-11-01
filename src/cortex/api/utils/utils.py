import json
from typing import  List

from cortex.api.utils.constants import Constants


def dump_json(data: object) -> str:
    return json.dumps(data, default=lambda o: o.__dict__, indent=4)


def are_severities_valid(severities: List[str]) -> bool:
    return all(x in Constants.SEVERITIES for x in severities)