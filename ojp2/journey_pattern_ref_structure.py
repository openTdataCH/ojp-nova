from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class JourneyPatternRefStructure:
    """
    Type for refrence to a JOURNEY PATTERN.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
