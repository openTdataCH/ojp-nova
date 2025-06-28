from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class SubscriptionQualifierStructure:
    """
    Type for unique identifier of Subscription within Participant.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
