from dataclasses import dataclass, field

from ojp2.taxi_submodes_of_transport_enumeration import (
    TaxiSubmodesOfTransportEnumeration,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class TaxiSubmode:
    """
    TPEG pti11 Taxi submodes.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: TaxiSubmodesOfTransportEnumeration = field(
        default=TaxiSubmodesOfTransportEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
