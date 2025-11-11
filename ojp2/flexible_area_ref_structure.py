from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class FlexibleAreaRefStructure:
    """
    Type for reference to a FLEXIBLE AREA.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
