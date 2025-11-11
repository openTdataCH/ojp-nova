from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from ojp2.datex_pictogram_enum import DatexPictogramEnum
from ojp2.extension_type import ExtensionType
from ojp2.multilingual_string import MultilingualString
from ojp2.operator_action import OperatorAction

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class SignSetting(OperatorAction):
    datex_pictogram: list[DatexPictogramEnum] = field(
        default_factory=list,
        metadata={
            "name": "datexPictogram",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_occurs": 2,
        },
    )
    pictogram_list: Optional[str] = field(
        default=None,
        metadata={
            "name": "pictogramList",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_length": 1024,
        },
    )
    pictogram_list_entry: list[str] = field(
        default_factory=list,
        metadata={
            "name": "pictogramListEntry",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_occurs": 2,
            "max_length": 1024,
        },
    )
    reason_for_setting: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "reasonForSetting",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    set_by: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "setBy",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    sign_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "signAddress",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_length": 1024,
        },
    )
    time_last_set: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "timeLastSet",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    sign_setting_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "signSettingExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
