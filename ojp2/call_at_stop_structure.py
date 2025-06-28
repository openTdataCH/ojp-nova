from dataclasses import dataclass, field
from typing import Optional

from ojp2.expected_departure_capacities import ExpectedDepartureCapacities
from ojp2.expected_departure_occupancy import ExpectedDepartureOccupancy
from ojp2.general_attribute_structure import GeneralAttributeStructure
from ojp2.international_text_structure import InternationalTextStructure
from ojp2.service_arrival_structure import ServiceArrivalStructure
from ojp2.service_departure_structure import ServiceDepartureStructure
from ojp2.situation_ref_list import SituationRefList
from ojp2.stop_point_ref import StopPointRef

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class CallAtStopStructure:
    """
    [same as CALL in SIRI] the meeting of a VEHICLE JOURNEY with a specific
    SCHEDULED STOP POINT.

    :ivar stop_point_ref: Reference to a stop point.
    :ivar stop_point_name: Name or description of stop point for use in
        passenger information.
    :ivar name_suffix: Additional description of the stop point that may
        be appended to the name if enough space is available. E.g.
        "opposite main entrance".
    :ivar planned_quay: Name of the bay where to board/alight from the
        vehicle. According to planned timetable.
    :ivar estimated_quay: Name of the bay where to board/alight from the
        vehicle. As to the latest real-time status.
    :ivar service_arrival: Arrival times of the service at this stop
        (group of attributes of TIMETABLED PASSING TIME, ESTIMATED
        PASSING TIME, OBSERVED PASSING TIME).
    :ivar service_departure: Departure times of the service at this stop
        (group of attributes of TIMETABLED PASSING TIME, ESTIMATED
        PASSING TIME, OBSERVED PASSING TIME).
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
    :ivar situation_full_refs: A list of references to SITUATIONs.
    """

    stop_point_ref: Optional[StopPointRef] = field(
        default=None,
        metadata={
            "name": "StopPointRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    stop_point_name: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "StopPointName",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
    name_suffix: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "NameSuffix",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    planned_quay: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "PlannedQuay",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    estimated_quay: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "EstimatedQuay",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
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
    situation_full_refs: Optional[SituationRefList] = field(
        default=None,
        metadata={
            "name": "SituationFullRefs",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
