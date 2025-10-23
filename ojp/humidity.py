from dataclasses import dataclass, field
from typing import Optional
from ojp.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class Humidity:
    relative_humidity: Optional[float] = field(
        default=None,
        metadata={
            "name": "relativeHumidity",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    humidity_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "humidityExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
