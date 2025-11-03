from dataclasses import dataclass, field
from typing import Optional

from ojp2.extension_type import ExtensionType
from ojp2.pollutant_type_enum import PollutantTypeEnum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class PollutionMeasurement:
    pollutant_concentration: Optional[float] = field(
        default=None,
        metadata={
            "name": "pollutantConcentration",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    pollutant_type: Optional[PollutantTypeEnum] = field(
        default=None,
        metadata={
            "name": "pollutantType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    pollution_measurement_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "pollutionMeasurementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
