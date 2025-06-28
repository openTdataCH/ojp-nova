from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class LevelRefStructure:
    """
    Type for reference to identifier of LEVEL.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
