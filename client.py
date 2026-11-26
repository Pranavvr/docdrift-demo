"""retry-client: a minimal HTTP client with automatic retries."""

import time
import urllib.request

MAX_RETRIES = 3
BACKOFF_SECONDS = 2
TIMEOUT_SECONDS = 10


class ClientError(Exception):
    """Raised when a request still fails after all retries."""


def get(url):
    """Fetch url and return the response body as text."""
    for attempt in range(MAX_RETRIES):
        try:
            with urllib.request.urlopen(url, timeout=TIMEOUT_SECONDS) as resp:
                return resp.read().decode()
        except OSError:
            if attempt < MAX_RETRIES - 1:
                time.sleep(BACKOFF_SECONDS)
    raise ClientError(f"GET {url} failed after {MAX_RETRIES} attempts")
