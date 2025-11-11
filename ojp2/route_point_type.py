from dataclasses import dataclass, field

from ojp2.route_point_type_enumeration import RoutePointTypeEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class RoutePointType:
    """
    Type for ROUTE POINT.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: RoutePointTypeEnumeration = field(
        default=RoutePointTypeEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
