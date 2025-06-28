from dataclasses import dataclass, field
from typing import Optional

from ojp2.extension_type import ExtensionType
from ojp2.temperature import Temperature
from ojp2.weather_value import WeatherValue

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class TemperatureInformation(WeatherValue):
    temperature: Optional[Temperature] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    temperature_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "temperatureInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
