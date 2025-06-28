from dataclasses import dataclass, field

from ojp2.coach_submodes_of_transport_enumeration import (
    CoachSubmodesOfTransportEnumeration,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class CoachSubmode:
    """
    TPEG Pti03 and Pts103 "CoachService" submodes.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: CoachSubmodesOfTransportEnumeration = field(
        default=CoachSubmodesOfTransportEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
