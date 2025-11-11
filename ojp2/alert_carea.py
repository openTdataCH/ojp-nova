from dataclasses import dataclass, field
from typing import Optional

from ojp2.alert_clocation import AlertClocation
from ojp2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class AlertCarea:
    class Meta:
        name = "AlertCArea"

    alert_clocation_country_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "alertCLocationCountryCode",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
            "max_length": 1024,
        },
    )
    alert_clocation_table_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "alertCLocationTableNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
            "max_length": 1024,
        },
    )
    alert_clocation_table_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "alertCLocationTableVersion",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
            "max_length": 1024,
        },
    )
    area_location: Optional[AlertClocation] = field(
        default=None,
        metadata={
            "name": "areaLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    alert_carea_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "alertCAreaExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
