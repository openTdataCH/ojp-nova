from dataclasses import dataclass, field
from typing import List
from ojp.type_of_value import TypeOfValue

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ValuesStructure:
    """Type for a list of TYPE OF VALUEs.

    (since SIRI 2.1)
    """
    type_of_value: List[TypeOfValue] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfValue",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        }
    )
