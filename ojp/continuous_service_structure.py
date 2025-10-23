from dataclasses import dataclass, field
from typing import List, Optional
from ojp.booking_arrangements_container_structure import BookingArrangementsContainerStructure
from ojp.continuous_modes_enumeration import ContinuousModesEnumeration
from ojp.general_attribute_structure import GeneralAttributeStructure
from ojp.individual_modes_enumeration import IndividualModesEnumeration
from ojp.international_text_structure import InternationalTextStructure
from ojp.mode_structure import ModeStructure
from ojp.service_via_point_structure import ServiceViaPointStructure
from ojp.sharing_service_structure import SharingServiceStructure
from ojp.situation_full_ref_2 import SituationFullRef2

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class ContinuousServiceStructure:
    """
    [a special form of SERVICE JOURNEY in TMv6] a vehicle movement on a continuous,
    non-timetabled service.

    :ivar continuous_mode: Continuous transport options.
    :ivar individual_mode: Individual transport options.
    :ivar operating_day_ref:
    :ivar vehicle_ref:
    :ivar journey_ref:
    :ivar line_ref: Line Reference.
    :ivar direction_ref: Direction Reference.
    :ivar mode: [a specialisation of MODE in TMv6] an extended range of
        VEHICLE MODEs, aggregating them with some SUBMODEs
    :ivar published_line_name: Line name or service description as known
        to the public, f.e. "512", "S8" or "Circle Line".
    :ivar operator_ref:
    :ivar route_description: Descriptive text for a route, f.e. "Airport
        via City Centre"
    :ivar via: Via points of the service that may help identify the
        vehicle to the public.
    :ivar attribute: Note or service attribute.
    :ivar sharing_service:
    :ivar origin_stop_point_ref: First stop of the vehicle journey.
    :ivar origin_text: Label for first stop.
    :ivar destination_stop_point_ref: Last stop of vehicle journey.
    :ivar destination_text: Label for last stop.
    :ivar booking_arrangements: Container with information on booking
        possibilities for this service.
    :ivar situation_full_ref:
    """
    continuous_mode: Optional[ContinuousModesEnumeration] = field(
        default=None,
        metadata={
            "name": "ContinuousMode",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    individual_mode: Optional[IndividualModesEnumeration] = field(
        default=None,
        metadata={
            "name": "IndividualMode",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    operating_day_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "OperatingDayRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    vehicle_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "VehicleRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    journey_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "JourneyRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    line_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "LineRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    direction_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DirectionRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    mode: Optional[ModeStructure] = field(
        default=None,
        metadata={
            "name": "Mode",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    published_line_name: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "PublishedLineName",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    operator_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "OperatorRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    route_description: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "RouteDescription",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    via: List[ServiceViaPointStructure] = field(
        default_factory=list,
        metadata={
            "name": "Via",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    attribute: List[GeneralAttributeStructure] = field(
        default_factory=list,
        metadata={
            "name": "Attribute",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    sharing_service: Optional[SharingServiceStructure] = field(
        default=None,
        metadata={
            "name": "SharingService",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    origin_stop_point_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "OriginStopPointRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    origin_text: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "OriginText",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    destination_stop_point_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DestinationStopPointRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    destination_text: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "DestinationText",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    booking_arrangements: Optional[BookingArrangementsContainerStructure] = field(
        default=None,
        metadata={
            "name": "BookingArrangements",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    situation_full_ref: List[SituationFullRef2] = field(
        default_factory=list,
        metadata={
            "name": "SituationFullRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
