from dataclasses import dataclass, field
from typing import Optional

from ojp2.environmental_obstruction_type_enum import (
    EnvironmentalObstructionTypeEnum,
)
from ojp2.extension_type import ExtensionType
from ojp2.obstruction import Obstruction

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class EnvironmentalObstruction(Obstruction):
    depth: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    environmental_obstruction_type: Optional[
        EnvironmentalObstructionTypeEnum
    ] = field(
        default=None,
        metadata={
            "name": "environmentalObstructionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    environmental_obstruction_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "environmentalObstructionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
