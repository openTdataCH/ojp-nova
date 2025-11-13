from dataclasses import dataclass, field
from typing import Optional

from ojp2.expected_departure_capacities import ExpectedDepartureCapacities
from ojp2.expected_departure_occupancy import ExpectedDepartureOccupancy
from ojp2.general_attribute_structure import GeneralAttributeStructure
from ojp2.journey_ref import JourneyRef
from ojp2.operating_day_ref import OperatingDayRef
from ojp2.place_ref_structure import PlaceRefStructure
from ojp2.service_arrival_structure import ServiceArrivalStructure
from ojp2.service_departure_structure import ServiceDepartureStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class ProvisionedCallAtPlaceStructure:
    """
    Provisioned vehicle call at a general location.

    :ivar journey_ref:
    :ivar operating_day_ref:
    :ivar call_place: More general location for a call than stop points.
        May be used with flexible services or "Area Dial-A-Ride".
    :ivar service_arrival: Arrival times of the service at this stop.
    :ivar service_departure: Departure times of the service at this
        stop.
    :ivar order: Sequence number of this stop in the service pattern of
        the journey.
    :ivar request_stop: The vehicle journey calls at this stop only on
        demand.
    :ivar unplanned_stop: This stop has not been planned by the planning
        department.
    :ivar not_serviced_stop: The vehicle will not call at this stop
        despite earlier planning.
    :ivar no_boarding_at_stop: Boarding will not be allowed at this stop
        of this journey.
    :ivar no_alighting_at_stop: Alighting will not be allowed at this
        stop of this journey.
    :ivar expected_departure_occupancy: The Occupancy structure from
        SIRI can be used here. It is recommended to mainly have one
        ExpectedDepartureOccupancy for each FareClass and mainly focus
        on OccupancyLevel and OccupancyPercentage. For more details have
        a look at the SIRI documentation.
    :ivar expected_departure_capacities: The Capacity structure also
        will probably rarely be used and parsed. When used, then it
        mainly shows elements that are important for accessibility.
    :ivar attribute: Note or attribute.
    """

    journey_ref: Optional[JourneyRef] = field(
        default=None,
        metadata={
            "name": "JourneyRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    operating_day_ref: Optional[OperatingDayRef] = field(
        default=None,
        metadata={
            "name": "OperatingDayRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    call_place: Optional[PlaceRefStructure] = field(
        default=None,
        metadata={
            "name": "CallPlace",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
    service_arrival: Optional[ServiceArrivalStructure] = field(
        default=None,
        metadata={
            "name": "ServiceArrival",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    service_departure: Optional[ServiceDepartureStructure] = field(
        default=None,
        metadata={
            "name": "ServiceDeparture",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "name": "Order",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    request_stop: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RequestStop",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    unplanned_stop: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UnplannedStop",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    not_serviced_stop: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NotServicedStop",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    no_boarding_at_stop: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NoBoardingAtStop",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    no_alighting_at_stop: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NoAlightingAtStop",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    expected_departure_occupancy: list[ExpectedDepartureOccupancy] = field(
        default_factory=list,
        metadata={
            "name": "ExpectedDepartureOccupancy",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    expected_departure_capacities: list[ExpectedDepartureCapacities] = field(
        default_factory=list,
        metadata={
            "name": "ExpectedDepartureCapacities",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    attribute: list[GeneralAttributeStructure] = field(
        default_factory=list,
        metadata={
            "name": "Attribute",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
