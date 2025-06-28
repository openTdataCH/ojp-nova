from dataclasses import dataclass, field
from typing import Optional

from ojp2.extension_type import ExtensionType
from ojp2.tpeg_loc04_height_type_enum import TpegLoc04HeightTypeEnum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class TpegHeight:
    height: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    height_type: Optional[TpegLoc04HeightTypeEnum] = field(
        default=None,
        metadata={
            "name": "heightType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    tpeg_height_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegHeightExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
