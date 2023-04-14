from dataclasses import dataclass, field
from typing import Optional
from ojp.arrival_boarding_activity_enumeration import ArrivalBoardingActivityEnumeration
from ojp.departure_boarding_activity_enumeration import DepartureBoardingActivityEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class BoardingStructure:
    """
    Type for boarding restrictions.

    :ivar arrival_boarding_activity: Type of boarding and alighting
        allowed at stop. Default is 'Alighting'.
    :ivar departure_boarding_activity: Type of alighting allowed at
        stop. Default is 'Boarding'.
    """
    arrival_boarding_activity: Optional[ArrivalBoardingActivityEnumeration] = field(
        default=None,
        metadata={
            "name": "ArrivalBoardingActivity",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    departure_boarding_activity: Optional[DepartureBoardingActivityEnumeration] = field(
        default=None,
        metadata={
            "name": "DepartureBoardingActivity",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
