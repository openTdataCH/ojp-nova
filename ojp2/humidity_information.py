from dataclasses import dataclass, field
from typing import Optional

from ojp2.extension_type import ExtensionType
from ojp2.humidity import Humidity
from ojp2.weather_value import WeatherValue

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class HumidityInformation(WeatherValue):
    humidity: Optional[Humidity] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    humidity_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "humidityInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
