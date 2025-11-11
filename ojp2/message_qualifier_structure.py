from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class MessageQualifierStructure:
    """
    Unique identifier of a message within SIRI functional service type and
    participant.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
