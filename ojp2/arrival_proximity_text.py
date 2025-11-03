from dataclasses import dataclass

from ojp2.natural_language_string_structure import (
    NaturalLanguageStringStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ArrivalProximityText(NaturalLanguageStringStructure):
    """Arbitrary text string to show to indicate the status of the departure of the
    VEHICLE for example, “Enroute”, “5 Km”, “Approaching”.

    May depend on the policy of the OPERATOR, for example show
    “Approaching” if less than 200metres away from stop. (since SIRI
    2.0)
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
