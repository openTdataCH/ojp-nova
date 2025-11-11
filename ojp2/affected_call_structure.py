from dataclasses import dataclass, field
from typing import Optional

from ojp2.actual_arrival_time import ActualArrivalTime
from ojp2.actual_departure_time import ActualDepartureTime
from ojp2.affected_interchange_structure import AffectedInterchangeStructure
from ojp2.affected_stop_point_structure import AffectedStopPointStructure
from ojp2.aimed_arrival_time import AimedArrivalTime
from ojp2.aimed_departure_time import AimedDepartureTime
from ojp2.aimed_headway_interval import AimedHeadwayInterval
from ojp2.arrival_boarding_activity import ArrivalBoardingActivity
from ojp2.arrival_platform_name import ArrivalPlatformName
from ojp2.arrival_status import ArrivalStatus
from ojp2.departure_boarding_activity import DepartureBoardingActivity
from ojp2.departure_platform_name import DeparturePlatformName
from ojp2.departure_status import DepartureStatus
from ojp2.expected_arrival_time import ExpectedArrivalTime
from ojp2.expected_departure_time import ExpectedDepartureTime
from ojp2.expected_headway_interval import ExpectedHeadwayInterval
from ojp2.location_structure import LocationStructure
from ojp2.natural_language_string_structure import (
    NaturalLanguageStringStructure,
)
from ojp2.route_point_type_enumeration import RoutePointTypeEnumeration
from ojp2.timing_point import TimingPoint
from ojp2.vehicle_at_stop import VehicleAtStop

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AffectedCallStructure(AffectedStopPointStructure):
    """
    Type for information about a CALL affected by an SITUATION.

    :ivar order: Order of visit to stop within JOURNEY PATTERN of
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
        full journey. (since SIRI 2.0)
    :ivar destination_display: Destination to show for the VEHICLE at
        the specific stop (vehicle signage), if different to the
        Destination Name for the full journey.
    :ivar aimed_arrival_time:
    :ivar actual_arrival_time:
    :ivar expected_arrival_time:
    :ivar arrival_status:
    :ivar arrival_platform_name:
    :ivar arrival_boarding_activity:
    :ivar aimed_departure_time:
    :ivar actual_departure_time:
    :ivar expected_departure_time:
    :ivar departure_status:
    :ivar departure_platform_name:
    :ivar departure_boarding_activity:
    :ivar aimed_headway_interval:
    :ivar expected_headway_interval:
    :ivar affected_interchanges:
    """

    order: Optional[int] = field(
        default=None,
        metadata={
            "name": "Order",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    call_condition: list[RoutePointTypeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "CallCondition",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
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
    arrival_status: Optional[ArrivalStatus] = field(
        default=None,
        metadata={
            "name": "ArrivalStatus",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    arrival_platform_name: list[ArrivalPlatformName] = field(
        default_factory=list,
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
    departure_status: Optional[DepartureStatus] = field(
        default=None,
        metadata={
            "name": "DepartureStatus",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    departure_platform_name: list[DeparturePlatformName] = field(
        default_factory=list,
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
    affected_interchanges: Optional[
        "AffectedCallStructure.AffectedInterchanges"
    ] = field(
        default=None,
        metadata={
            "name": "AffectedInterchanges",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )

    @dataclass
    class AffectedInterchanges:
        affected_interchange: list[AffectedInterchangeStructure] = field(
            default_factory=list,
            metadata={
                "name": "AffectedInterchange",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
