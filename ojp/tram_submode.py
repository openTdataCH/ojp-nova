from dataclasses import dataclass, field
from ojp.tram_submodes_of_transport_enumeration import TramSubmodesOfTransportEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class TramSubmode:
    """
    TPEG pti06 Tram submodes.
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: TramSubmodesOfTransportEnumeration = field(
        default=TramSubmodesOfTransportEnumeration.UNKNOWN,
        metadata={
            "required": True,
        }
    )
