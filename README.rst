About the cortex-xdr-client
################################

A python-based client for the `Cortex XDR 3.x
<https://cortex-docs.paloaltonetworks.com/xdr-3-api>`__ and `Cortex XDR 5.x
<https://cortex-docs.paloaltonetworks.com/xdr-5-api>`__ APIs.

The client keeps its hand-written API classes, request helpers and Pydantic
models. Standard and Advanced API key authentication work with both versions.

Getting started
===============

.. code-block:: python

    from cortex_xdr_client.api.authentication import Authentication
    from cortex_xdr_client.client import CortexXDRClient

    auth = Authentication(api_key="your-key", api_key_id=123)

    # Existing usage continues to select XDR 3.x.
    legacy = CortexXDRClient(auth, "tenant.example.com")
    incidents = legacy.incidents_api.get_incidents()

    # Select the product version explicitly for an XDR 5.x tenant.
    platform = CortexXDRClient(auth, "api-tenant.example.com", api_version=5)
    endpoints = platform.endpoints_api.get_endpoint()
    cases = platform.cases_api.get_cases(search_from=0, search_to=100)
    issues = platform.issues_api.get_issues(search_from=0, search_to=100)

``api_version`` accepts ``3``, ``5``, ``APIVersion.V3`` or ``APIVersion.V5``
(from ``cortex_xdr_client.api.version``). It selects the **product generation**,
not the number in the URL. Both generations use many ``/public_api/v1/`` routes;
some operations use other prefixes or endpoint versions.

Use the tenant FQDN from the API key examples. A hostname without ``api-``, an
``api-`` hostname, or an HTTPS origin such as ``https://api-tenant.example.com``
is accepted. Do not include an API path. The existing third positional argument
still sets the connect/read timeout, for example ``(10, 60)``.

Supported APIs
==============

The following APIs have dedicated methods and response parsing:

* **Both versions:** endpoints (list, filter, isolate, unisolate, scan, alias,
  retrieve and quarantine files), response action status, file retrieval details,
  downloads, scripts (list, metadata, execution status/results/files, run and
  snippets), XQL queries/results/streams, and JSON indicator insertion.
* **XDR 3.x:** alerts with multiple events, incidents and extra incident data.
* **XDR 5.x:** case search/update/artifacts/schema/timeline; issue
  search/create/update/schema; issue exception creation/search/disable.

On v5, use ``cases_api`` and ``issues_api``. Legacy ``incidents_api`` and
``alerts_api`` methods raise ``NotImplementedError`` with migration guidance
before making a request. Cases and Issues have different fields, filters and
response envelopes, so they have their own models. Their methods likewise
reject v3 clients. No automatic tenant detection or cross-version fallback is
performed.

Searching cases and issues
==========================

.. code-block:: python

    from cortex_xdr_client.api.models.filters import request_filter

    cases = platform.cases_api.get_cases(
        filters=[request_filter("status_progress", "in", ["New"])],
        search_from=0,
        search_to=100,
        sort={"field": "creation_time", "keyword": "desc"},
    )
    for case in cases.reply.data:
        print(case.case_id, case.case_name, case.status_progress)

    issues = platform.issues_api.get_issues(
        filters=[request_filter("severity", "in", ["HIGH", "CRITICAL"])],
        include_fields=["normalized_fields", "custom_fields"],
    )
    for issue in issues.reply.data:
        print(issue.id, issue.detection_method, issue.status_progress)

Case severities are lowercase; issue severities are uppercase. Case and Issue
search results expose ``reply.total_count``, ``reply.filter_count`` and
``reply.data``, corresponding to ``TOTAL_COUNT``, ``FILTER_COUNT`` and ``DATA``.
Dotted issue fields have Python names, for example ``status.progress`` becomes
``status_progress``. Use ``dict(by_alias=True)`` to recover the wire names.
Custom and additional response fields are preserved in the new models.

Case/Issue updates return ``None`` on HTTP 204. Case artifacts return the
unwrapped list from the API. Other new methods return their complete JSON
response unless they have a dedicated response model. Pagination is explicit;
methods retrieve one page per call.

Additional API families
=======================

``client.request`` provides authenticated access to documented operations that
do not have dedicated methods, including the v3 Broker API and the v5 Agent
Configurations, Application Security, Asset Compliance and Notifications APIs.
It returns a ``requests.Response`` and uses the client's timeout and fresh
authentication headers. These families have transport support, not a full set
of typed methods or local request-schema validation.

Supply the **exact path, method and full body** from the documentation for your
tenant version. No prefix is rewritten and no ``request_data`` wrapper is added.
The low-level method does not enforce which product version exposes a path;
the server remains authoritative for availability, licensing and permissions.

.. code-block:: python

    # XDR 3.x Broker API: its GET operation accepts a JSON filter body.
    brokers = legacy.request(
        "/public_api/v1/brokers/",
        method="get",
        json_value={"name": ["broker-eu-01"]},
    ).json()

    # XDR 5.x agent configuration.
    configuration = platform.request(
        "/public_api/v1/configurations/agent/content_management",
    ).json()

    applications = platform.request(
        "/public_api/appsec/v1/application", method="get",
    ).json()

    compliance = platform.request(
        "/public_api/v1/compliance/get_asset",
        json_value={"request_data": {"asset_id": "your-asset-id"}},
    ).json()

    rules = platform.request(
        "/platform/notifications/v1/list-rules", method="get",
    ).json()

Use ``params`` for query parameters, ``json_value`` for JSON, or ``data`` and
``files`` for form/multipart operations. HTTP errors propagate as
``requests.HTTPError``; rate-limit responses are not retried automatically.
Authenticated redirects are rejected to keep credentials on the configured
tenant. Download helpers accept either the file token or the tenant's complete
file-retrieval download URL.

API coverage
============

This is a partial API client. Dedicated wrappers cover 24 of 124 documented v3
operations and 34 of 218 v5 operations in the audited references. Other operations
require ``client.request()`` with caller-supplied paths and payloads; generic
transport does not provide dedicated models or operation-level verification.
See `the coverage inventory <docs/API_COVERAGE.md>`__ for the gaps.

Compatibility notes
===================

* Existing constructor calls and shared API method names remain available.
* Endpoint enum filters now serialize the documented lowercase request values,
  while response enums retain their existing values. XDR 5 cloud filters are
  available on ``get_endpoint``.
* File retrieval nests paths under ``request_data.files``. Incident/case IDs
  belong inside ``request_data``; response actions still use the wire field
  ``incident_id`` on v5.
* Alert filters send lowercase severities and accept ``CRITICAL``. Script
  filters preserve ``False`` and use ``modification_date``. Script IDs accept
  strings as well as existing integer values.
* XQL results follow a returned ``stream_id`` and handle compressed files as
  well as streams already decompressed by requests. Limits above 1,000 are
  forwarded to the server.
* Indicators require only ``indicator``, ``type`` and ``severity``. The existing
  ``IoCSeverity.informational`` maps to ``INFO`` on the wire. The legacy
  ``unknown`` severity is rejected locally for v5, whose schema excludes it.

See `the compatibility audit <docs/API_COMPATIBILITY.md>`__ for sources,
documentation inconsistencies and verification limits.

Contributing
============

See `CONTRIBUTING.md <CONTRIBUTING.md>`__ for setup and testing.
