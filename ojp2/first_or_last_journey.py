from dataclasses import dataclass, field

from ojp2.first_or_last_journey_enumeration import (
    FirstOrLastJourneyEnumeration,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class FirstOrLastJourney:
    """Whether journey is first or last journey of day.

    (since SIRI 2.0)
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: FirstOrLastJourneyEnumeration = field(
        default=FirstOrLastJourneyEnumeration.UNSPECIFIED,
        metadata={
            "required": True,
        },
    )
