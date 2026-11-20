from unittest.mock import Mock

import pytest
import requests

from appsec_http import HttpClient


def make_response():
    response = Mock()
    response.url = "https://example.test/resource"
    response.status_code = 200
    response.elapsed = None
    response.headers = {"Content-Type": "application/json"}
    response.text = '{"ok": true}'
    response.content = b'{"ok": true}'
    return response


def test_get_returns_normalized_result(monkeypatch):
    client = HttpClient(timeout=3)
    fake_response = make_response()
    captured = {}

    def fake_request(**kwargs):
        captured.update(kwargs)
        return fake_response

    monkeypatch.setattr(client.session, "request", fake_request)

    result = client.get(
        "https://example.test/resource",
        params={"q": "test"},
    )

    assert result.status_code == 200
    assert result.method == "GET"
    assert result.content_length == len(fake_response.content)
    assert captured["timeout"] == 3
    assert captured["verify"] is True
    assert captured["allow_redirects"] is False
    client.close()


def test_rejects_non_http_scheme():
    client = HttpClient()
    with pytest.raises(ValueError, match="http"):
        client.get("file:///etc/passwd")
    client.close()


def test_rejects_non_positive_timeout():
    with pytest.raises(ValueError, match="timeout"):
        HttpClient(timeout=0)


def test_transport_errors_propagate(monkeypatch):
    client = HttpClient()

    def fail_request(**kwargs):
        raise requests.Timeout("request timed out")

    monkeypatch.setattr(client.session, "request", fail_request)

    with pytest.raises(requests.Timeout):
        client.get("https://example.test/")
    client.close()
