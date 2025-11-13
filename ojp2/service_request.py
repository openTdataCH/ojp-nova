from dataclasses import dataclass, field

from ojp2.ojpavailability_request import OjpavailabilityRequest
from ojp2.ojpexchange_points_request import OjpexchangePointsRequest
from ojp2.ojpfare_request import OjpfareRequest
from ojp2.ojpline_information_request import OjplineInformationRequest
from ojp2.ojplocation_information_request import OjplocationInformationRequest
from ojp2.ojpmulti_point_trip_request import OjpmultiPointTripRequest
from ojp2.ojpstatus_request import OjpstatusRequest
from ojp2.ojpstop_event_request import OjpstopEventRequest
from ojp2.ojptrip_change_request import OjptripChangeRequest
from ojp2.ojptrip_info_request import OjptripInfoRequest
from ojp2.ojptrip_refine_request import OjptripRefineRequest
from ojp2.ojptrip_request import OjptripRequest
from ojp2.service_request_structure import ServiceRequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ServiceRequest(ServiceRequestStructure):
    """Request from Consumer to Producer for immediate delivery of data.

    Answered with a ServiceDelivery (or a DataReadyRequest)
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    ojptrip_change_request: list[OjptripChangeRequest] = field(
        default_factory=list,
        metadata={
            "name": "OJPTripChangeRequest",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    ojpline_information_request: list[OjplineInformationRequest] = field(
        default_factory=list,
        metadata={
            "name": "OJPLineInformationRequest",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    ojpavailability_request: list[OjpavailabilityRequest] = field(
        default_factory=list,
        metadata={
            "name": "OJPAvailabilityRequest",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    ojptrip_refine_request: list[OjptripRefineRequest] = field(
        default_factory=list,
        metadata={
            "name": "OJPTripRefineRequest",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    ojpstatus_request: list[OjpstatusRequest] = field(
        default_factory=list,
        metadata={
            "name": "OJPStatusRequest",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    ojpmulti_point_trip_request: list[OjpmultiPointTripRequest] = field(
        default_factory=list,
        metadata={
            "name": "OJPMultiPointTripRequest",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    ojptrip_request: list[OjptripRequest] = field(
        default_factory=list,
        metadata={
            "name": "OJPTripRequest",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    ojptrip_info_request: list[OjptripInfoRequest] = field(
        default_factory=list,
        metadata={
            "name": "OJPTripInfoRequest",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    ojpstop_event_request: list[OjpstopEventRequest] = field(
        default_factory=list,
        metadata={
            "name": "OJPStopEventRequest",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    ojpexchange_points_request: list[OjpexchangePointsRequest] = field(
        default_factory=list,
        metadata={
            "name": "OJPExchangePointsRequest",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    ojplocation_information_request: list[OjplocationInformationRequest] = (
        field(
            default_factory=list,
            metadata={
                "name": "OJPLocationInformationRequest",
                "type": "Element",
                "namespace": "http://www.vdv.de/ojp",
            },
        )
    )
    ojpfare_request: list[OjpfareRequest] = field(
        default_factory=list,
        metadata={
            "name": "OJPFareRequest",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
