from dataclasses import dataclass, field
from typing import List, Optional
from ojp.extension_type import ExtensionType
from ojp.matrix_fault_enum import MatrixFaultEnum
from ojp.sign_setting import SignSetting

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class MatrixSignSetting(SignSetting):
    aspect_displayed: Optional[str] = field(
        default=None,
        metadata={
            "name": "aspectDisplayed",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
            "max_length": 1024,
        }
    )
    matrix_fault: List[MatrixFaultEnum] = field(
        default_factory=list,
        metadata={
            "name": "matrixFault",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    matrix_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "matrixIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
            "max_length": 1024,
        }
    )
    matrix_sign_setting_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "matrixSignSettingExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
