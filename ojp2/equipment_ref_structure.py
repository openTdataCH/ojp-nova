from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class EquipmentRefStructure:
    """
    Type for reference to a EQUIPMENT.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
