from typing import TypedDict


class Request(TypedDict):
    url: str
    method: str
    body: dict
    params: dict
    headers: dict
