from dataclasses import dataclass, field
from ojp.air_submodes_of_transport_enumeration import AirSubmodesOfTransportEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AirSubmode:
    """
    TPEG pti08 Air submodes.
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: AirSubmodesOfTransportEnumeration = field(
        default=AirSubmodesOfTransportEnumeration.UNKNOWN,
        metadata={
            "required": True,
        }
    )
