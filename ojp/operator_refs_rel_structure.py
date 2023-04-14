from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OperatorRefsRelStructure:
    class Meta:
        name = "OperatorRefs_RelStructure"

    operator_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OperatorRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "min_occurs": 1,
        }
    )
