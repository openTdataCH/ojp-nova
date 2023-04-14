from dataclasses import dataclass, field
from typing import List, Optional
from ojp.extension_type import ExtensionType
from ojp.point_coordinates import PointCoordinates
from ojp.tpeg_other_point_descriptor import TpegOtherPointDescriptor
from ojp.tpeg_point import TpegPoint

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class TpegNonJunctionPoint(TpegPoint):
    point_coordinates: Optional[PointCoordinates] = field(
        default=None,
        metadata={
            "name": "pointCoordinates",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    name: List[TpegOtherPointDescriptor] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        }
    )
    tpeg_non_junction_point_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegNonJunctionPointExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
