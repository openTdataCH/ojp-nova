from dataclasses import dataclass, field
from typing import Optional

from ojp2.capability_not_supported_error import CapabilityNotSupportedError
from ojp2.error_description_structure import ErrorDescriptionStructure
from ojp2.ojpavailability_delivery import OjpavailabilityDelivery
from ojp2.ojperror import Ojperror
from ojp2.ojpexchange_points_delivery import OjpexchangePointsDelivery
from ojp2.ojpfare_delivery import OjpfareDelivery
from ojp2.ojpline_information_delivery import OjplineInformationDelivery
from ojp2.ojplocation_information_delivery import (
    OjplocationInformationDelivery,
)
from ojp2.ojpmulti_point_trip_delivery import OjpmultiPointTripDelivery
from ojp2.ojpstatus_delivery import OjpstatusDelivery
from ojp2.ojpstop_event_delivery import OjpstopEventDelivery
from ojp2.ojptrip_change_delivery import OjptripChangeDelivery
from ojp2.ojptrip_delivery import OjptripDelivery
from ojp2.ojptrip_info_delivery import OjptripInfoDelivery
from ojp2.ojptrip_refine_delivery import OjptripRefineDelivery
from ojp2.other_error import OtherError
from ojp2.producer_response_structure import ProducerResponseStructure

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
    :ivar ojptrip_change_delivery:
    :ivar ojpline_information_delivery:
    :ivar ojpavailability_delivery:
    :ivar ojptrip_refine_delivery:
    :ivar ojpstatus_delivery:
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
        },
    )
    error_condition: Optional["ServiceDeliveryStructure.ErrorCondition"] = (
        field(
            default=None,
            metadata={
                "name": "ErrorCondition",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
    )
    more_data: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MoreData",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    ojptrip_change_delivery: list[OjptripChangeDelivery] = field(
        default_factory=list,
        metadata={
            "name": "OJPTripChangeDelivery",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    ojpline_information_delivery: list[OjplineInformationDelivery] = field(
        default_factory=list,
        metadata={
            "name": "OJPLineInformationDelivery",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    ojpavailability_delivery: list[OjpavailabilityDelivery] = field(
        default_factory=list,
        metadata={
            "name": "OJPAvailabilityDelivery",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    ojptrip_refine_delivery: list[OjptripRefineDelivery] = field(
        default_factory=list,
        metadata={
            "name": "OJPTripRefineDelivery",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    ojpstatus_delivery: list[OjpstatusDelivery] = field(
        default_factory=list,
        metadata={
            "name": "OJPStatusDelivery",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    ojpmulti_point_trip_delivery: list[OjpmultiPointTripDelivery] = field(
        default_factory=list,
        metadata={
            "name": "OJPMultiPointTripDelivery",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    ojptrip_delivery: list[OjptripDelivery] = field(
        default_factory=list,
        metadata={
            "name": "OJPTripDelivery",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    ojptrip_info_delivery: list[OjptripInfoDelivery] = field(
        default_factory=list,
        metadata={
            "name": "OJPTripInfoDelivery",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    ojpstop_event_delivery: list[OjpstopEventDelivery] = field(
        default_factory=list,
        metadata={
            "name": "OJPStopEventDelivery",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    ojpexchange_points_delivery: list[OjpexchangePointsDelivery] = field(
        default_factory=list,
        metadata={
            "name": "OJPExchangePointsDelivery",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    ojplocation_information_delivery: list[OjplocationInformationDelivery] = (
        field(
            default_factory=list,
            metadata={
                "name": "OJPLocationInformationDelivery",
                "type": "Element",
                "namespace": "http://www.vdv.de/ojp",
            },
        )
    )
    ojpfare_delivery: list[OjpfareDelivery] = field(
        default_factory=list,
        metadata={
            "name": "OJPFareDelivery",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    srs_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "srsName",
            "type": "Attribute",
        },
    )

    @dataclass
    class ErrorCondition:
        """
        :ivar capability_not_supported_error:
        :ivar ojperror:
        :ivar other_error:
        :ivar description: Text description of error.
        """

        capability_not_supported_error: Optional[
            CapabilityNotSupportedError
        ] = field(
            default=None,
            metadata={
                "name": "CapabilityNotSupportedError",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        ojperror: Optional[Ojperror] = field(
            default=None,
            metadata={
                "name": "OJPError",
                "type": "Element",
                "namespace": "http://www.vdv.de/ojp",
            },
        )
        other_error: Optional[OtherError] = field(
            default=None,
            metadata={
                "name": "OtherError",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        description: Optional[ErrorDescriptionStructure] = field(
            default=None,
            metadata={
                "name": "Description",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
