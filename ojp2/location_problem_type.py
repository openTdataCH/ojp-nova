from dataclasses import dataclass, field
from typing import Optional

from ojp2.location_problem_type_enumeration import (
    LocationProblemTypeEnumeration,
)

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class LocationProblemType:
    class Meta:
        namespace = "http://www.vdv.de/ojp"

    value: Optional[LocationProblemTypeEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
