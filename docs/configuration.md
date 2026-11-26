# Configuration

All settings live at the top of `client.py`.

## Settings

- `MAX_RETRIES`: how many attempts the client makes before giving up. Default: 3.
- `BACKOFF_SECONDS`: how long to wait between attempts. Default: 2.
- `TIMEOUT_SECONDS`: how long a single attempt may take. Default: 10.
