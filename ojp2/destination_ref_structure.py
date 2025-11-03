from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class DestinationRefStructure:
    """
    Type for reference to a DESTINATION.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
