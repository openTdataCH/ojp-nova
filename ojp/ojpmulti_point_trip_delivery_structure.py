from dataclasses import dataclass, field
from typing import List, Optional
from ojp.abstract_service_delivery_structure import AbstractServiceDeliveryStructure
from ojp.extensions_1 import Extensions1
from ojp.multi_point_trip_result_structure import MultiPointTripResultStructure
from ojp.ojpmulti_point_trip_request import OjpmultiPointTripRequest
from ojp.trip_response_context_structure import TripResponseContextStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjpmultiPointTripDeliveryStructure(AbstractServiceDeliveryStructure):
    """
    :ivar ojpmulti_point_trip_request:
    :ivar data_frame_ref: identifier of the set of data being used by an
        information system, which allows a comparison to be made with
        the versions of data being used by overlapping systems.
    :ivar calc_time: Calculation time.
    :ivar trip_response_context: Context to hold trip response objects
        that occur frequently.
    :ivar multi_point_trip_result: The trip results found by the server.
    :ivar extensions:
    """
    class Meta:
        name = "OJPMultiPointTripDeliveryStructure"

    ojpmulti_point_trip_request: Optional[OjpmultiPointTripRequest] = field(
        default=None,
        metadata={
            "name": "OJPMultiPointTripRequest",
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
    trip_response_context: Optional[TripResponseContextStructure] = field(
        default=None,
        metadata={
            "name": "TripResponseContext",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    multi_point_trip_result: List[MultiPointTripResultStructure] = field(
        default_factory=list,
        metadata={
            "name": "MultiPointTripResult",
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
