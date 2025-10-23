from dataclasses import dataclass, field
from typing import Optional
from ojp.extension_type import ExtensionType
from ojp.visibility import Visibility
from ojp.weather_value import WeatherValue

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class VisibilityInformation(WeatherValue):
    visibility: Optional[Visibility] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    visibility_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "visibilityInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
