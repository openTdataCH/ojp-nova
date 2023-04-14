from dataclasses import dataclass, field
from typing import Optional
from ojp.exchange_points_problem_type_enumeration import ExchangePointsProblemTypeEnumeration

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class ExchangePointsProblemType:
    class Meta:
        namespace = "http://www.vdv.de/ojp"

    value: Optional[ExchangePointsProblemTypeEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
