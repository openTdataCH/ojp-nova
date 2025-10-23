from dataclasses import dataclass, field
from ojp.arrival_boarding_activity_enumeration import ArrivalBoardingActivityEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ArrivalBoardingActivity:
    """Type of boarding and alighting allowed at stop.

    Default is 'Alighting'.
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: ArrivalBoardingActivityEnumeration = field(
        default=ArrivalBoardingActivityEnumeration.ALIGHTING,
        metadata={
            "required": True,
        }
    )
