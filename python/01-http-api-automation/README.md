# HTTP/API Security Testing

A reusable Python HTTP client foundation for authorized application-security testing.

## Scope

This module provides:
- reusable HTTP sessions;
- explicit request timeouts;
- TLS certificate verification enabled by default;
- configurable headers, query parameters, and JSON bodies;
- response metadata and elapsed-time inspection;
- predictable handling of transport errors.

It is an HTTP testing foundation, not an automated vulnerability scanner. A successful HTTP response does not prove that an application is secure or vulnerable.

## Requirements

- Python 3.10+
- Dependencies in `requirements.txt`

## Setup

```bash
python -m venv .venv

# Windows PowerShell
.venv\Scripts\Activate.ps1

# Linux/macOS
source .venv/bin/activate

pip install -r requirements.txt
```

## Quick start

```python
from appsec_http import HttpClient

with HttpClient(timeout=10) as client:
    response = client.get(
        "https://httpbin.org/get",
        params={"source": "appsec-toolkit"},
        headers={"User-Agent": "AppSec-Scripting-Toolkit/0.1"},
    )

    print("Status:", response.status_code)
    print("Elapsed:", response.elapsed_ms, "ms")
    print("Content-Type:", response.headers.get("Content-Type"))
    print("Body preview:", response.body_preview)
```

Use only systems you own or are explicitly authorized to test. Start with a local lab such as OWASP Juice Shop or a deliberately vulnerable test application. Do not use this module to generate high-volume traffic.

## Run tests

```bash
pytest -q
```

## Design decisions

- `verify_tls=True` is the default. Disabling TLS verification should be limited to controlled local labs.
- A finite timeout is always configured to avoid indefinitely hanging requests.
- The client does not automatically retry requests. Retrying non-idempotent operations can duplicate actions.
- Response bodies are represented by a bounded preview in the result object; avoid logging secrets or personal data.
- The library does not automatically follow redirects unless explicitly configured.

## Current status

Initial implementation: HTTP client foundation and unit tests. Authentication helpers, CLI workflows, and additional security checks are planned for later iterations.
