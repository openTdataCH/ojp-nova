from dataclasses import dataclass, field
from typing import Optional
from ojp.trip_info_problem_type_enumeration import TripInfoProblemTypeEnumeration

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class TripInfoProblemType:
    class Meta:
        namespace = "http://www.vdv.de/ojp"

    value: Optional[TripInfoProblemTypeEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
