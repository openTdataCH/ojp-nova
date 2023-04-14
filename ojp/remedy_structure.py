from dataclasses import dataclass, field
from typing import List, Optional
from ojp.extensions_1 import Extensions1
from ojp.natural_language_string_structure import NaturalLanguageStringStructure
from ojp.remedy_type_enumeration import RemedyTypeEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class RemedyStructure:
    """
    Description of the remedy to the change of a facility status (mainly when
    it becomes partially or totally anavailable)

    :ivar remedy_type: Type of the remedy (repair/replacement/remove)
    :ivar description: Description of the set up remedy in natural
        language.  (Unbounded since SIRI 2.0)
    :ivar extensions:
    """
    remedy_type: Optional[RemedyTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "RemedyType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    description: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
