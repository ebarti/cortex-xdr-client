# Migrating to client 2.0

Client 2.0 requires Python 3.11+ and Pydantic 2.13.5 or later within v2.
The client release number is independent of the Cortex product version:
both XDR 3.x and XDR 5.x remain supported, and the default is still XDR 3.x.
Applications requiring Python 3.8-3.10 or Pydantic v1 should stay on client 1.x.

## Model methods

The models now use Pydantic v2 directly, without the `pydantic.v1` compatibility
layer. Update application code that consumes model responses:

| Pydantic v1 | Pydantic v2 |
| --- | --- |
| `Model.parse_obj(data)` | `Model.model_validate(data)` |
| `Model.parse_raw(json_text)` | `Model.model_validate_json(json_text)` |
| `response.dict()` | `response.model_dump()` |
| `response.json()` | `response.model_dump_json()` |
| `response.copy()` | `response.model_copy()` |
| `Model.__fields__` | `Model.model_fields` |
| `response.reply.data.__root__` | `response.reply.data.root` |

Action status uses `RootModel`; dumping the response still produces the same
mapping under `reply.data`, with no additional `root` key in the API payload.
The historical `ActionStatuStr` class name remains available.

Use `model_dump(mode='json', by_alias=True)` for a JSON-compatible dictionary
with API field names. Ordinary `model_dump()` keeps Python values, including
datetime objects and enums. HTTP responses returned by `client.request()` still
use Requests' `.json()` method.

## Shared response base

`CortexResponseModel` preserves new fields returned by the server, including
fields in nested response objects. It accepts either model field names or API
aliases, such as `total_count` / `TOTAL_COUNT` and `status_progress` /
`status.progress`. Additional fields are included in model dumps.

Known fields retain their declared types. Structured strings/lists such as
script output and alert descriptions keep their original shape; there is no
wildcard validator that converts arbitrary objects to strings. Response enum
behavior is preserved: endpoints and incidents expose enum members, while
alerts continue to expose severity values as strings.

Request models (`IoC` and `Vendor`) do not inherit the permissive response base.
They retain their required fields and exclude unknown input fields from outgoing
payloads. Optional fields explicitly default to `None`, preserving their v1
missing-field behavior. Required response envelopes and fields stay required.

Native v2 validation rules apply. In particular, numbers are not implicitly
converted to strings, fractional numbers do not validate as integers, and
models are not equal to plain dictionaries. Compare `model_dump()` results
when dictionary equality is intended. See the [official Pydantic migration
guide](https://docs.pydantic.dev/latest/migration/) for additional differences.

## Verification

The 220-test offline suite passes on Python 3.11, 3.12, 3.13 and 3.14 with
Pydantic 2.13.5 and deprecation warnings treated as errors. It covers both XDR
generations, sparse responses, required fields, nested additional fields,
aliases, enums, structured outputs, action status mappings and request payloads.
The Poetry-locked environment also passes all 220 tests. The wheel and source
distribution build successfully, and Sphinx builds with warnings treated as
errors using the updated documentation dependencies.

No live tenant credentials were supplied. Validation remains against published
contracts and mocked HTTP responses; see [API compatibility](API_COMPATIBILITY.md)
for the API coverage and limitations.
