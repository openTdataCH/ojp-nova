from dataclasses import dataclass, field
from ojp.natural_language_string_structure import NaturalLanguageStringStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class DefaultedTextStructure(NaturalLanguageStringStructure):
    """
    Type for a text that may be overridden.

    :ivar overridden: Whether the text value has been overridden from
        the generated default. Default is 'true'.
    """
    overridden: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )
