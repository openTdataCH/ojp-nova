from dataclasses import dataclass

from ojp2.natural_language_string_structure import (
    NaturalLanguageStringStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class PublishedLineName(NaturalLanguageStringStructure):
    """
    Name or Number by which the LINEis known to the public.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
