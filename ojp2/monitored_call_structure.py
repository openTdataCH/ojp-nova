from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from ojp2.abstract_monitored_call_structure import (
    AbstractMonitoredCallStructure,
)
from ojp2.actual_arrival_time import ActualArrivalTime
from ojp2.actual_departure_time import ActualDepartureTime
from ojp2.aimed_arrival_time import AimedArrivalTime
from ojp2.aimed_departure_time import AimedDepartureTime
from ojp2.aimed_headway_interval import AimedHeadwayInterval
from ojp2.aimed_latest_passenger_access_time import (
    AimedLatestPassengerAccessTime,
)
from ojp2.arrival_boarding_activity import ArrivalBoardingActivity
from ojp2.arrival_cancellation_reason import ArrivalCancellationReason
from ojp2.arrival_formation_assignment import ArrivalFormationAssignment
from ojp2.arrival_operator_refs import ArrivalOperatorRefs
from ojp2.arrival_orientation_relative_to_quay import (
    ArrivalOrientationRelativeToQuay,
)
from ojp2.arrival_platform_name import ArrivalPlatformName
from ojp2.arrival_proximity_text import ArrivalProximityText
from ojp2.arrival_status import ArrivalStatus
from ojp2.departure_boarding_activity import DepartureBoardingActivity
from ojp2.departure_cancellation_reason import DepartureCancellationReason
from ojp2.departure_formation_assignment import DepartureFormationAssignment
from ojp2.departure_operator_refs import DepartureOperatorRefs
from ojp2.departure_orientation_relative_to_quay import (
    DepartureOrientationRelativeToQuay,
)
from ojp2.departure_platform_name import DeparturePlatformName
from ojp2.departure_proximity_text import DepartureProximityText
from ojp2.departure_status import DepartureStatus
from ojp2.expected_arrival_time import ExpectedArrivalTime
from ojp2.expected_departure_capacities import ExpectedDepartureCapacities
from ojp2.expected_departure_occupancy import ExpectedDepartureOccupancy
from ojp2.expected_departure_time import ExpectedDepartureTime
from ojp2.expected_headway_interval import ExpectedHeadwayInterval
from ojp2.expected_latest_passenger_access_time import (
    ExpectedLatestPassengerAccessTime,
)
from ojp2.extensions_2 import Extensions2
from ojp2.facility_change_element import FacilityChangeElement
from ojp2.facility_condition_element import FacilityConditionElement
from ojp2.formation_condition import FormationCondition
from ojp2.location_structure import LocationStructure
from ojp2.natural_language_string_structure import (
    NaturalLanguageStringStructure,
)
from ojp2.prediction_quality_structure import PredictionQualityStructure
from ojp2.recorded_departure_capacities import RecordedDepartureCapacities
from ojp2.recorded_departure_occupancy import RecordedDepartureOccupancy
from ojp2.situation_ref import SituationRef
from ojp2.stop_assignment_structure import StopAssignmentStructure
from ojp2.timing_point import TimingPoint
from ojp2.vehicle_at_stop import VehicleAtStop

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class MonitoredCallStructure(AbstractMonitoredCallStructure):
    """
    Type for Current CALL at stop.

    :ivar vehicle_at_stop:
    :ivar vehicle_location_at_stop: Exact location that VEHICLE will
        take up / or has taken at STOP POINT.
    :ivar reverses_at_stop: Whether VEHICLE will reverse at stop.
        Default is 'false'.
    :ivar platform_traversal: For Rail, whether this is a platform
        traversal at speed, typically triggering an announcement to
        stand back from platform. If so Boarding Activity of arrival and
        deparure should be passthrough.
    :ivar signal_status: Status of signal clearance for TRAIN. This may
        affect the prioritiisition and emphasis given to arrival or
        departure on displays - e.g. cleared trains appear first,
        flashing in green.
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
    :ivar call_note: Text annotation that applies to this CALL.
    :ivar formation_condition: Information about a change of the
        formation (e.g. TRAIN composition) or changes of vehicles within
        the formation. (since SIRI 2.1)
    :ivar facility_condition_element: Information about a change of
        Equipment availability at stop or on vehicle that may affect
        access or use.
    :ivar facility_change_element:
    :ivar situation_ref:
    :ivar aimed_arrival_time:
    :ivar actual_arrival_time:
    :ivar expected_arrival_time:
    :ivar latest_expected_arrival_time: Latest time at which a VEHICLE
        will arrive at stop. (since SIRI 2.0)
    :ivar arrival_status:
    :ivar arrival_cancellation_reason:
    :ivar arrival_proximity_text:
    :ivar arrival_platform_name:
    :ivar arrival_boarding_activity:
    :ivar arrival_stop_assignment: Assignment of planned, expected
        and/or recorded arrival at STOP POINT to a phsyical QUAY
        (platform). If not given, assume same as for departure. (since
        SIRI 2.0).
    :ivar arrival_formation_assignment:
    :ivar arrival_orientation_relative_to_quay:
    :ivar arrival_operator_refs:
    :ivar aimed_departure_time:
    :ivar actual_departure_time:
    :ivar expected_departure_time:
    :ivar provisional_expected_departure_time: Expected departure time
        of VEHICLE without waiting time due to operational actions. For
        people at stop this would normally be shown if different from
        Expected Departure time. (since SIRI 2.0).
    :ivar earliest_expected_departure_time: Earliest time at which
        VEHICLE may leave the stop. Used to secure connections.
        Passengers must be at boarding point by this time to be sure of
        catching VEHICLE. (since SIRI 2.0)
    :ivar expected_departure_prediction_quality: Prediction quality,
        either as approcimate level, or more quantitatyive percentile
        range of   predictions will  fall within a given range of times.
        (since SIRI 2.0)
    :ivar aimed_latest_passenger_access_time:
    :ivar expected_latest_passenger_access_time:
    :ivar departure_status:
    :ivar departure_cancellation_reason:
    :ivar departure_proximity_text:
    :ivar departure_platform_name:
    :ivar departure_boarding_activity:
    :ivar departure_stop_assignment:
    :ivar departure_formation_assignment:
    :ivar departure_orientation_relative_to_quay:
    :ivar expected_departure_occupancy:
    :ivar expected_departure_capacities:
    :ivar recorded_departure_occupancy:
    :ivar recorded_departure_capacities:
    :ivar departure_operator_refs:
    :ivar aimed_headway_interval:
    :ivar expected_headway_interval:
    :ivar distance_from_stop: Distance of VEHICLE from stop of CALL as
        measured along ROUTE track. Only shown if detail level is
        'calls' or higher. Positive value denotes distance before stop.
        (since SIRI 2.0).
    :ivar number_of_stops_away: Count of stops along SERVICE PATTERN
        between current position of VEHICLE and stop of CALL as measured
        along ROUTE track. Only shown if detail level is 'calls' or
        higher. (since SIRI 2.0).
    :ivar extensions:
    """

    vehicle_at_stop: Optional[VehicleAtStop] = field(
        default=None,
        metadata={
            "name": "VehicleAtStop",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_location_at_stop: Optional[LocationStructure] = field(
        default=None,
        metadata={
            "name": "VehicleLocationAtStop",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    reverses_at_stop: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReversesAtStop",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    platform_traversal: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PlatformTraversal",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    signal_status: Optional[str] = field(
        default=None,
        metadata={
            "name": "SignalStatus",
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
    formation_condition: list[FormationCondition] = field(
        default_factory=list,
        metadata={
            "name": "FormationCondition",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    facility_condition_element: list[FacilityConditionElement] = field(
        default_factory=list,
        metadata={
            "name": "FacilityConditionElement",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    facility_change_element: Optional[FacilityChangeElement] = field(
        default=None,
        metadata={
            "name": "FacilityChangeElement",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    situation_ref: list[SituationRef] = field(
        default_factory=list,
        metadata={
            "name": "SituationRef",
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
    actual_arrival_time: Optional[ActualArrivalTime] = field(
        default=None,
        metadata={
            "name": "ActualArrivalTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    expected_arrival_time: Optional[ExpectedArrivalTime] = field(
        default=None,
        metadata={
            "name": "ExpectedArrivalTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    latest_expected_arrival_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "LatestExpectedArrivalTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    arrival_status: Optional[ArrivalStatus] = field(
        default=None,
        metadata={
            "name": "ArrivalStatus",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    arrival_cancellation_reason: Optional[ArrivalCancellationReason] = field(
        default=None,
        metadata={
            "name": "ArrivalCancellationReason",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    arrival_proximity_text: Optional[ArrivalProximityText] = field(
        default=None,
        metadata={
            "name": "ArrivalProximityText",
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
    arrival_stop_assignment: list[StopAssignmentStructure] = field(
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
    arrival_orientation_relative_to_quay: list[
        ArrivalOrientationRelativeToQuay
    ] = field(
        default_factory=list,
        metadata={
            "name": "ArrivalOrientationRelativeToQuay",
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
    actual_departure_time: Optional[ActualDepartureTime] = field(
        default=None,
        metadata={
            "name": "ActualDepartureTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    expected_departure_time: Optional[ExpectedDepartureTime] = field(
        default=None,
        metadata={
            "name": "ExpectedDepartureTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    provisional_expected_departure_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ProvisionalExpectedDepartureTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    earliest_expected_departure_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "EarliestExpectedDepartureTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    expected_departure_prediction_quality: Optional[
        PredictionQualityStructure
    ] = field(
        default=None,
        metadata={
            "name": "ExpectedDeparturePredictionQuality",
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
    expected_latest_passenger_access_time: Optional[
        ExpectedLatestPassengerAccessTime
    ] = field(
        default=None,
        metadata={
            "name": "ExpectedLatestPassengerAccessTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    departure_status: Optional[DepartureStatus] = field(
        default=None,
        metadata={
            "name": "DepartureStatus",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    departure_cancellation_reason: Optional[DepartureCancellationReason] = (
        field(
            default=None,
            metadata={
                "name": "DepartureCancellationReason",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
    )
    departure_proximity_text: Optional[DepartureProximityText] = field(
        default=None,
        metadata={
            "name": "DepartureProximityText",
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
    departure_stop_assignment: list[StopAssignmentStructure] = field(
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
    departure_orientation_relative_to_quay: list[
        DepartureOrientationRelativeToQuay
    ] = field(
        default_factory=list,
        metadata={
            "name": "DepartureOrientationRelativeToQuay",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
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
    recorded_departure_occupancy: list[RecordedDepartureOccupancy] = field(
        default_factory=list,
        metadata={
            "name": "RecordedDepartureOccupancy",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    recorded_departure_capacities: list[RecordedDepartureCapacities] = field(
        default_factory=list,
        metadata={
            "name": "RecordedDepartureCapacities",
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
    aimed_headway_interval: Optional[AimedHeadwayInterval] = field(
        default=None,
        metadata={
            "name": "AimedHeadwayInterval",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    expected_headway_interval: Optional[ExpectedHeadwayInterval] = field(
        default=None,
        metadata={
            "name": "ExpectedHeadwayInterval",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    distance_from_stop: Optional[int] = field(
        default=None,
        metadata={
            "name": "DistanceFromStop",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    number_of_stops_away: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfStopsAway",
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
