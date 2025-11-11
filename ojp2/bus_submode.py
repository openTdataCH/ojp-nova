from dataclasses import dataclass, field

from ojp2.bus_submodes_of_transport_enumeration import (
    BusSubmodesOfTransportEnumeration,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class BusSubmode:
    """
    TPEG Pti05 and Pts105 "BusService" submodes.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: BusSubmodesOfTransportEnumeration = field(
        default=BusSubmodesOfTransportEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
