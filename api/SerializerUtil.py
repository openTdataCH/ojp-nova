from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

class SerializerUtil:
    ns_map = {"": "http://www.siri.org.uk/siri", "ojp": "http://www.vdv.de/ojp"}
    _serializer_config = SerializerConfig(ignore_default_attributes=True, pretty_print=True)
    serializer = XmlSerializer(config=_serializer_config)
