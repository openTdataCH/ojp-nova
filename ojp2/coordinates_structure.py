from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class CoordinatesStructure:
    """
    Type for GM Coordinates.
    """

    value: list[str] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
