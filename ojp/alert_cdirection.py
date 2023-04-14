from dataclasses import dataclass, field
from typing import Optional
from ojp.alert_cdirection_enum import AlertCdirectionEnum
from ojp.extension_type import ExtensionType
from ojp.multilingual_string import MultilingualString

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class AlertCdirection:
    class Meta:
        name = "AlertCDirection"

    alert_cdirection_coded: Optional[AlertCdirectionEnum] = field(
        default=None,
        metadata={
            "name": "alertCDirectionCoded",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    alert_cdirection_named: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "alertCDirectionNamed",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    alert_cdirection_sense: Optional[bool] = field(
        default=None,
        metadata={
            "name": "alertCDirectionSense",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    alert_cdirection_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "alertCDirectionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
