from dataclasses import dataclass, field
from typing import Optional
from ojp.alert_carea import AlertCarea
from ojp.extension_type import ExtensionType
from ojp.location import Location
from ojp.tpeg_area_location import TpegAreaLocation

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class Area(Location):
    alert_carea: Optional[AlertCarea] = field(
        default=None,
        metadata={
            "name": "alertCArea",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    tpeg_area_location: Optional[TpegAreaLocation] = field(
        default=None,
        metadata={
            "name": "tpegAreaLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    area_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "areaExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
