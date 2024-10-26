from typing import TypedDict


class Response(TypedDict):
    status_code: int
    headers: dict
    body: str
