from abc import ABC, abstractmethod

from fastapi import Response
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig


class SerializerUtil:
    ns_map = {"": "https://www.siri.org.uk/siri", "ojp": "https://www.vdv.de/ojp"}
    _serializer_config = SerializerConfig(
        ignore_default_attributes=True, pretty_print=True
    )
    serializer = XmlSerializer(config=_serializer_config)


ns_map = {"": "https://www.siri.org.uk/siri", "ojp": "https://www.vdv.de/ojp"}
_serializer_config = SerializerConfig(ignore_default_attributes=True, pretty_print=True)
serializer = XmlSerializer(config=_serializer_config)


class OjpFareService(ABC):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    @abstractmethod
    def handle_request(self, body: bytes) -> Response:
        """
        Handles an ojp request.
        """
        return Response(body)
