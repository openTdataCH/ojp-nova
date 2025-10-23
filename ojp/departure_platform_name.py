from dataclasses import dataclass
from ojp.natural_language_string_structure import NaturalLanguageStringStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class DeparturePlatformName(NaturalLanguageStringStructure):
    """Departure QUAY ( Bay or platform) name.

    Inheritable property.
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
