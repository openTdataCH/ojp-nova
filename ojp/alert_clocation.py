from dataclasses import dataclass, field
from typing import Optional
from ojp.extension_type import ExtensionType
from ojp.multilingual_string import MultilingualString

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class AlertClocation:
    class Meta:
        name = "AlertCLocation"

    alert_clocation_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "alertCLocationName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    specific_location: Optional[int] = field(
        default=None,
        metadata={
            "name": "specificLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    alert_clocation_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "alertCLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
