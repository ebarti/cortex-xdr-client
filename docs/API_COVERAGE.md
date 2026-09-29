# Dedicated API coverage

This client is **not a complete SDK for either product generation**. The XDR
3.x/5.x compatibility changes update the existing API wrappers, add native
Cases/Issues wrappers, and provide authenticated transport for other operations.
Generic `client.request()` access does not count as a dedicated wrapper or as
verification of that operation's schema and behavior.

The table below compares the client with the specifications downloaded on
2026-09-22. An operation means one HTTP method plus one path, not just a path.
Source URLs, hashes and the full operation inventory are in
[`openapi_operations.json`](../tests/fixtures/openapi_operations.json).

| Product | Reference | Published operations | Dedicated wrappers | Without wrappers |
| --- | --- | ---: | ---: | ---: |
| 3.x | Core | 106 | 24 | 82 |
| 3.x | Broker | 18 | 0 | 18 |
| **3.x total** | | **124** | **24** | **100** |
| 5.x | Core platform | 121 | 21 | 100 |
| 5.x | Agent configurations | 20 | 0 | 20 |
| 5.x | Application Security | 55 | 0 | 55 |
| 5.x | Asset compliance | 1 | 0 | 1 |
| 5.x | Notifications | 6 | 0 | 6 |
| 5.x | Cases reference | 8 | 6 | 2 |
| 5.x | Issues reference | 7 | 7 | 0 |
| **5.x total** | | **218** | **34** | **184** |

The five v5 downloads contain 203 operations; the embedded Cases/Issues
references add 15. Cases/Issues describe XDR 5.2. The download helper is not
counted because its route is described in prose rather than the paths inventory.
Aliases such as `start_xql` and conveniences such as `scan_all_endpoints` do not
count twice. The malformed AppSec route remains in the published denominator;
its corrected route has not been verified.

## What has dedicated wrappers

- Both products: eight endpoint operations (`get_endpoints`, `get_endpoint`,
  `isolate`, `unisolate`, `scan`, `update_agent_name`, `file_retrieval`,
  `quarantine`), two action lookups, seven script operations, three XQL operations
  and indicator insertion.
- XDR 3.x: incident search, extra incident data and multi-event alert search.
- XDR 5.x: case search/update/artifacts/schema/timeline/add-record and all seven
  operations in the supplied Issues reference (including issue exceptions).

Some wrappers return dictionaries, and the models cover selected documented
fields. These counts do not imply fully typed request/response schemas or every
optional parameter for each operation.

## What remains

All operations in the supplemental families lack dedicated wrappers. Core
coverage is also partial: examples include distributions, RBAC, integrations,
audit logs, device control and additional endpoint/XQL operations. The v5 core
also includes assets/groups, API keys, BIOCs, correlations, dashboards/widgets,
playbooks, policies and scheduled queries without wrappers.

The Cases reference's `/public_api/v1/entries/get` and
`/public_api/v1/entries/insert` operations are not wrapped.

These operations require callers to use `client.request()` with the documented
method, exact path and complete payload, and interpret the raw response. Only
representative generic transport calls are tested; the inventory is not an
endpoint-by-endpoint test suite. No live tenant validation has been performed.
