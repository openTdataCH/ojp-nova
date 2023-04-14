from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class TariffZoneRef:
    """
    Reference to a fare zone.
    """
    class Meta:
        namespace = "http://www.vdv.de/ojp"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
