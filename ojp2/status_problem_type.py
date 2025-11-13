from dataclasses import dataclass, field
from typing import Optional

from ojp2.status_problem_type_enumeration import StatusProblemTypeEnumeration

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class StatusProblemType:
    class Meta:
        namespace = "http://www.vdv.de/ojp"

    value: Optional[StatusProblemTypeEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
