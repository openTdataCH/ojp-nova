from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class TariffZoneRefStructure:
    """
    Reference to a fare zone.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
