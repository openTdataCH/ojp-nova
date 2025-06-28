from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class StopPlaceRefStructure1:
    """
    Type for reference to a STOP PLACE.
    """

    class Meta:
        name = "StopPlaceRefStructure"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
