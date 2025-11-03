from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class FareProductRefStructure:
    """
    Reference to a FareProduct.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
