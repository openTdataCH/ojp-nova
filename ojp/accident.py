from dataclasses import dataclass, field
from typing import List, Optional
from ojp.accident_cause_enum import AccidentCauseEnum
from ojp.accident_type_enum import AccidentTypeEnum
from ojp.extension_type import ExtensionType
from ojp.group_of_people_involved import GroupOfPeopleInvolved
from ojp.group_of_vehicles_involved import GroupOfVehiclesInvolved
from ojp.traffic_element import TrafficElement
from ojp.vehicle import Vehicle

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class Accident(TrafficElement):
    accident_cause: Optional[AccidentCauseEnum] = field(
        default=None,
        metadata={
            "name": "accidentCause",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    accident_type: List[AccidentTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "accidentType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        }
    )
    total_number_of_people_involved: Optional[int] = field(
        default=None,
        metadata={
            "name": "totalNumberOfPeopleInvolved",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    total_number_of_vehicles_involved: Optional[int] = field(
        default=None,
        metadata={
            "name": "totalNumberOfVehiclesInvolved",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    vehicle_involved: List[Vehicle] = field(
        default_factory=list,
        metadata={
            "name": "vehicleInvolved",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    group_of_vehicles_involved: List[GroupOfVehiclesInvolved] = field(
        default_factory=list,
        metadata={
            "name": "groupOfVehiclesInvolved",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    group_of_people_involved: List[GroupOfPeopleInvolved] = field(
        default_factory=list,
        metadata={
            "name": "groupOfPeopleInvolved",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    accident_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "accidentExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
