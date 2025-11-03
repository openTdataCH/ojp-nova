from dataclasses import dataclass, field

from ojp2.funicular_submodes_of_transport_enumeration import (
    FunicularSubmodesOfTransportEnumeration,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class FunicularSubmode:
    """
    TPEG pti10 Funicular submodes.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: FunicularSubmodesOfTransportEnumeration = field(
        default=FunicularSubmodesOfTransportEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
