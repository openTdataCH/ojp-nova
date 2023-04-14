from dataclasses import dataclass, field
from typing import Optional
from ojp.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class Temperature:
    air_temperature: Optional[float] = field(
        default=None,
        metadata={
            "name": "airTemperature",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    dew_point_temperature: Optional[float] = field(
        default=None,
        metadata={
            "name": "dewPointTemperature",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    maximum_temperature: Optional[float] = field(
        default=None,
        metadata={
            "name": "maximumTemperature",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    minimum_temperature: Optional[float] = field(
        default=None,
        metadata={
            "name": "minimumTemperature",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    temperature_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "temperatureExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
