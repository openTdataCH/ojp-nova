from dataclasses import dataclass, field
from typing import Optional
from ojp.extension_type import ExtensionType
from ojp.tpeg_height import TpegHeight
from ojp.tpeg_loc01_area_location_subtype_enum import TpegLoc01AreaLocationSubtypeEnum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class TpegAreaLocation:
    tpeg_area_location_type: Optional[TpegLoc01AreaLocationSubtypeEnum] = field(
        default=None,
        metadata={
            "name": "tpegAreaLocationType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    tpeg_height: Optional[TpegHeight] = field(
        default=None,
        metadata={
            "name": "tpegHeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    tpeg_area_location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegAreaLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
