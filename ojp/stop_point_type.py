from dataclasses import dataclass, field
from ojp.stop_point_type_enumeration import StopPointTypeEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class StopPointType:
    """
    STOP POINT type Tpeg Report Type pti17.
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: StopPointTypeEnumeration = field(
        default=StopPointTypeEnumeration.UNKNOWN,
        metadata={
            "required": True,
        }
    )
