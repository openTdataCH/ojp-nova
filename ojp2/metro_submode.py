from dataclasses import dataclass, field

from ojp2.metro_submodes_of_transport_enumeration import (
    MetroSubmodesOfTransportEnumeration,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class MetroSubmode:
    """
    TPEG Pti04 metro and Pts104 "UrbanRailwayService" submodes.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: MetroSubmodesOfTransportEnumeration = field(
        default=MetroSubmodesOfTransportEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
