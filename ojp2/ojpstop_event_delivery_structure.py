from dataclasses import dataclass, field
from typing import Optional

from ojp2.abstract_service_delivery_structure import (
    AbstractServiceDeliveryStructure,
)
from ojp2.data_frame_ref_structure import DataFrameRefStructure
from ojp2.extensions_2 import Extensions2
from ojp2.ojperror_structure import OjperrorStructure
from ojp2.ojpstop_event_request import OjpstopEventRequest
from ojp2.response_context_structure import ResponseContextStructure
from ojp2.stop_event_result_structure import StopEventResultStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjpstopEventDeliveryStructure(AbstractServiceDeliveryStructure):
    """
    :ivar ojpstop_event_request:
    :ivar data_frame_ref: identifier of the set of data being used by an
        information system, which allows a comparison to be made with
        the versions of data being used by overlapping systems.
    :ivar calc_time: Calculation time.
    :ivar error_condition: OJP generic problem for the whole delivery.
    :ivar stop_event_response_context: Container for data that is
        referenced multiple times.
    :ivar stop_event_result: Enclosing element for stop event data.
    :ivar extensions:
    """

    class Meta:
        name = "OJPStopEventDeliveryStructure"

    ojpstop_event_request: Optional[OjpstopEventRequest] = field(
        default=None,
        metadata={
            "name": "OJPStopEventRequest",
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
    stop_event_response_context: Optional[ResponseContextStructure] = field(
        default=None,
        metadata={
            "name": "StopEventResponseContext",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    stop_event_result: list[StopEventResultStructure] = field(
        default_factory=list,
        metadata={
            "name": "StopEventResult",
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
