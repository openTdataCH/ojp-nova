from dataclasses import dataclass, field
from typing import Optional

from ojp2.extension_type import ExtensionType
from ojp2.tpeg_loc01_linear_location_subtype_enum import (
    TpegLoc01LinearLocationSubtypeEnum,
)
from ojp2.tpeg_loc02_direction_type_enum import TpegLoc02DirectionTypeEnum
from ojp2.tpeg_point import TpegPoint

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class TpegLinearLocation:
    tpeg_direction: Optional[TpegLoc02DirectionTypeEnum] = field(
        default=None,
        metadata={
            "name": "tpegDirection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    tpeg_linear_location_type: Optional[TpegLoc01LinearLocationSubtypeEnum] = (
        field(
            default=None,
            metadata={
                "name": "tpegLinearLocationType",
                "type": "Element",
                "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
                "required": True,
            },
        )
    )
    to: Optional[TpegPoint] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    from_value: Optional[TpegPoint] = field(
        default=None,
        metadata={
            "name": "from",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    tpeg_linear_location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegLinearLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
