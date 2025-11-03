from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class JourneyRefStructure:
    """
    Reference to a Journey.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
