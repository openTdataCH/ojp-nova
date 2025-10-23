from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class StopPlaceRef1:
    """
    Reference to a STOP PLACE.
    """
    class Meta:
        name = "StopPlaceRef"
        namespace = "http://www.ifopt.org.uk/ifopt"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
