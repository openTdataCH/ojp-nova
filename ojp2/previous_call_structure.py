from dataclasses import dataclass, field
from typing import Optional

from ojp2.abstract_monitored_call_structure import (
    AbstractMonitoredCallStructure,
)
from ojp2.actual_arrival_time import ActualArrivalTime
from ojp2.actual_departure_time import ActualDepartureTime
from ojp2.aimed_arrival_time import AimedArrivalTime
from ojp2.aimed_departure_time import AimedDepartureTime
from ojp2.expected_arrival_time import ExpectedArrivalTime
from ojp2.expected_departure_time import ExpectedDepartureTime
from ojp2.extensions_2 import Extensions2
from ojp2.recorded_departure_capacities import RecordedDepartureCapacities
from ojp2.recorded_departure_occupancy import RecordedDepartureOccupancy
from ojp2.vehicle_at_stop import VehicleAtStop

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class PreviousCallStructure(AbstractMonitoredCallStructure):
    """
    Type for CALL at previous stop.
    """

    vehicle_at_stop: Optional[VehicleAtStop] = field(
        default=None,
        metadata={
            "name": "VehicleAtStop",
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
    extensions: Optional[Extensions2] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
