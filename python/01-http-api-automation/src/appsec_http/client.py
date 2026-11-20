"""A small, reusable HTTP client for authorized security testing."""

from __future__ import annotations

from dataclasses import dataclass
from time import perf_counter
from typing import Any, Mapping

import requests


@dataclass(frozen=True)
class HttpResult:
    """A bounded, inspection-friendly representation of an HTTP response."""

    url: str
    method: str
    status_code: int
    elapsed_ms: float
    headers: Mapping[str, str]
    body_preview: str
    content_length: int


class HttpClient:
    """Session-based HTTP client with conservative security defaults."""

    def __init__(
        self,
        *,
        timeout: float = 10.0,
        verify_tls: bool = True,
        follow_redirects: bool = False,
        user_agent: str = "AppSec-Scripting-Toolkit/0.1",
    ) -> None:
        if timeout <= 0:
            raise ValueError("timeout must be greater than zero")

        self.timeout = timeout
        self.verify_tls = verify_tls
        self.follow_redirects = follow_redirects
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": user_agent})

    def close(self) -> None:
        """Close the underlying connection pool."""
        self.session.close()

    def __enter__(self) -> "HttpClient":
        return self

    def __exit__(self, exc_type: Any, exc: Any, traceback: Any) -> None:
        self.close()

    def request(
        self,
        method: str,
        url: str,
        *,
        params: Mapping[str, Any] | None = None,
        headers: Mapping[str, str] | None = None,
        json: Any = None,
        data: Any = None,
        allow_redirects: bool | None = None,
    ) -> HttpResult:
        """Send one request and return normalized response metadata.

        Requests exceptions intentionally propagate to the caller so that
        applications can distinguish timeouts, TLS failures, and connection
        errors without silently treating them as successful responses.
        """
        if not url.lower().startswith(("http://", "https://")):
            raise ValueError("url must use http:// or https://")

        redirect_setting = (
            self.follow_redirects
            if allow_redirects is None
            else allow_redirects
        )

        started = perf_counter()
        response = self.session.request(
            method=method.upper(),
            url=url,
            params=params,
            headers=headers,
            json=json,
            data=data,
            timeout=self.timeout,
            verify=self.verify_tls,
            allow_redirects=redirect_setting,
        )
        elapsed_ms = (perf_counter() - started) * 1000

        # Decode a bounded preview only; do not retain an unlimited body.
        preview = response.text[:500]
        return HttpResult(
            url=response.url,
            method=method.upper(),
            status_code=response.status_code,
            elapsed_ms=round(elapsed_ms, 2),
            headers=dict(response.headers),
            body_preview=preview,
            content_length=len(response.content),
        )

    def get(self, url: str, **kwargs: Any) -> HttpResult:
        return self.request("GET", url, **kwargs)

    def post(self, url: str, **kwargs: Any) -> HttpResult:
        return self.request("POST", url, **kwargs)

    def put(self, url: str, **kwargs: Any) -> HttpResult:
        return self.request("PUT", url, **kwargs)

    def patch(self, url: str, **kwargs: Any) -> HttpResult:
        return self.request("PATCH", url, **kwargs)

    def delete(self, url: str, **kwargs: Any) -> HttpResult:
        return self.request("DELETE", url, **kwargs)
