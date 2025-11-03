from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ClearDownRefStructure:
    """
    Reference Cleardown identifier of a stop.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
