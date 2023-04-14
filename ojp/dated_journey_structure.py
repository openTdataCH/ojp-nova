from dataclasses import dataclass, field
from typing import List, Optional
from ojp.booking_arrangements_container_structure import BookingArrangementsContainerStructure
from ojp.general_attribute_structure import GeneralAttributeStructure
from ojp.international_text_structure import InternationalTextStructure
from ojp.mode_structure import ModeStructure
from ojp.occupancy_enumeration import OccupancyEnumeration
from ojp.private_modes_enumeration import PrivateModesEnumeration
from ojp.service_via_point_structure import ServiceViaPointStructure
from ojp.situation_full_ref_2 import SituationFullRef2
from ojp.web_link_structure import WebLinkStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class DatedJourneyStructure:
    """[equivalent to  DATED VEHICLE JOURNEY in TMv6]  passenger carrying
    VEHICLE JOURNEY for one specified DAY TYPE for which the pattern of working
    is in principle defined by a SERVICE JOURNEY PATTERN.

    DatedJourney details of a service include its operating days.

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
    :ivar private_mode: [a category of MODE in TMv6] MODEs offered by
        private individuals
    :ivar organisation_ref:
    :ivar info_url: Link to web page providing more details on service.
    :ivar origin_stop_point_ref: First stop of the vehicle journey.
    :ivar origin_text: Label for first stop.
    :ivar destination_stop_point_ref: Last stop of vehicle journey.
    :ivar destination_text: Label for last stop.
    :ivar unplanned: Whether this trip is an additional one that has not
        been planned. Default is false.
    :ivar cancelled: Whether this trip is cancelled and will not be run.
        Default is false.
    :ivar deviation: Whether this trip deviates from the planned service
        pattern. Default is false.
    :ivar occupancy: [equivalent to OCCUPANCY in SIRI] passenger load
        status of a VEHICLE. If omitted, not known.
    :ivar booking_arrangements: Container with information on booking
        possibilities for this service.
    :ivar situation_full_ref:
    """
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
    journey_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "JourneyRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "max_occurs": 2,
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
    private_mode: Optional[PrivateModesEnumeration] = field(
        default=None,
        metadata={
            "name": "PrivateMode",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    organisation_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrganisationRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    info_url: Optional[WebLinkStructure] = field(
        default=None,
        metadata={
            "name": "InfoURL",
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
            "required": True,
        }
    )
    unplanned: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Unplanned",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    cancelled: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Cancelled",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    deviation: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    occupancy: Optional[OccupancyEnumeration] = field(
        default=None,
        metadata={
            "name": "Occupancy",
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
