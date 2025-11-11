from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class VehicleJourneyRefStructure:
    """
    Type for reference to a VEHICLE JOURNEY.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
