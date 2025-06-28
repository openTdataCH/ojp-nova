from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class VehicleRefStructure:
    """
    Reference to a VEHICLE.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
