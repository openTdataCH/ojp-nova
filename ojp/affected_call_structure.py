from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime, XmlDuration
from ojp.affected_interchange_structure import AffectedInterchangeStructure
from ojp.affected_stop_point_structure import AffectedStopPointStructure
from ojp.arrival_boarding_activity_enumeration import ArrivalBoardingActivityEnumeration
from ojp.arrival_platform_name import ArrivalPlatformName
from ojp.call_status_enumeration import CallStatusEnumeration
from ojp.departure_boarding_activity_enumeration import DepartureBoardingActivityEnumeration
from ojp.departure_platform_name import DeparturePlatformName
from ojp.location_structure import LocationStructure
from ojp.natural_language_string_structure import NaturalLanguageStringStructure
from ojp.route_point_type_enumeration import RoutePointTypeEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AffectedCallStructure(AffectedStopPointStructure):
    """
    Type for information about a CALL affected by an SITUATION.

    :ivar order: Order of visit to stop within JORUNYE PATTERN of
        journey.
    :ivar call_condition: Status of CALL TPEG 13_6
    :ivar vehicle_at_stop:
    :ivar vehicle_location_at_stop: Exact location that VEHICLE will
        take up / or has taken at STOP POINT.
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
    :ivar aimed_arrival_time: Target arrival time of VEHICLE according
        to latest working timetable.
    :ivar actual_arrival_time: Observed time of arrival of VEHICLE.
    :ivar expected_arrival_time: Estimated time of arriival of VEHICLE.
    :ivar arrival_status:
    :ivar arrival_platform_name:
    :ivar arrival_boarding_activity:
    :ivar aimed_departure_time: Target departure time of VEHICLE
        according to latest working timetable.
    :ivar actual_departure_time: Observed time of departure of VEHICLE
        from stop.
    :ivar expected_departure_time: Estimated time of departure of
        VEHICLE from stop. May include waiting time. For people on a
        VEHICLE this is the time that would normally be shown.
    :ivar departure_status:
    :ivar departure_platform_name:
    :ivar departure_boarding_activity:
    :ivar aimed_headway_interval:
    :ivar expected_headway_interval:
    :ivar affected_interchange:
    """
    order: Optional[int] = field(
        default=None,
        metadata={
            "name": "Order",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    call_condition: List[RoutePointTypeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "CallCondition",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
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
    arrival_status: Optional[CallStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "ArrivalStatus",
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
    departure_status: Optional[CallStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "DepartureStatus",
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
    affected_interchange: List[AffectedInterchangeStructure] = field(
        default_factory=list,
        metadata={
            "name": "AffectedInterchange",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
