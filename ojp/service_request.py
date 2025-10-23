from dataclasses import dataclass, field
from typing import List
from ojp.ojpexchange_points_request import OjpexchangePointsRequest
from ojp.ojpfare_request import OjpfareRequest
from ojp.ojplocation_information_request import OjplocationInformationRequest
from ojp.ojpmulti_point_trip_request import OjpmultiPointTripRequest
from ojp.ojpstop_event_request import OjpstopEventRequest
from ojp.ojptrip_info_request import OjptripInfoRequest
from ojp.ojptrip_request import OjptripRequest
from ojp.service_request_structure import ServiceRequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ServiceRequest(ServiceRequestStructure):
    """Request from Consumer to Producer for immediate delivery of data.

    Answered with a ServiceDelivery (or a DataReadyRequest)
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    ojpmulti_point_trip_request: List[OjpmultiPointTripRequest] = field(
        default_factory=list,
        metadata={
            "name": "OJPMultiPointTripRequest",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    ojptrip_request: List[OjptripRequest] = field(
        default_factory=list,
        metadata={
            "name": "OJPTripRequest",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    ojptrip_info_request: List[OjptripInfoRequest] = field(
        default_factory=list,
        metadata={
            "name": "OJPTripInfoRequest",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    ojpstop_event_request: List[OjpstopEventRequest] = field(
        default_factory=list,
        metadata={
            "name": "OJPStopEventRequest",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    ojpexchange_points_request: List[OjpexchangePointsRequest] = field(
        default_factory=list,
        metadata={
            "name": "OJPExchangePointsRequest",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    ojplocation_information_request: List[OjplocationInformationRequest] = field(
        default_factory=list,
        metadata={
            "name": "OJPLocationInformationRequest",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    ojpfare_request: List[OjpfareRequest] = field(
        default_factory=list,
        metadata={
            "name": "OJPFareRequest",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
