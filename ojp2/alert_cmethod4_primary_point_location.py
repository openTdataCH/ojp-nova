from dataclasses import dataclass, field
from typing import Optional

from ojp2.alert_clocation import AlertClocation
from ojp2.extension_type import ExtensionType
from ojp2.offset_distance import OffsetDistance

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class AlertCmethod4PrimaryPointLocation:
    class Meta:
        name = "AlertCMethod4PrimaryPointLocation"

    alert_clocation: Optional[AlertClocation] = field(
        default=None,
        metadata={
            "name": "alertCLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    offset_distance: Optional[OffsetDistance] = field(
        default=None,
        metadata={
            "name": "offsetDistance",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    alert_cmethod4_primary_point_location_extension: Optional[
        ExtensionType
    ] = field(
        default=None,
        metadata={
            "name": "alertCMethod4PrimaryPointLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
