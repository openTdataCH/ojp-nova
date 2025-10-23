from dataclasses import dataclass, field
from typing import Optional
from ojp.alert_cdirection import AlertCdirection
from ojp.alert_clinear import AlertClinear
from ojp.alert_clocation import AlertClocation
from ojp.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class AlertClinearByCode(AlertClinear):
    class Meta:
        name = "AlertCLinearByCode"

    alert_cdirection: Optional[AlertCdirection] = field(
        default=None,
        metadata={
            "name": "alertCDirection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    location_code_for_linear_location: Optional[AlertClocation] = field(
        default=None,
        metadata={
            "name": "locationCodeForLinearLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    alert_clinear_by_code_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "alertCLinearByCodeExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
