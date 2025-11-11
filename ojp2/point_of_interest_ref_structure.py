from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class PointOfInterestRefStructure:
    """
    Reference to a Point of Interest.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
