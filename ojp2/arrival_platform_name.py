from dataclasses import dataclass

from ojp2.natural_language_string_structure import (
    NaturalLanguageStringStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ArrivalPlatformName(NaturalLanguageStringStructure):
    """Bay or platform (QUAY) name to show passenger i.e. expected platform for
    vehicle to arrive at.

    Inheritable property. Can be omitted if the same as the
    DeparturePlatformName If there no arrival platform name separate
    from the departure platform name, the precedence is: (i) any arrival
    platform on any related dated timetable element, (ii) any departure
    platform name on this estimated element; (iii) any departure
    platform name on any related dated timetable CALL.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
