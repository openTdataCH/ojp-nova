from dataclasses import dataclass, field
from typing import Optional

from ojp2.accident_cause_enum import AccidentCauseEnum
from ojp2.accident_type_enum import AccidentTypeEnum
from ojp2.extension_type import ExtensionType
from ojp2.group_of_people_involved import GroupOfPeopleInvolved
from ojp2.group_of_vehicles_involved import GroupOfVehiclesInvolved
from ojp2.traffic_element import TrafficElement
from ojp2.vehicle import Vehicle

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class Accident(TrafficElement):
    accident_cause: Optional[AccidentCauseEnum] = field(
        default=None,
        metadata={
            "name": "accidentCause",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    accident_type: list[AccidentTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "accidentType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        },
    )
    total_number_of_people_involved: Optional[int] = field(
        default=None,
        metadata={
            "name": "totalNumberOfPeopleInvolved",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    total_number_of_vehicles_involved: Optional[int] = field(
        default=None,
        metadata={
            "name": "totalNumberOfVehiclesInvolved",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    vehicle_involved: list[Vehicle] = field(
        default_factory=list,
        metadata={
            "name": "vehicleInvolved",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    group_of_vehicles_involved: list[GroupOfVehiclesInvolved] = field(
        default_factory=list,
        metadata={
            "name": "groupOfVehiclesInvolved",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    group_of_people_involved: list[GroupOfPeopleInvolved] = field(
        default_factory=list,
        metadata={
            "name": "groupOfPeopleInvolved",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    accident_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "accidentExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
