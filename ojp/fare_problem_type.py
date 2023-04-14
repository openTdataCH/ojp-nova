from dataclasses import dataclass, field
from typing import Optional
from ojp.fare_problem_type_enumeration import FareProblemTypeEnumeration

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class FareProblemType:
    class Meta:
        namespace = "http://www.vdv.de/ojp"

    value: Optional[FareProblemTypeEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
