from dataclasses import dataclass, field
from typing import List
from ojp.error_message_structure import ErrorMessageStructure
from ojp.fare_result_structure import FareResultStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class FareResponseStructure:
    """
    Fare response structure.

    :ivar error_message: Error messages related to the request as a
        whole.
    :ivar fare_result: Fare result choice element.
    """
    error_message: List[ErrorMessageStructure] = field(
        default_factory=list,
        metadata={
            "name": "ErrorMessage",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    fare_result: List[FareResultStructure] = field(
        default_factory=list,
        metadata={
            "name": "FareResult",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
