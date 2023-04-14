from dataclasses import dataclass, field
from typing import Optional
from ojp.abstract_service_delivery_structure import AbstractServiceDeliveryStructure
from ojp.extensions_1 import Extensions1
from ojp.ojptrip_info_request import OjptripInfoRequest
from ojp.trip_info_response_context_structure import TripInfoResponseContextStructure
from ojp.trip_info_result_structure import TripInfoResultStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjptripInfoDeliveryStructure(AbstractServiceDeliveryStructure):
    """
    :ivar ojptrip_info_request:
    :ivar data_frame_ref: identifier of the set of data being used by an
        information system, which allows a comparison to be made with
        the versions of data being used by overlapping systems.
    :ivar calc_time: Calculation time.
    :ivar trip_info_response_context: Response context.
    :ivar trip_info_result: Result structure.
    :ivar extensions:
    """
    class Meta:
        name = "OJPTripInfoDeliveryStructure"

    ojptrip_info_request: Optional[OjptripInfoRequest] = field(
        default=None,
        metadata={
            "name": "OJPTripInfoRequest",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
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
    trip_info_response_context: Optional[TripInfoResponseContextStructure] = field(
        default=None,
        metadata={
            "name": "TripInfoResponseContext",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    trip_info_result: Optional[TripInfoResultStructure] = field(
        default=None,
        metadata={
            "name": "TripInfoResult",
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
