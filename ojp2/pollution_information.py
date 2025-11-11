from dataclasses import dataclass, field
from typing import Optional

from ojp2.extension_type import ExtensionType
from ojp2.pollution_measurement import PollutionMeasurement
from ojp2.weather_value import WeatherValue

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class PollutionInformation(WeatherValue):
    pollution_measurement: list[PollutionMeasurement] = field(
        default_factory=list,
        metadata={
            "name": "pollutionMeasurement",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        },
    )
    pollution_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "pollutionInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
