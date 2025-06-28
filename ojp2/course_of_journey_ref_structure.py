from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class CourseOfJourneyRefStructure:
    """
    Type for reference to a COURSE OF JOURNEY (Run).
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
