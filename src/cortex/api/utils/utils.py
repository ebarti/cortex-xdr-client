import json


def dump_json(data: object) -> str:
    return json.dumps(data, default=lambda o: o.__dict__, indent=4)
