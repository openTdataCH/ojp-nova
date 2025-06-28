from dataclasses import dataclass, field
from typing import Optional

from ojp2.extension_type import ExtensionType
from ojp2.precipitation_type_enum import PrecipitationTypeEnum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class PrecipitationDetail:
    deposition_depth: Optional[float] = field(
        default=None,
        metadata={
            "name": "depositionDepth",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    precipitation_intensity: Optional[float] = field(
        default=None,
        metadata={
            "name": "precipitationIntensity",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    precipitation_type: Optional[PrecipitationTypeEnum] = field(
        default=None,
        metadata={
            "name": "precipitationType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    precipitation_detail_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "precipitationDetailExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
