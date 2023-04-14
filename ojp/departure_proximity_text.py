from dataclasses import dataclass
from ojp.natural_language_string_structure import NaturalLanguageStringStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class DepartureProximityText(NaturalLanguageStringStructure):
    """Arbitrary text string to show to indicate the status of the departure of
    the vehicle, for example, “Boarding”, “GatesClosed”.

    +SIRI v2.0
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
