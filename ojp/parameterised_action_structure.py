from dataclasses import dataclass, field
from typing import List, Optional
from ojp.action_data_structure import ActionDataStructure
from ojp.natural_language_string_structure import NaturalLanguageStringStructure
from ojp.simple_action_structure import SimpleActionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ParameterisedActionStructure(SimpleActionStructure):
    """
    Type for parameterised, i.e. user definable, actions.

    :ivar description: Description of action.
    :ivar action_data: Data associated with action.
    """
    description: Optional[NaturalLanguageStringStructure] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    action_data: List[ActionDataStructure] = field(
        default_factory=list,
        metadata={
            "name": "ActionData",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
