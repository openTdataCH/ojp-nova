from dataclasses import dataclass, field
from typing import Optional

from ojp2.basic_data_value import BasicDataValue
from ojp2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class WeatherValue(BasicDataValue):
    weather_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "weatherValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
