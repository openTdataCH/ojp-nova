from dataclasses import dataclass, field
from typing import List, Optional
from ojp.natural_language_string_structure import NaturalLanguageStringStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ActionDataStructure:
    """
    Type for list of SITUATIONs.

    :ivar name: Name of action data Element.
    :ivar type: Data type of action data.
    :ivar value: Value for action.
    :ivar prompt: Display prompt for presenting action to user.
        (Unbounded since SIRI 2.0)
    """
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    value: List[object] = field(
        default_factory=list,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        }
    )
    prompt: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "Prompt",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
