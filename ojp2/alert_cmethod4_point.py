from dataclasses import dataclass, field
from typing import Optional

from ojp2.alert_cdirection import AlertCdirection
from ojp2.alert_cmethod4_primary_point_location import (
    AlertCmethod4PrimaryPointLocation,
)
from ojp2.alert_cpoint import AlertCpoint
from ojp2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class AlertCmethod4Point(AlertCpoint):
    class Meta:
        name = "AlertCMethod4Point"

    alert_cdirection: Optional[AlertCdirection] = field(
        default=None,
        metadata={
            "name": "alertCDirection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    alert_cmethod4_primary_point_location: Optional[
        AlertCmethod4PrimaryPointLocation
    ] = field(
        default=None,
        metadata={
            "name": "alertCMethod4PrimaryPointLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    alert_cmethod4_point_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "alertCMethod4PointExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
