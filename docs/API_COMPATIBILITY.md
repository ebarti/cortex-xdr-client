# Cortex XDR API compatibility audit

Compared on 2026-09-22 and expanded against all indexed 3.x/5.x pages on
2026-09-29. The original client targeted the `/public_api/v1/`
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

## Coverage boundary

The expanded inventory has 124 XDR 3.x operations and 386 XDR 5.x operations,
including 10 indexed Broker VM on-appliance operations. All 510 have dedicated
methods. The initial seven downloads cover only a subset of the indexed 5.x
families; see [the full coverage inventory](API_COVERAGE.md) for the source
snapshot, method catalog and verification limits. Dedicated operation methods
do not imply universal typed Pydantic request/response models.

## Compatibility decisions

- Preserve the hand-written client structure, method names and positional
  timeout argument. Default to XDR v3. Client 2.0 uses Pydantic v2 and Python
  3.11+; see [the model migration notes](PYDANTIC_V2.md).
- Use native v5 Cases and Issues methods with their own models. Do not silently
  translate legacy incident status/filter semantics or invent a legacy-shaped
  response. Fail locally when a typed API targets the wrong product generation.
- Reuse the shared routes for endpoints, actions, scripts, XQL, indicators and
  downloads. Keep the wire field `incident_id` where v5 calls it a case ID.
- Provide dedicated methods for every pinned operation, with named documented
  fields, exact paths, JSON/query/multipart support and version guards. The
  low-level exact-path transport remains available. New methods return complete
  JSON, text, bytes or `None` according to the response and do not invent
  universal typed models or local schema validation. They retain envelope
  differences such as `request` versus `request_data` on dataset APIs.
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
  `/get /public_api/appsec/v1/package_explorer/...`. The catalog preserves the
  literal path and uses the inferred `/public_api/...` wire path. This
  correction requires live tenant confirmation.
- The indexed Broker VM on-appliance API uses a separate broker HTTPS origin,
  password bootstrap and 10-minute Bearer token, so it has an explicit
  `BrokerApplianceClient` and never reuses tenant API-key transport.
- The Forensics server template is malformed and the Policy server is relative;
  these methods use the caller-configured tenant HTTPS origin with the literal
  published path. Three CWP registry operations expose the literal required
  `Authentication` header separately from the normal tenant headers. These
  effective-host/auth decisions still need live tenant confirmation.
- Several indexed blocks omit declarations for placeholders retained in their
  paths; those literal placeholders become required, percent-encoded method
  parameters. The legacy XQL stream reference prints an invalid gzip header
  name; the method sends a valid `Accept-Encoding` header instead.
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
SHA-256 values and published paths/methods for the seven original downloads and
two embedded references. `indexed_openapi_blocks.json` pins the 190 indexed
page URLs, hashes and embedded blocks. `core_responses.json` retains selected
vendor response examples. Tests run offline and do not depend on live docs.

Coverage includes both versions' shared typed calls, authentication, exact URLs,
request nesting and enum serialization, current response examples, v5 native
methods, HTTP 202/204, gzip handling, errors, timeouts and representative
transports from every supplemental specification. The old no-op indicator test
now exercises a real mocked request.

The original response tests now use independent expected URLs. Additional
request contracts check script identity/targets/parameters, action lookups,
response-action targets, XQL timeframes and incident filters/pagination. In
isolated copies, the suite detects ten deliberate regressions: wrong API prefix,
missing authentication, empty bodies, ignored HTTP errors/timeouts, wrong script
ID, lost script targets/parameters, wrong snippet code and ignored script timeout.
These targeted probes are not an exhaustive mutation score or full API coverage.

The compatibility layer's earlier 210-test result predates the full-coverage
work. The current operation-contract suite and build checks are reported on the
follow-up pull request. Client 2.0 model migration is described in
[the migration notes](PYDANTIC_V2.md).

No live tenant credentials were supplied. These tests establish local behavior
against published contracts, not successful authentication, licensing, data
availability or action execution on a real tenant. No tenant actions were run.
