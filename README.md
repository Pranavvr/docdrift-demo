# retry-client

A minimal HTTP client with automatic retries.

## Usage

Call `get(url)` to fetch a page. It returns the response body as text.

## Retries

The client retries 3 times, waiting 2 seconds between attempts.

## Errors

If every attempt fails, `get` raises `ClientError`.
