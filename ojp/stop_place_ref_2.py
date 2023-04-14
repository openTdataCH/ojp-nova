from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class StopPlaceRef2:
    """
    Reference to a Stop Place.
    """
    class Meta:
        name = "StopPlaceRef"
        namespace = "http://www.vdv.de/ojp"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
