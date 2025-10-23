from dataclasses import dataclass, field
from ojp.route_point_type_enumeration import RoutePointTypeEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class RoutePointType:
    """
    Route point type Tpeg Report Type pti15.
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: RoutePointTypeEnumeration = field(
        default=RoutePointTypeEnumeration.UNKNOWN,
        metadata={
            "required": True,
        }
    )
