from dataclasses import dataclass
from ojp.natural_language_string_structure import NaturalLanguageStringStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AimedLocationName(NaturalLanguageStringStructure):
    """Name or description (e.g. address) of the scheduled location or flexible
    area.

    (since SIRI 2.1)
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
