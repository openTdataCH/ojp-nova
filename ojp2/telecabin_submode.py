from dataclasses import dataclass, field

from ojp2.telecabin_submodes_of_transport_enumeration import (
    TelecabinSubmodesOfTransportEnumeration,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class TelecabinSubmode:
    """
    TPEG Pti09 telecabin and Pts109 "GondolaCableCarService" submodes.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: TelecabinSubmodesOfTransportEnumeration = field(
        default=TelecabinSubmodesOfTransportEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
