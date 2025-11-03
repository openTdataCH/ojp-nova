from dataclasses import dataclass, field
from typing import Optional

from ojp2.trip_change_problem_type_enumeration import (
    TripChangeProblemTypeEnumeration,
)

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class TripChangeProblemType:
    class Meta:
        namespace = "http://www.vdv.de/ojp"

    value: Optional[TripChangeProblemTypeEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
