from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class TopographicPlaceRefStructure:
    """
    Reference to a TopographicPlace.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
