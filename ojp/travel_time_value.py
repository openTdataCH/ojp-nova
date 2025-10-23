from dataclasses import dataclass, field
from typing import List, Optional
from ojp.basic_data_value import BasicDataValue
from ojp.extension_type import ExtensionType
from ojp.travel_time_trend_type_enum import TravelTimeTrendTypeEnum
from ojp.travel_time_type_enum import TravelTimeTypeEnum
from ojp.vehicle_type_enum import VehicleTypeEnum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class TravelTimeValue(BasicDataValue):
    travel_time: Optional[float] = field(
        default=None,
        metadata={
            "name": "travelTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    travel_time_trend_type: Optional[TravelTimeTrendTypeEnum] = field(
        default=None,
        metadata={
            "name": "travelTimeTrendType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    travel_time_type: Optional[TravelTimeTypeEnum] = field(
        default=None,
        metadata={
            "name": "travelTimeType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    free_flow_speed: Optional[float] = field(
        default=None,
        metadata={
            "name": "freeFlowSpeed",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    free_flow_travel_time: Optional[float] = field(
        default=None,
        metadata={
            "name": "freeFlowTravelTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    normally_expected_travel_time: Optional[float] = field(
        default=None,
        metadata={
            "name": "normallyExpectedTravelTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    vehicle_type: List[VehicleTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "vehicleType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    travel_time_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "travelTimeValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
