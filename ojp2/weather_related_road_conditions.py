from dataclasses import dataclass, field
from typing import Optional

from ojp2.extension_type import ExtensionType
from ojp2.road_conditions import RoadConditions
from ojp2.road_surface_condition_measurements import (
    RoadSurfaceConditionMeasurements,
)
from ojp2.weather_related_road_condition_type_enum import (
    WeatherRelatedRoadConditionTypeEnum,
)

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class WeatherRelatedRoadConditions(RoadConditions):
    weather_related_road_condition_type: list[
        WeatherRelatedRoadConditionTypeEnum
    ] = field(
        default_factory=list,
        metadata={
            "name": "weatherRelatedRoadConditionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        },
    )
    road_surface_condition_measurements: Optional[
        RoadSurfaceConditionMeasurements
    ] = field(
        default=None,
        metadata={
            "name": "roadSurfaceConditionMeasurements",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    weather_related_road_conditions_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "weatherRelatedRoadConditionsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
