from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class ParticipantRef:
    """
    Reference to a Participant ([equivalent of PARTICIPANT in SIRI] IT system that
    is participating in a communication with other participant(s))
    """
    class Meta:
        namespace = "http://www.vdv.de/ojp"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
