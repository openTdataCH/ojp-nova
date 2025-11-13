from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class DatedVehicleJourneyRefStructure:
    """
    Type for reference to a Dated VEHICLE JOURNEY.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
