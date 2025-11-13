from dataclasses import dataclass, field

from ojp2.rail_submodes_of_transport_enumeration import (
    RailSubmodesOfTransportEnumeration,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class RailSubmode:
    """
    TPEG Pti02, Pts102 "RailwayService" and train link loc13 submodes.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: RailSubmodesOfTransportEnumeration = field(
        default=RailSubmodesOfTransportEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
