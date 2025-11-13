from dataclasses import dataclass, field

from ojp2.departure_boarding_activity_enumeration import (
    DepartureBoardingActivityEnumeration,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class DepartureBoardingActivity:
    """Nature of boarding allowed at stop.

    Default is 'Boarding'.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: DepartureBoardingActivityEnumeration = field(
        default=DepartureBoardingActivityEnumeration.BOARDING,
        metadata={
            "required": True,
        },
    )
