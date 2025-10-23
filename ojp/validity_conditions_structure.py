from dataclasses import dataclass, field
from typing import List
from ojp.validity_condition_structure import ValidityConditionStructure

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class ValidityConditionsStructure:
    """
    A collection of one or more validity conditions.

    :ivar validity_condition: Reference to the identifier of an
        administrative area.
    """
    validity_condition: List[ValidityConditionStructure] = field(
        default_factory=list,
        metadata={
            "name": "ValidityCondition",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
            "min_occurs": 1,
        }
    )
