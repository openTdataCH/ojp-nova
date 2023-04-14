from dataclasses import dataclass, field
from typing import Optional
from ojp.driving_condition_type_enum import DrivingConditionTypeEnum
from ojp.extension_type import ExtensionType
from ojp.traffic_element import TrafficElement

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class Conditions(TrafficElement):
    driving_condition_type: Optional[DrivingConditionTypeEnum] = field(
        default=None,
        metadata={
            "name": "drivingConditionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    conditions_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "conditionsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
