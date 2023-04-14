from dataclasses import dataclass, field
from typing import List
from ojp.type_of_value import TypeOfValue
from ojp.value_set import ValueSet

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class TypesOfValueStructure:
    """Type for containment of VALUE SETs and/or TYPE OF VALUEs.

    (since SIRI 2.1)
    """
    value_set: List[ValueSet] = field(
        default_factory=list,
        metadata={
            "name": "ValueSet",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    type_of_value: List[TypeOfValue] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfValue",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
