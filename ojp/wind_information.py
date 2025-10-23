from dataclasses import dataclass, field
from typing import Optional
from ojp.extension_type import ExtensionType
from ojp.weather_value import WeatherValue
from ojp.wind import Wind

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class WindInformation(WeatherValue):
    wind: Optional[Wind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    wind_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "windInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
