from dataclasses import dataclass, field
from typing import Optional

from ojp2.extension_type import ExtensionType
from ojp2.non_weather_related_road_condition_type_enum import (
    NonWeatherRelatedRoadConditionTypeEnum,
)
from ojp2.road_conditions import RoadConditions

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class NonWeatherRelatedRoadConditions(RoadConditions):
    non_weather_related_road_condition_type: list[
        NonWeatherRelatedRoadConditionTypeEnum
    ] = field(
        default_factory=list,
        metadata={
            "name": "nonWeatherRelatedRoadConditionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        },
    )
    non_weather_related_road_conditions_extension: Optional[ExtensionType] = (
        field(
            default=None,
            metadata={
                "name": "nonWeatherRelatedRoadConditionsExtension",
                "type": "Element",
                "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            },
        )
    )
