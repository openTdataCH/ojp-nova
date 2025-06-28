from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class DirectionRefStructure:
    """
    Reference to a DIRECTION.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
