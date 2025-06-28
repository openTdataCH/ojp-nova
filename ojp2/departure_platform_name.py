from dataclasses import dataclass

from ojp2.natural_language_string_structure import (
    NaturalLanguageStringStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class DeparturePlatformName(NaturalLanguageStringStructure):
    """Departure QUAY (bay or platform) name.

    Default taken from planned timetable.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
