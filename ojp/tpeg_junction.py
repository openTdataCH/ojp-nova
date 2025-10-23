from dataclasses import dataclass, field
from typing import List, Optional
from ojp.extension_type import ExtensionType
from ojp.point_coordinates import PointCoordinates
from ojp.tpeg_ilc_point_descriptor import TpegIlcPointDescriptor
from ojp.tpeg_junction_point_descriptor import TpegJunctionPointDescriptor
from ojp.tpeg_other_point_descriptor import TpegOtherPointDescriptor
from ojp.tpeg_point import TpegPoint

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class TpegJunction(TpegPoint):
    point_coordinates: Optional[PointCoordinates] = field(
        default=None,
        metadata={
            "name": "pointCoordinates",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    name: Optional[TpegJunctionPointDescriptor] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    ilc: List[TpegIlcPointDescriptor] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
            "max_occurs": 3,
        }
    )
    other_name: List[TpegOtherPointDescriptor] = field(
        default_factory=list,
        metadata={
            "name": "otherName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    tpeg_junction_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegJunctionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
