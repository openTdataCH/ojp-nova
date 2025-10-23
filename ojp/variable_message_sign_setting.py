from dataclasses import dataclass, field
from typing import List, Optional
from ojp.extension_type import ExtensionType
from ojp.multilingual_string import MultilingualString
from ojp.sign_setting import SignSetting
from ojp.vms_fault_enum import VmsFaultEnum
from ojp.vms_type_enum import VmsTypeEnum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class VariableMessageSignSetting(SignSetting):
    number_of_characters: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfCharacters",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    number_of_rows: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfRows",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    vms_fault: List[VmsFaultEnum] = field(
        default_factory=list,
        metadata={
            "name": "vmsFault",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    vms_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "vmsIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_length": 1024,
        }
    )
    vms_legend: List[MultilingualString] = field(
        default_factory=list,
        metadata={
            "name": "vmsLegend",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    vms_type: Optional[VmsTypeEnum] = field(
        default=None,
        metadata={
            "name": "vmsType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    variable_message_sign_setting_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "variableMessageSignSettingExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
