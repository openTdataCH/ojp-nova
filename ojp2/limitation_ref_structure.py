from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.ifopt.org.uk/acsb"


@dataclass
class LimitationRefStructure:
    """
    Type for reference to an identifier of a hazard within a STOP PLACE.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
