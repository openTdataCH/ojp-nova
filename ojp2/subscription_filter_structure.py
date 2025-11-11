from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class SubscriptionFilterStructure:
    """
    Type for unique identifier of Subscription filter within Participant.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
