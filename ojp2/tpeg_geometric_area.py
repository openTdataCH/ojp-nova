from dataclasses import dataclass, field
from typing import Optional

from ojp2.extension_type import ExtensionType
from ojp2.point_coordinates import PointCoordinates
from ojp2.tpeg_area_descriptor import TpegAreaDescriptor
from ojp2.tpeg_area_location import TpegAreaLocation

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class TpegGeometricArea(TpegAreaLocation):
    radius: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    centre_point: Optional[PointCoordinates] = field(
        default=None,
        metadata={
            "name": "centrePoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    name: Optional[TpegAreaDescriptor] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    tpeg_geometric_area_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegGeometricAreaExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
