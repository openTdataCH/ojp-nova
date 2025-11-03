from dataclasses import dataclass, field

from ojp2.water_submodes_of_transport_enumeration import (
    WaterSubmodesOfTransportEnumeration,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class WaterSubmode:
    """
    TPEG Pti07 and Pts107 "WaterTransportService" submodes.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: WaterSubmodesOfTransportEnumeration = field(
        default=WaterSubmodesOfTransportEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
