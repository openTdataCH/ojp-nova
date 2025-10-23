from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from ojp.abstract_monitored_call_structure import AbstractMonitoredCallStructure
from ojp.extensions_1 import Extensions1

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class PreviousCallStructure(AbstractMonitoredCallStructure):
    """
    Type for CALL at previous stop.

    :ivar vehicle_at_stop:
    :ivar aimed_arrival_time: Target arrival time of VEHICLE according
        to latest working timetable.
    :ivar actual_arrival_time: Observed time of arrival of VEHICLE.
    :ivar expected_arrival_time: Estimated time of arriival of VEHICLE.
    :ivar aimed_departure_time: Target departure time of VEHICLE
        according to latest working timetable.
    :ivar actual_departure_time: Observed time of departure of VEHICLE
        from stop.
    :ivar expected_departure_time: Estimated time of departure of
        VEHICLE from stop. May include waiting time. For people on a
        VEHICLE this is the time that would normally be shown.
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
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
