from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class InterchangeRefStructure:
    """
    Type for reference to a SERVICE JOURNEY INTERCHANGE.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
