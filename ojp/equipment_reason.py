from dataclasses import dataclass, field
from typing import Optional
from ojp.equipment_reason_enumeration import EquipmentReasonEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class EquipmentReason:
    """
    TPEG Pti18_3/TPEG Pti_21 equipment event reason.
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: Optional[EquipmentReasonEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
