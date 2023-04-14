from dataclasses import dataclass, field
from typing import List, Optional
from ojp.extensions_2 import Extensions2
from ojp.natural_language_string_structure import NaturalLanguageStringStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class RecommendedActionStructure:
    """
    Description of the recommended action for passengers on how to deal with
    changes, for example of the TRAIN formation.

    :ivar type_of_action_ref: Type of the recommendation, e.g.
        'unknown', 'replacement' or 'otherRoute'.
    :ivar description: Description of the recommended action in natural
        language.
    :ivar extensions:
    """
    type_of_action_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "TypeOfActionRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
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
    extensions: Optional[Extensions2] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
