from dataclasses import dataclass, field
from typing import Optional

from ojp2.car_park_configuration_enum import CarParkConfigurationEnum
from ojp2.car_park_status_enum import CarParkStatusEnum
from ojp2.extension_type import ExtensionType
from ojp2.non_road_event_information import NonRoadEventInformation

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class CarParks(NonRoadEventInformation):
    car_park_configuration: Optional[CarParkConfigurationEnum] = field(
        default=None,
        metadata={
            "name": "carParkConfiguration",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    car_park_identity: Optional[str] = field(
        default=None,
        metadata={
            "name": "carParkIdentity",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
            "max_length": 1024,
        },
    )
    car_park_occupancy: Optional[float] = field(
        default=None,
        metadata={
            "name": "carParkOccupancy",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    car_park_status: Optional[CarParkStatusEnum] = field(
        default=None,
        metadata={
            "name": "carParkStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    exit_rate: Optional[int] = field(
        default=None,
        metadata={
            "name": "exitRate",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    fill_rate: Optional[int] = field(
        default=None,
        metadata={
            "name": "fillRate",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    number_of_vacant_parking_spaces: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfVacantParkingSpaces",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    occupied_spaces: Optional[int] = field(
        default=None,
        metadata={
            "name": "occupiedSpaces",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    queuing_time: Optional[float] = field(
        default=None,
        metadata={
            "name": "queuingTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    total_capacity: Optional[int] = field(
        default=None,
        metadata={
            "name": "totalCapacity",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    car_parks_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "carParksExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
