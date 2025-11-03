from dataclasses import dataclass, field

from ojp2.stop_point_type_enumeration import StopPointTypeEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class StopPointType:
    """STOP POINT type - TPEG Pts017, ServiceDeliveryPointType"""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: StopPointTypeEnumeration = field(
        default=StopPointTypeEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
