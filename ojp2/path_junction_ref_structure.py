from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class PathJunctionRefStructure:
    """
    Type for reference to a PATH JUNCTION.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
