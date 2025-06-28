from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class JourneyPlaceRefStructure:
    """
    Reference to a PLACE visited by a VEHICLE JOURNEY.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
