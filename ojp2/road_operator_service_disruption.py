from dataclasses import dataclass, field
from typing import Optional

from ojp2.extension_type import ExtensionType
from ojp2.non_road_event_information import NonRoadEventInformation
from ojp2.road_operator_service_disruption_type_enum import (
    RoadOperatorServiceDisruptionTypeEnum,
)

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class RoadOperatorServiceDisruption(NonRoadEventInformation):
    road_operator_service_disruption_type: list[
        RoadOperatorServiceDisruptionTypeEnum
    ] = field(
        default_factory=list,
        metadata={
            "name": "roadOperatorServiceDisruptionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        },
    )
    road_operator_service_disruption_extension: Optional[ExtensionType] = (
        field(
            default=None,
            metadata={
                "name": "roadOperatorServiceDisruptionExtension",
                "type": "Element",
                "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            },
        )
    )
