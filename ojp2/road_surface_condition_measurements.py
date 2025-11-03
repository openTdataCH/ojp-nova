from dataclasses import dataclass, field
from typing import Optional

from ojp2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class RoadSurfaceConditionMeasurements:
    de_icing_application_rate: Optional[float] = field(
        default=None,
        metadata={
            "name": "deIcingApplicationRate",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    de_icing_concentration: Optional[float] = field(
        default=None,
        metadata={
            "name": "deIcingConcentration",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    depth_of_snow: Optional[float] = field(
        default=None,
        metadata={
            "name": "depthOfSnow",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    protection_temperature: Optional[float] = field(
        default=None,
        metadata={
            "name": "protectionTemperature",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    road_surface_temperature: Optional[float] = field(
        default=None,
        metadata={
            "name": "roadSurfaceTemperature",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    water_film_thickness: Optional[float] = field(
        default=None,
        metadata={
            "name": "waterFilmThickness",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    road_surface_condition_measurements_extension: Optional[ExtensionType] = (
        field(
            default=None,
            metadata={
                "name": "roadSurfaceConditionMeasurementsExtension",
                "type": "Element",
                "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            },
        )
    )
