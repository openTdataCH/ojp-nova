from dataclasses import dataclass

from ojp2.natural_language_string_structure import (
    NaturalLanguageStringStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class RouteName(NaturalLanguageStringStructure):
    """
    Description of route by which it can be recogniozed.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
