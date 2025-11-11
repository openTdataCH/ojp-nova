from dataclasses import dataclass, field
from typing import Optional

from ojp2.alert_cpoint import AlertCpoint
from ojp2.extension_type import ExtensionType
from ojp2.network_location import NetworkLocation
from ojp2.point_by_coordinates import PointByCoordinates
from ojp2.roadside_reference_point import RoadsideReferencePoint
from ojp2.tpeg_point_location import TpegPointLocation

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class Point1(NetworkLocation):
    class Meta:
        name = "Point"

    tpeg_point_location: Optional[TpegPointLocation] = field(
        default=None,
        metadata={
            "name": "tpegPointLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    alert_cpoint: Optional[AlertCpoint] = field(
        default=None,
        metadata={
            "name": "alertCPoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    roadside_reference_point: Optional[RoadsideReferencePoint] = field(
        default=None,
        metadata={
            "name": "roadsideReferencePoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    point_by_coordinates: Optional[PointByCoordinates] = field(
        default=None,
        metadata={
            "name": "pointByCoordinates",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    point_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "pointExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
