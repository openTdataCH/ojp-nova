from dataclasses import dataclass, field
from typing import Optional
from ojp.extension_type import ExtensionType
from ojp.operator_action import OperatorAction
from ojp.roadside_assistance_type_enum import RoadsideAssistanceTypeEnum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class RoadsideAssistance(OperatorAction):
    roadside_assistance_type: Optional[RoadsideAssistanceTypeEnum] = field(
        default=None,
        metadata={
            "name": "roadsideAssistanceType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    roadside_assistance_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "roadsideAssistanceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
