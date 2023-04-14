from dataclasses import dataclass, field
from ojp.telecabin_submodes_of_transport_enumeration import TelecabinSubmodesOfTransportEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class TelecabinSubmode:
    """
    TPEG pti09 Telecabin submodes.
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: TelecabinSubmodesOfTransportEnumeration = field(
        default=TelecabinSubmodesOfTransportEnumeration.UNKNOWN,
        metadata={
            "required": True,
        }
    )
