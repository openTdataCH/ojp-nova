from dataclasses import dataclass
from ojp.natural_language_string_structure import NaturalLanguageStringStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class JourneyNote(NaturalLanguageStringStructure):
    """Additional descriptive text associated with journey.

    Inherited property.
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
