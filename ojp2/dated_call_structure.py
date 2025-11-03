from dataclasses import dataclass, field
from typing import Optional

from ojp2.aimed_arrival_time import AimedArrivalTime
from ojp2.aimed_departure_time import AimedDepartureTime
from ojp2.aimed_headway_interval import AimedHeadwayInterval
from ojp2.aimed_latest_passenger_access_time import (
    AimedLatestPassengerAccessTime,
)
from ojp2.arrival_boarding_activity import ArrivalBoardingActivity
from ojp2.arrival_formation_assignment import ArrivalFormationAssignment
from ojp2.arrival_operator_refs import ArrivalOperatorRefs
from ojp2.arrival_platform_name import ArrivalPlatformName
from ojp2.departure_boarding_activity import DepartureBoardingActivity
from ojp2.departure_formation_assignment import DepartureFormationAssignment
from ojp2.departure_operator_refs import DepartureOperatorRefs
from ojp2.departure_platform_name import DeparturePlatformName
from ojp2.extensions_2 import Extensions2
from ojp2.from_service_journey_interchange_structure import (
    FromServiceJourneyInterchangeStructure,
)
from ojp2.natural_language_string_structure import (
    NaturalLanguageStringStructure,
)
from ojp2.order import Order
from ojp2.planned_stop_assignment_structure import (
    PlannedStopAssignmentStructure,
)
from ojp2.stop_point_name import StopPointName
from ojp2.stop_point_ref import StopPointRef
from ojp2.targeted_interchange_structure import TargetedInterchangeStructure
from ojp2.timing_point import TimingPoint
from ojp2.to_service_journey_interchange_structure import (
    ToServiceJourneyInterchangeStructure,
)
from ojp2.visit_number import VisitNumber

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class DatedCallStructure:
    """
    Type for Planned VEHICLE JOURNEY Stop (Production Timetable Service).

    :ivar stop_point_ref:
    :ivar visit_number:
    :ivar order:
    :ivar stop_point_name: Name of SCHEDULED STOP POINT.  (Unbounded
        since SIRI 2.0)
    :ivar extra_call: Whether this DATED CALL is an addition to the
        plan. Can only be used when both participants recognise the same
        schedule version. If omitted, defaults to false: the journey is
        not an addition.
    :ivar cancellation: Whether this DATED CALL is a cancellation of a
        previously announced call (or planned according to the long-term
        timetable). Can only be used when both participants recognise
        the same schedule version. If omitted, defaults to 'false': the
        journey is not cancelled.
    :ivar timing_point:
    :ivar boarding_stretch: Whether this is a Hail and Ride Stop.
        Default is 'false'.
    :ivar request_stop: Whether Vehicle stops only if requested
        explicitly by passenger. Default is 'false'.
    :ivar origin_display: Origin to show for the VEHICLE at the specific
        stop (vehicle signage), if different to the Origin Name for the
        full journey. (since SIRI 2.0)
    :ivar destination_display: Destination to show for the VEHICLE at
        the specific stop (vehicle signage), if different to the
        Destination Name for the full journey.
    :ivar call_note: Text annotation that applies to this call.
    :ivar aimed_arrival_time:
    :ivar arrival_platform_name:
    :ivar arrival_boarding_activity:
    :ivar arrival_stop_assignment: Assignment of planned arrival at
        scheduled STOP POINT to a phsyical QUAY (platform). If not
        given, assume same as for departure. (since SIRI 2.0).
    :ivar arrival_formation_assignment:
    :ivar arrival_operator_refs:
    :ivar aimed_departure_time:
    :ivar departure_platform_name:
    :ivar departure_boarding_activity:
    :ivar departure_stop_assignment:
    :ivar departure_formation_assignment:
    :ivar departure_operator_refs:
    :ivar aimed_latest_passenger_access_time:
    :ivar aimed_headway_interval:
    :ivar targeted_interchange: Information on any planned distributor
        connections (deprecated from SIRI V2.0 ... see 2 next
        attributes)
    :ivar from_service_journey_interchange: Information on any planned
        feeder connections. SIRI 2.0
    :ivar to_service_journey_interchange: Information on any planned
        distributor connections. SIRI 2.0
    :ivar extensions:
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
    visit_number: Optional[VisitNumber] = field(
        default=None,
        metadata={
            "name": "VisitNumber",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    order: Optional[Order] = field(
        default=None,
        metadata={
            "name": "Order",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_point_name: list[StopPointName] = field(
        default_factory=list,
        metadata={
            "name": "StopPointName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    extra_call: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ExtraCall",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    cancellation: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Cancellation",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    timing_point: Optional[TimingPoint] = field(
        default=None,
        metadata={
            "name": "TimingPoint",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    boarding_stretch: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BoardingStretch",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    request_stop: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RequestStop",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    origin_display: list[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "OriginDisplay",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    destination_display: list[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "DestinationDisplay",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    call_note: list[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "CallNote",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    aimed_arrival_time: Optional[AimedArrivalTime] = field(
        default=None,
        metadata={
            "name": "AimedArrivalTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    arrival_platform_name: Optional[ArrivalPlatformName] = field(
        default=None,
        metadata={
            "name": "ArrivalPlatformName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    arrival_boarding_activity: Optional[ArrivalBoardingActivity] = field(
        default=None,
        metadata={
            "name": "ArrivalBoardingActivity",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    arrival_stop_assignment: list[PlannedStopAssignmentStructure] = field(
        default_factory=list,
        metadata={
            "name": "ArrivalStopAssignment",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    arrival_formation_assignment: list[ArrivalFormationAssignment] = field(
        default_factory=list,
        metadata={
            "name": "ArrivalFormationAssignment",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    arrival_operator_refs: list[ArrivalOperatorRefs] = field(
        default_factory=list,
        metadata={
            "name": "ArrivalOperatorRefs",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    aimed_departure_time: Optional[AimedDepartureTime] = field(
        default=None,
        metadata={
            "name": "AimedDepartureTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    departure_platform_name: Optional[DeparturePlatformName] = field(
        default=None,
        metadata={
            "name": "DeparturePlatformName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    departure_boarding_activity: Optional[DepartureBoardingActivity] = field(
        default=None,
        metadata={
            "name": "DepartureBoardingActivity",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    departure_stop_assignment: list[PlannedStopAssignmentStructure] = field(
        default_factory=list,
        metadata={
            "name": "DepartureStopAssignment",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    departure_formation_assignment: list[DepartureFormationAssignment] = field(
        default_factory=list,
        metadata={
            "name": "DepartureFormationAssignment",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    departure_operator_refs: list[DepartureOperatorRefs] = field(
        default_factory=list,
        metadata={
            "name": "DepartureOperatorRefs",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    aimed_latest_passenger_access_time: Optional[
        AimedLatestPassengerAccessTime
    ] = field(
        default=None,
        metadata={
            "name": "AimedLatestPassengerAccessTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    aimed_headway_interval: Optional[AimedHeadwayInterval] = field(
        default=None,
        metadata={
            "name": "AimedHeadwayInterval",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    targeted_interchange: list[TargetedInterchangeStructure] = field(
        default_factory=list,
        metadata={
            "name": "TargetedInterchange",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    from_service_journey_interchange: list[
        FromServiceJourneyInterchangeStructure
    ] = field(
        default_factory=list,
        metadata={
            "name": "FromServiceJourneyInterchange",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    to_service_journey_interchange: list[
        ToServiceJourneyInterchangeStructure
    ] = field(
        default_factory=list,
        metadata={
            "name": "ToServiceJourneyInterchange",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
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
