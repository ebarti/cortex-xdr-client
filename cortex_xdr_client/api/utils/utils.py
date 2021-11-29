import json
from datetime import datetime
from enum import Enum
from json import JSONEncoder
from typing import List


def get_enum_values(p: List[Enum]) -> List[str]:
    return [e.value for e in p]


def dump_json(data: object) -> str:
    return json.dumps(data, cls=AllClassEncoder, sort_keys=True, indent=4)


class AllClassEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.datetime):
            return str(o.timestamp() * 1000)
        return o.__dict__