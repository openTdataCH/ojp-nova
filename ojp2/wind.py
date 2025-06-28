from dataclasses import dataclass, field
from typing import Optional

from ojp2.direction_compass_enum import DirectionCompassEnum
from ojp2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class Wind:
    maximum_wind_speed: Optional[float] = field(
        default=None,
        metadata={
            "name": "maximumWindSpeed",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    wind_direction_bearing: Optional[int] = field(
        default=None,
        metadata={
            "name": "windDirectionBearing",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    wind_direction_compass: Optional[DirectionCompassEnum] = field(
        default=None,
        metadata={
            "name": "windDirectionCompass",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    wind_measurement_height: Optional[int] = field(
        default=None,
        metadata={
            "name": "windMeasurementHeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    wind_speed: Optional[float] = field(
        default=None,
        metadata={
            "name": "windSpeed",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    wind_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "windExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
