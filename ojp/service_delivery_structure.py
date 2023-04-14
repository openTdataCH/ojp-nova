from dataclasses import dataclass, field
from typing import List, Optional
from ojp.capability_not_supported_error import CapabilityNotSupportedError
from ojp.ojpexchange_points_delivery import OjpexchangePointsDelivery
from ojp.ojpfare_delivery import OjpfareDelivery
from ojp.ojplocation_information_delivery import OjplocationInformationDelivery
from ojp.ojpmulti_point_trip_delivery import OjpmultiPointTripDelivery
from ojp.ojpstop_event_delivery import OjpstopEventDelivery
from ojp.ojptrip_delivery import OjptripDelivery
from ojp.ojptrip_info_delivery import OjptripInfoDelivery
from ojp.other_error import OtherError
from ojp.producer_response_structure import ProducerResponseStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ServiceDeliveryStructure(ProducerResponseStructure):
    """
    Type for SIRI Service Delivery.

    :ivar status: Whether the complerte request could be processed
        successfully or not. Default is 'true'. If any of the individual
        requests within the delivery failed, should be set to ' false'.
    :ivar error_condition: Description of any error or warning
        conditions that appluy to the overall request. More Specific
        error conditions should be included on each request that fails.
    :ivar more_data: Whether there is a further delvery message with
        more current updates that follows this one. Default is 'false'.
    :ivar ojpmulti_point_trip_delivery:
    :ivar ojptrip_delivery:
    :ivar ojptrip_info_delivery:
    :ivar ojpstop_event_delivery:
    :ivar ojpexchange_points_delivery:
    :ivar ojplocation_information_delivery:
    :ivar ojpfare_delivery:
    :ivar srs_name: Default gml coordinate format for eny location
        elements in response; applies if Coordinates element is used to
        specify points. May be overridden on individual points.
    """
    status: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    error_condition: Optional["ServiceDeliveryStructure.ErrorCondition"] = field(
        default=None,
        metadata={
            "name": "ErrorCondition",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    more_data: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MoreData",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    ojpmulti_point_trip_delivery: List[OjpmultiPointTripDelivery] = field(
        default_factory=list,
        metadata={
            "name": "OJPMultiPointTripDelivery",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    ojptrip_delivery: List[OjptripDelivery] = field(
        default_factory=list,
        metadata={
            "name": "OJPTripDelivery",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    ojptrip_info_delivery: List[OjptripInfoDelivery] = field(
        default_factory=list,
        metadata={
            "name": "OJPTripInfoDelivery",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    ojpstop_event_delivery: List[OjpstopEventDelivery] = field(
        default_factory=list,
        metadata={
            "name": "OJPStopEventDelivery",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    ojpexchange_points_delivery: List[OjpexchangePointsDelivery] = field(
        default_factory=list,
        metadata={
            "name": "OJPExchangePointsDelivery",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    ojplocation_information_delivery: List[OjplocationInformationDelivery] = field(
        default_factory=list,
        metadata={
            "name": "OJPLocationInformationDelivery",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    ojpfare_delivery: List[OjpfareDelivery] = field(
        default_factory=list,
        metadata={
            "name": "OJPFareDelivery",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    srs_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "srsName",
            "type": "Attribute",
        }
    )

    @dataclass
    class ErrorCondition:
        """
        :ivar capability_not_supported_error:
        :ivar other_error:
        :ivar description: Text description of error.
        """
        capability_not_supported_error: Optional[CapabilityNotSupportedError] = field(
            default=None,
            metadata={
                "name": "CapabilityNotSupportedError",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            }
        )
        other_error: Optional[OtherError] = field(
            default=None,
            metadata={
                "name": "OtherError",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            }
        )
        description: Optional[str] = field(
            default=None,
            metadata={
                "name": "Description",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            }
        )
