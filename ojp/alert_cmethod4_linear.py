from dataclasses import dataclass, field
from typing import Optional
from ojp.alert_cdirection import AlertCdirection
from ojp.alert_clinear import AlertClinear
from ojp.alert_cmethod4_primary_point_location import AlertCmethod4PrimaryPointLocation
from ojp.alert_cmethod4_secondary_point_location import AlertCmethod4SecondaryPointLocation
from ojp.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class AlertCmethod4Linear(AlertClinear):
    class Meta:
        name = "AlertCMethod4Linear"

    alert_cdirection: Optional[AlertCdirection] = field(
        default=None,
        metadata={
            "name": "alertCDirection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    alert_cmethod4_primary_point_location: Optional[AlertCmethod4PrimaryPointLocation] = field(
        default=None,
        metadata={
            "name": "alertCMethod4PrimaryPointLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    alert_cmethod4_secondary_point_location: Optional[AlertCmethod4SecondaryPointLocation] = field(
        default=None,
        metadata={
            "name": "alertCMethod4SecondaryPointLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    alert_cmethod4_linear_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "alertCMethod4LinearExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
