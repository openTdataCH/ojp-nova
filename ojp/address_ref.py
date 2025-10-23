from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class AddressRef:
    """
    Reference to an Address.
    """
    class Meta:
        namespace = "http://www.vdv.de/ojp"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
