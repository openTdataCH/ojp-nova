from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class JourneyPartRefStructure:
    """
    Type for reference to a JOURNEY PART.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
