from dataclasses import dataclass, field
from typing import List, Optional
from ojp.abstract_service_delivery_structure import AbstractServiceDeliveryStructure
from ojp.extensions_1 import Extensions1
from ojp.ojpstop_event_request import OjpstopEventRequest
from ojp.stop_event_response_context_structure import StopEventResponseContextStructure
from ojp.stop_event_result_structure import StopEventResultStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjpstopEventDeliveryStructure(AbstractServiceDeliveryStructure):
    """
    :ivar ojpstop_event_request:
    :ivar data_frame_ref: identifier of the set of data being used by an
        information system, which allows a comparison to be made with
        the versions of data being used by overlapping systems.
    :ivar calc_time: Calculation time.
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
    stop_event_response_context: Optional[StopEventResponseContextStructure] = field(
        default=None,
        metadata={
            "name": "StopEventResponseContext",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    stop_event_result: List[StopEventResultStructure] = field(
        default_factory=list,
        metadata={
            "name": "StopEventResult",
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
