from dataclasses import dataclass, field
from typing import Optional

from ojp2.abstract_service_delivery_structure import (
    AbstractServiceDeliveryStructure,
)
from ojp2.data_frame_ref_structure import DataFrameRefStructure
from ojp2.extensions_2 import Extensions2
from ojp2.ojperror_structure import OjperrorStructure
from ojp2.ojptrip_request import OjptripRequest
from ojp2.response_context_structure import ResponseContextStructure
from ojp2.trip_result_structure import TripResultStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjptripDeliveryStructure(AbstractServiceDeliveryStructure):
    """
    :ivar ojptrip_request:
    :ivar data_frame_ref: identifier of the set of data being used by an
        information system, which allows a comparison to be made with
        the versions of data being used by overlapping systems.
    :ivar calc_time: Calculation time.
    :ivar error_condition: OJP generic problem for the whole delivery.
    :ivar trip_response_context: Context to hold trip response objects
        that occur frequently.
    :ivar trip_result: The trip results found by the server.
    :ivar extensions:
    """

    class Meta:
        name = "OJPTripDeliveryStructure"

    ojptrip_request: Optional[OjptripRequest] = field(
        default=None,
        metadata={
            "name": "OJPTripRequest",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    data_frame_ref: Optional[DataFrameRefStructure] = field(
        default=None,
        metadata={
            "name": "DataFrameRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    calc_time: Optional[int] = field(
        default=None,
        metadata={
            "name": "CalcTime",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    error_condition: list[OjperrorStructure] = field(
        default_factory=list,
        metadata={
            "name": "ErrorCondition",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    trip_response_context: Optional[ResponseContextStructure] = field(
        default=None,
        metadata={
            "name": "TripResponseContext",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    trip_result: list[TripResultStructure] = field(
        default_factory=list,
        metadata={
            "name": "TripResult",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    extensions: Optional[Extensions2] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
