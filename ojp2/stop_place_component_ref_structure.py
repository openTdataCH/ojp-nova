from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class StopPlaceComponentRefStructure:
    """
    Type for reference to STOP PLACE.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
