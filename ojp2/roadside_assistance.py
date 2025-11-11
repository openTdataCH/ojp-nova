from dataclasses import dataclass, field
from typing import Optional

from ojp2.extension_type import ExtensionType
from ojp2.operator_action import OperatorAction
from ojp2.roadside_assistance_type_enum import RoadsideAssistanceTypeEnum

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
        },
    )
    roadside_assistance_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "roadsideAssistanceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
