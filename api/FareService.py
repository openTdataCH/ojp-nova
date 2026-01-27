#!/usr/bin/env python3
import logging
from abc import abstractmethod, ABC
from fastapi import Request, Response
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig


class FareService(ABC):
    ns_map = {"": "http://www.siri.org.uk/siri", "ojp": "http://www.vdv.de/ojp"}
    _serializer_config = SerializerConfig(ignore_default_attributes=True, pretty_print=True)
    serializer = XmlSerializer(config=_serializer_config)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    @abstractmethod
    def handle_request(self, body: bytes) -> Response:
        return Response(body)
