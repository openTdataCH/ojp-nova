from dataclasses import dataclass, field
from typing import Optional
from ojp.availability_problem_type_enumeration import AvailabilityProblemTypeEnumeration

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class AvailabilityProblemType:
    class Meta:
        namespace = "http://www.vdv.de/ojp"

    value: Optional[AvailabilityProblemTypeEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
