from dataclasses import dataclass, field
from ojp.metro_submodes_of_transport_enumeration import MetroSubmodesOfTransportEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class MetroSubmode:
    """
    TPEG pti04 Metro submodes.
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: MetroSubmodesOfTransportEnumeration = field(
        default=MetroSubmodesOfTransportEnumeration.UNKNOWN,
        metadata={
            "required": True,
        }
    )
