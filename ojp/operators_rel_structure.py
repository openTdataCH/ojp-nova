from dataclasses import dataclass, field
from typing import List
from ojp.affected_operator_structure import AffectedOperatorStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OperatorsRelStructure:
    """
    Structure providing a collection of operators.

    :ivar operator: Operator of the service.
    """
    class Meta:
        name = "Operators_RelStructure"

    operator: List[AffectedOperatorStructure] = field(
        default_factory=list,
        metadata={
            "name": "Operator",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "min_occurs": 1,
        }
    )
