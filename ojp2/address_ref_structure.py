from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class AddressRefStructure:
    """
    Reference to an Address.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
