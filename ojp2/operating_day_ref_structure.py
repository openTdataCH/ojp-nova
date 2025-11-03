from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OperatingDayRefStructure:
    """
    Reference to an Operating Day.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
