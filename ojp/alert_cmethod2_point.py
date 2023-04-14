from dataclasses import dataclass, field
from typing import Optional
from ojp.alert_cdirection import AlertCdirection
from ojp.alert_cmethod2_primary_point_location import AlertCmethod2PrimaryPointLocation
from ojp.alert_cpoint import AlertCpoint
from ojp.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class AlertCmethod2Point(AlertCpoint):
    class Meta:
        name = "AlertCMethod2Point"

    alert_cdirection: Optional[AlertCdirection] = field(
        default=None,
        metadata={
            "name": "alertCDirection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    alert_cmethod2_primary_point_location: Optional[AlertCmethod2PrimaryPointLocation] = field(
        default=None,
        metadata={
            "name": "alertCMethod2PrimaryPointLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    alert_cmethod2_point_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "alertCMethod2PointExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
