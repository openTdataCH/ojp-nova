from dataclasses import dataclass, field
from typing import Optional
from ojp.extension_type import ExtensionType
from ojp.tpeg_loc01_framed_point_location_subtype_enum import TpegLoc01FramedPointLocationSubtypeEnum
from ojp.tpeg_non_junction_point import TpegNonJunctionPoint
from ojp.tpeg_point import TpegPoint
from ojp.tpeg_point_location import TpegPointLocation

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class TpegFramedPoint(TpegPointLocation):
    tpeg_framed_point_location_type: Optional[TpegLoc01FramedPointLocationSubtypeEnum] = field(
        default=None,
        metadata={
            "name": "tpegFramedPointLocationType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    framed_point: Optional[TpegNonJunctionPoint] = field(
        default=None,
        metadata={
            "name": "framedPoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    to: Optional[TpegPoint] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    from_value: Optional[TpegPoint] = field(
        default=None,
        metadata={
            "name": "from",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    tpeg_framed_point_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegFramedPointExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
