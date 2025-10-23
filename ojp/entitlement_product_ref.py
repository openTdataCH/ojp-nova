from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class EntitlementProductRef:
    """
    Reference to a a precondition to access a service or to purchase a FARE PRODUCT
    issued by an organisation that may not be a PT operator (eg: military card,
    concessionary card, etc).
    """
    class Meta:
        namespace = "http://www.vdv.de/ojp"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
