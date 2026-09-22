# Cortex XDR API compatibility audit

Compared on 2026-09-22. The original client targeted the `/public_api/v1/`
endpoint family now documented under XDR 3.x. Product versions 3 and 5 are not
HTTP API path versions. Shared endpoints retain their published paths.

## Sources

All seven supplied specifications were downloaded and inspected:

| Product | Specification | Paths |
| --- | --- | ---: |
| 3.x | [Core](https://openapi.gitbook.com/o/r4DIGbR5VLvkZy3gAYsu/spec/release-xdr-legacy-cortex-xdr.json) | 106 |
| 3.x | [Broker](https://openapi.gitbook.com/o/r4DIGbR5VLvkZy3gAYsu/spec/release-xdr-legacy-broker-papi.yaml) | 18 |
| 5.x | [Core platform](https://openapi.gitbook.com/o/r4DIGbR5VLvkZy3gAYsu/spec/release-xdr-platform-cortex-platform-papi.json) | 121 |
| 5.x | [Agent configurations](https://openapi.gitbook.com/o/r4DIGbR5VLvkZy3gAYsu/spec/release-xdr-platform-agent-configurations-papi.yaml) | 20 |
| 5.x | [Application Security](https://openapi.gitbook.com/o/r4DIGbR5VLvkZy3gAYsu/spec/release-xdr-platform-appsec-papi.json) | 40 |
| 5.x | [Asset compliance](https://openapi.gitbook.com/o/r4DIGbR5VLvkZy3gAYsu/spec/release-xdr-platform-asset-compliance-papi.yaml) | 1 |
| 5.x | [Notifications](https://openapi.gitbook.com/o/r4DIGbR5VLvkZy3gAYsu/spec/release-xdr-platform-platform-notifications-papi.json) | 4 |

The v5 core download does not contain Cases or Issues. Their endpoint contracts
are embedded as OpenAPI JSON on the [Cases page](https://cortex-docs.paloaltonetworks.com/xdr-5-api/cases-apis/cases)
and [Issues page](https://cortex-docs.paloaltonetworks.com/xdr-5-api/issues-apis/issues).
Those embedded contracts identify themselves as Cortex XDR 5.2; availability on
earlier 5.x tenants must be confirmed against that tenant's documentation.

## Compatibility decisions

- Preserve the hand-written client structure, Pydantic v1 models, Python 3.8
  support, method names and positional timeout argument. Default to v3.
- Use native v5 Cases and Issues methods with their own models. Do not silently
  translate legacy incident status/filter semantics or invent a legacy-shaped
  response. Fail locally when a typed API targets the wrong product generation.
- Reuse the shared routes for endpoints, actions, scripts, XQL, indicators and
  downloads. Keep the wire field `incident_id` where v5 calls it a case ID.
- Provide exact-path transport for the remaining published operations, with
  JSON, query, multipart and all documented HTTP methods. This is not a generated
  SDK or a claim of typed coverage for every operation. The caller supplies the
  version-specific schema, including envelope differences such as `request`
  versus `request_data` on dataset APIs.
- Preserve HTTP errors, caller timeouts and explicit pagination. Do not
  automatically retry response actions after an uncertain result.

## Vendor documentation inconsistencies

- The [v5 getting-started page](https://cortex-docs.paloaltonetworks.com/xdr-5-api)
  illustrates `/XDR/public/v1/`, but the downloaded endpoint contracts and the
  Cases/Issues reference specify `/public_api/v1/` for these operations. Typed
  methods use the endpoint contracts. The low-level request accepts other exact
  tenant-relative paths when explicitly documented for an operation.
- Download tokens/URLs and their POST request are documented in the description
  of `actions/file_retrieval_details`; there is no separate download path in the
  core OpenAPI paths map.
- Application Security contains a malformed path starting with
  `/get /public_api/appsec/v1/package_explorer/...`. The operation inventory
  preserves it as published. No corrected route is guessed or advertised.
- Some schemas and examples disagree: legacy XQL `relativeTime` is typed as a
  string despite integer usage; script filters have differing empty/all
  examples; indicator expiration describes `Never` despite an integer schema.
  The client preserves the documented integer XQL timeframe and accepts `Never`
  for indicator expiration, and follows each version's get-scripts example.
- Both quarantine schemas omit `incident_id`; the existing optional argument is
  retained inside `request_data` for compatibility. Its effect requires tenant
  verification.

## Verification

`tests/fixtures/openapi_operations.json` records source URLs, downloaded-file
SHA-256 values and published paths/methods for the seven downloads and the two
embedded references. `core_responses.json` retains selected current vendor
response examples. Tests run offline and do not depend on live documentation.

Coverage includes both versions' shared typed calls, authentication, exact URLs,
request nesting and enum serialization, current response examples, v5 native
methods, HTTP 202/204, gzip handling, errors, timeouts and representative
transports from every supplemental specification. The old no-op indicator test
now exercises a real mocked request.

Local verification: 172 tests passed on Python 3.8.12 and 3.12.12. The source
distribution and wheel built successfully, and the README passed strict
reStructuredText parsing.

No live tenant credentials were supplied. These tests establish local behavior
against published contracts, not successful authentication, licensing, data
availability or action execution on a real tenant. No tenant actions were run.
