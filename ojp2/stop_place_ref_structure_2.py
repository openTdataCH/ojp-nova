from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class StopPlaceRefStructure2:
    """
    Reference to a Stop Place.
    """

    class Meta:
        name = "StopPlaceRefStructure"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
