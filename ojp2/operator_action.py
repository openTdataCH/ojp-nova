from dataclasses import dataclass, field
from typing import Optional

from ojp2.extension_type import ExtensionType
from ojp2.operator_action_origin_enum import OperatorActionOriginEnum
from ojp2.operator_action_status_enum import OperatorActionStatusEnum
from ojp2.situation_record import SituationRecord

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class OperatorAction(SituationRecord):
    action_origin: Optional[OperatorActionOriginEnum] = field(
        default=None,
        metadata={
            "name": "actionOrigin",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    operator_action_status: Optional[OperatorActionStatusEnum] = field(
        default=None,
        metadata={
            "name": "operatorActionStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    operator_action_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "operatorActionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
