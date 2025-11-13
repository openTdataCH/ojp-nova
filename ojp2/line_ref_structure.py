from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class LineRefStructure:
    """
    Type for reference to a LINE.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
