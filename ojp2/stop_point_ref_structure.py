from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class StopPointRefStructure:
    """
    Reference to a SCHEDULED STOP POINT.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
