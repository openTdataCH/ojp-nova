from dataclasses import dataclass, field
from typing import Optional

from ojp2.conditions import Conditions
from ojp2.extension_type import ExtensionType
from ojp2.humidity import Humidity
from ojp2.pollution_measurement import PollutionMeasurement
from ojp2.poor_environment_type_enum import PoorEnvironmentTypeEnum
from ojp2.precipitation_detail import PrecipitationDetail
from ojp2.temperature import Temperature
from ojp2.visibility import Visibility
from ojp2.wind import Wind

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class PoorEnvironmentConditions(Conditions):
    poor_environment_type: list[PoorEnvironmentTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "poorEnvironmentType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        },
    )
    precipitation_detail: Optional[PrecipitationDetail] = field(
        default=None,
        metadata={
            "name": "precipitationDetail",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    visibility: Optional[Visibility] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    pollution_measurement: list[PollutionMeasurement] = field(
        default_factory=list,
        metadata={
            "name": "pollutionMeasurement",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    temperature: Optional[Temperature] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    wind: Optional[Wind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    humidity: Optional[Humidity] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    poor_environment_conditions_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "poorEnvironmentConditionsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
