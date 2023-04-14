from dataclasses import dataclass, field
from typing import List, Optional
from ojp.extension_type import ExtensionType
from ojp.non_weather_related_road_condition_type_enum import NonWeatherRelatedRoadConditionTypeEnum
from ojp.road_conditions import RoadConditions

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class NonWeatherRelatedRoadConditions(RoadConditions):
    non_weather_related_road_condition_type: List[NonWeatherRelatedRoadConditionTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "nonWeatherRelatedRoadConditionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        }
    )
    non_weather_related_road_conditions_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "nonWeatherRelatedRoadConditionsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
