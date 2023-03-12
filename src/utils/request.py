import requests
from typing import (
    Any,
)


def send_request(url: str, action: str, **kwargs) -> Any:
    """Reference: https://docs.python-requests.org/en/latest/user/quickstart/#make-a-request"""

    # Get the request function by mapping dict
    mapping = {
        "GET":     requests.get,
        "POST":    requests.post,
        "PUT":     requests.put,
        "DELETE":  requests.delete,
        "OPTIONS": requests.options,
    }
    if action not in mapping:
        raise ValueError(f'action [{action}] does not exist')
    resp = mapping[action](url, **kwargs)

    # Raise HTTPError, if one occurred
    resp.raise_for_status()

    # Determine whether to return json or text by header of the response
    return resp.json() if resp.headers.get('content-type') == 'application/json' else resp.text()
