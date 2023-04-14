from dataclasses import dataclass, field
from typing import List, Optional
from ojp.error_message_structure import ErrorMessageStructure
from ojp.exchange_points_result_structure import ExchangePointsResultStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class ExchangePointsResponseStructure:
    """
    :ivar error_message:
    :ivar continue_at: If the response returns less results than
        expected, the value of skip can be used in a follow-up request
        to get further results. It tells the server to skip the given
        number of results in its response.
    :ivar place:
    """
    error_message: List[ErrorMessageStructure] = field(
        default_factory=list,
        metadata={
            "name": "ErrorMessage",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    continue_at: Optional[int] = field(
        default=None,
        metadata={
            "name": "ContinueAt",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    place: List[ExchangePointsResultStructure] = field(
        default_factory=list,
        metadata={
            "name": "Place",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
