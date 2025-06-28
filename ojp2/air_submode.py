from dataclasses import dataclass, field

from ojp2.air_submodes_of_transport_enumeration import (
    AirSubmodesOfTransportEnumeration,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AirSubmode:
    """
    TPEG Pti08 and Pts108 "AirService" submodes.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: AirSubmodesOfTransportEnumeration = field(
        default=AirSubmodesOfTransportEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
