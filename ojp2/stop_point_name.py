from dataclasses import dataclass

from ojp2.natural_language_string_structure import (
    NaturalLanguageStringStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class StopPointName(NaturalLanguageStringStructure):
    """
    Name of SCHEDULED STOP POINT.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
