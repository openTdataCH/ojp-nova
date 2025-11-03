from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class EquipmentTypeRefStructure:
    """
    Type for TYPE OF EQUIPMENT.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
