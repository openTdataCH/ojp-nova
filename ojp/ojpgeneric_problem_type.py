from dataclasses import dataclass, field
from typing import Optional
from ojp.ojpgeneric_problem_type_enumeration import OjpgenericProblemTypeEnumeration

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjpgenericProblemType:
    class Meta:
        name = "OJPGenericProblemType"
        namespace = "http://www.vdv.de/ojp"

    value: Optional[OjpgenericProblemTypeEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
