from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class CheckPointRefStructure:
    """
    Type for reference to am identifier of a hazard within a STOP PLACE.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
