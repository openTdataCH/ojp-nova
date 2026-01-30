#!/usr/bin/env python3
from abc import abstractmethod, ABC

from fastapi import Response


class FareService(ABC):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    @abstractmethod
    def handle_request(self, body: bytes) -> Response:
        return Response(body)
