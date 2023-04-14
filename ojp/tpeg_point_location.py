from dataclasses import dataclass, field
from typing import Optional
from ojp.extension_type import ExtensionType
from ojp.tpeg_loc02_direction_type_enum import TpegLoc02DirectionTypeEnum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class TpegPointLocation:
    tpeg_direction: Optional[TpegLoc02DirectionTypeEnum] = field(
        default=None,
        metadata={
            "name": "tpegDirection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    tpeg_point_location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegPointLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
