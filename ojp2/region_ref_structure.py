from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class RegionRefStructure:
    """
    Type for a Reference to identifier of Region.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
