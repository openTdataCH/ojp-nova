from dataclasses import dataclass, field
from typing import Optional
from ojp.alert_cdirection import AlertCdirection
from ojp.alert_clinear import AlertClinear
from ojp.alert_cmethod2_primary_point_location import AlertCmethod2PrimaryPointLocation
from ojp.alert_cmethod2_secondary_point_location import AlertCmethod2SecondaryPointLocation
from ojp.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class AlertCmethod2Linear(AlertClinear):
    class Meta:
        name = "AlertCMethod2Linear"

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
    alert_cmethod2_secondary_point_location: Optional[AlertCmethod2SecondaryPointLocation] = field(
        default=None,
        metadata={
            "name": "alertCMethod2SecondaryPointLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    alert_cmethod2_linear_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "alertCMethod2LinearExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
