from dataclasses import dataclass, field
from typing import Optional

from ojp2.delay_band_enum import DelayBandEnum
from ojp2.delays_type_enum import DelaysTypeEnum
from ojp2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class Delays:
    delay_band: Optional[DelayBandEnum] = field(
        default=None,
        metadata={
            "name": "delayBand",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    delays_type: Optional[DelaysTypeEnum] = field(
        default=None,
        metadata={
            "name": "delaysType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    delay_time_value: Optional[float] = field(
        default=None,
        metadata={
            "name": "delayTimeValue",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    delays_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "delaysExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
