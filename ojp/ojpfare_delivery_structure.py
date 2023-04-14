from dataclasses import dataclass, field
from typing import List, Optional
from ojp.abstract_service_delivery_structure import AbstractServiceDeliveryStructure
from ojp.extensions_1 import Extensions1
from ojp.fare_result_structure import FareResultStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjpfareDeliveryStructure(AbstractServiceDeliveryStructure):
    """
    :ivar data_frame_ref: identifier of the set of data being used by an
        information system, which allows a comparison to be made with
        the versions of data being used by overlapping systems.
    :ivar calc_time: Calculation time.
    :ivar fare_result: Fare result choice element.
    :ivar extensions:
    """
    class Meta:
        name = "OJPFareDeliveryStructure"

    data_frame_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DataFrameRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    calc_time: Optional[int] = field(
        default=None,
        metadata={
            "name": "CalcTime",
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
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
