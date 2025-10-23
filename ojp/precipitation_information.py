from dataclasses import dataclass, field
from typing import Optional
from ojp.extension_type import ExtensionType
from ojp.precipitation_detail import PrecipitationDetail
from ojp.weather_value import WeatherValue

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class PrecipitationInformation(WeatherValue):
    no_precipitation: Optional[bool] = field(
        default=None,
        metadata={
            "name": "noPrecipitation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    precipitation_detail: Optional[PrecipitationDetail] = field(
        default=None,
        metadata={
            "name": "precipitationDetail",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    precipitation_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "precipitationInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
