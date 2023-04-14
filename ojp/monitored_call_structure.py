from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime, XmlDuration
from ojp.abstract_monitored_call_structure import AbstractMonitoredCallStructure
from ojp.arrival_boarding_activity_enumeration import ArrivalBoardingActivityEnumeration
from ojp.arrival_platform_name import ArrivalPlatformName
from ojp.arrival_proximity_text import ArrivalProximityText
from ojp.call_status_enumeration import CallStatusEnumeration
from ojp.departure_boarding_activity_enumeration import DepartureBoardingActivityEnumeration
from ojp.departure_platform_name import DeparturePlatformName
from ojp.departure_proximity_text import DepartureProximityText
from ojp.extensions_1 import Extensions1
from ojp.facility_change_element import FacilityChangeElement
from ojp.facility_condition_element import FacilityConditionElement
from ojp.location_structure import LocationStructure
from ojp.natural_language_string_structure import NaturalLanguageStringStructure
from ojp.prediction_quality_structure import PredictionQualityStructure
from ojp.situation_ref import SituationRef
from ojp.stop_assignment_structure import StopAssignmentStructure

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
        full journey. (+Siri 2.0)
    :ivar destination_display: Destination to show for the VEHICLE at
        the specific stop (vehicle signage), if different to the
        Destination Name for the full journey.
    :ivar call_note: Text annotation that applies to this CALL.
    :ivar facility_condition_element: Information about a change of
        Equipment availabilti at stop or on vehicle that may affect
        access or use.
    :ivar facility_change_element:
    :ivar situation_ref:
    :ivar aimed_arrival_time: Target arrival time of VEHICLE according
        to latest working timetable.
    :ivar actual_arrival_time: Observed time of arrival of VEHICLE.
    :ivar expected_arrival_time: Estimated time of arriival of VEHICLE.
    :ivar latest_expected_arrival_time: Latest time at which a VEHICLE
        will arrive at stop. +SIRI v2.0
    :ivar arrival_status:
    :ivar arrival_proximity_text:
    :ivar arrival_platform_name: Bay or platform (QUAY) name to show
        passenger i.e. expected platform for vehicel to arrive
        at.Inheritable property. Can be omitted if the same as the
        DeparturePlatformName If there no arrival platform name separate
        from the departure platform name, the precedence is (i) any
        arrival platform on any related dated timetable element, (ii)
        any departure platform name on this estimated element; (iii) any
        departure platform name on any related dated timetable CALL.
    :ivar arrival_boarding_activity: Nature of boarding and alighting
        allowed at stop. Default is 'Alighting'.
    :ivar arrival_stop_assignment: Assignment of arrival of Scheduled
        STOP POINT to a phsyical QUAY (platform). If not given, assume
        same as for departure +SIRI v2.0.
    :ivar arrival_operator_refs: OPERATORs of of servcie up until
        arrival.. May change for departure. +SIRI v2.0.
    :ivar aimed_departure_time: Target departure time of VEHICLE
        according to latest working timetable.
    :ivar actual_departure_time: Observed time of departure of VEHICLE
        from stop.
    :ivar expected_departure_time: Estimated time of departure of
        VEHICLE from stop. May include waiting time. For people on a
        VEHICLE this is the time that would normally be shown.
    :ivar provisional_expected_departure_time: Expected departure time
        of VEHICLE without waiting time due to operational actions. For
        people at stop this would normally be shown if different from
        Expected Departure time. +SIRI v2.0.
    :ivar earliest_expected_departure_time: Earliest time at which
        VEHICLE may leave the stop. Used to secure connections.
        Passengers must be at boarding point by this time to be sure of
        catching VEHICLE. +SIRI v2.0
    :ivar expected_departure_prediction_quality: Prediction quality,
        either as approcimate level, or more quantitatyive percentile
        range of   predictions will  fall within a given range of times.
        +SIRI v2.0
    :ivar aimed_latest_passenger_access_time: Target Latest time at
        which a PASSENGER should aim to arrive at the STOP PLACE
        containing the stop. This time may be earlier than the VEHICLE
        departure times as itmay include time for processes such as
        checkin, security, etc.(As specified by CHECK CONSTRAINT DELAYs
        in the underlying data) If absent assume to be the same as
        Earliest expected departure time, +SIRI v2.0
    :ivar expected_latest_passenger_access_time: Expected Latest time at
        which a PASSENGER should aim to arrive at the STOP PLACE
        containing the stop. This time may be earlier than the VEHICLE
        departure times as it may include time for processes such as
        checkin, security, etc.(As specified by CHECK CONSTRAINT DELAYs
        in the underlying data) If absent assume to be the same as
        Earliest expected departure time, +SIRI v2.0
    :ivar departure_status:
    :ivar departure_proximity_text:
    :ivar departure_platform_name: Departure QUAY ( Bay or platform)
        name. Defaulted taken from  from planned timetable..
    :ivar departure_boarding_activity:
    :ivar departure_stop_assignment: Assignments of departure platfiorm
        for Scheduled STOP POINT to a physical QUAY. +SIRI v2.0.
    :ivar departure_operator_refs: OPERATORs of of service for
        departure and onwards.. May change from that for arrival. +SIRI
        v2.0.
    :ivar aimed_headway_interval:
    :ivar expected_headway_interval:
    :ivar distance_from_stop: Distance of VEHICLE from stop of CALL as
        measured along ROUTE track. Only shown if detail level is
        'calls' or higher. Positive value denotes distance before stop.
        +SIRI v2.0.
    :ivar number_of_stops_away: Count of stops along SERVICE PATTERN
        between current position of VEHICLE and stop of CALL as measured
        along ROUTE track. Only shown if detail level is 'calls' or
        higher. +SIRI v2.0.
    :ivar extensions:
    """
    vehicle_at_stop: Optional[bool] = field(
        default=None,
        metadata={
            "name": "VehicleAtStop",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    vehicle_location_at_stop: Optional[LocationStructure] = field(
        default=None,
        metadata={
            "name": "VehicleLocationAtStop",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    reverses_at_stop: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReversesAtStop",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    platform_traversal: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PlatformTraversal",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    signal_status: Optional[str] = field(
        default=None,
        metadata={
            "name": "SignalStatus",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    timing_point: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TimingPoint",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    boarding_stretch: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BoardingStretch",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    request_stop: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RequestStop",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    origin_display: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "OriginDisplay",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    destination_display: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "DestinationDisplay",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    call_note: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "CallNote",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    facility_condition_element: List[FacilityConditionElement] = field(
        default_factory=list,
        metadata={
            "name": "FacilityConditionElement",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    facility_change_element: Optional[FacilityChangeElement] = field(
        default=None,
        metadata={
            "name": "FacilityChangeElement",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    situation_ref: List[SituationRef] = field(
        default_factory=list,
        metadata={
            "name": "SituationRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    aimed_arrival_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "AimedArrivalTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    actual_arrival_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ActualArrivalTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    expected_arrival_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ExpectedArrivalTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    latest_expected_arrival_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "LatestExpectedArrivalTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    arrival_status: Optional[CallStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "ArrivalStatus",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    arrival_proximity_text: Optional[ArrivalProximityText] = field(
        default=None,
        metadata={
            "name": "ArrivalProximityText",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    arrival_platform_name: Optional[ArrivalPlatformName] = field(
        default=None,
        metadata={
            "name": "ArrivalPlatformName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    arrival_boarding_activity: Optional[ArrivalBoardingActivityEnumeration] = field(
        default=None,
        metadata={
            "name": "ArrivalBoardingActivity",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    arrival_stop_assignment: Optional[StopAssignmentStructure] = field(
        default=None,
        metadata={
            "name": "ArrivalStopAssignment",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    arrival_operator_refs: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ArrivalOperatorRefs",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    aimed_departure_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "AimedDepartureTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    actual_departure_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ActualDepartureTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    expected_departure_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ExpectedDepartureTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    provisional_expected_departure_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ProvisionalExpectedDepartureTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    earliest_expected_departure_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "EarliestExpectedDepartureTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    expected_departure_prediction_quality: Optional[PredictionQualityStructure] = field(
        default=None,
        metadata={
            "name": "ExpectedDeparturePredictionQuality",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    aimed_latest_passenger_access_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "AimedLatestPassengerAccessTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    expected_latest_passenger_access_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ExpectedLatestPassengerAccessTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    departure_status: Optional[CallStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "DepartureStatus",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    departure_proximity_text: Optional[DepartureProximityText] = field(
        default=None,
        metadata={
            "name": "DepartureProximityText",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    departure_platform_name: Optional[DeparturePlatformName] = field(
        default=None,
        metadata={
            "name": "DeparturePlatformName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    departure_boarding_activity: Optional[DepartureBoardingActivityEnumeration] = field(
        default=None,
        metadata={
            "name": "DepartureBoardingActivity",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    departure_stop_assignment: Optional[StopAssignmentStructure] = field(
        default=None,
        metadata={
            "name": "DepartureStopAssignment",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    departure_operator_refs: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DepartureOperatorRefs",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    aimed_headway_interval: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "AimedHeadwayInterval",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    expected_headway_interval: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "ExpectedHeadwayInterval",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    distance_from_stop: Optional[int] = field(
        default=None,
        metadata={
            "name": "DistanceFromStop",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    number_of_stops_away: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfStopsAway",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
