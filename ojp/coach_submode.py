from dataclasses import dataclass, field
from ojp.coach_submodes_of_transport_enumeration import CoachSubmodesOfTransportEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class CoachSubmode:
    """
    TPEG pti03 Coach submodes.
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: CoachSubmodesOfTransportEnumeration = field(
        default=CoachSubmodesOfTransportEnumeration.UNKNOWN,
        metadata={
            "required": True,
        }
    )
