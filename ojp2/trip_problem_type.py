from dataclasses import dataclass, field
from typing import Optional

from ojp2.trip_problem_type_enumeration import TripProblemTypeEnumeration

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class TripProblemType:
    class Meta:
        namespace = "http://www.vdv.de/ojp"

    value: Optional[TripProblemTypeEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
