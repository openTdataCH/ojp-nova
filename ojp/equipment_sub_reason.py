from dataclasses import dataclass, field
from typing import Optional
from ojp.equipment_sub_reason_enumeration import EquipmentSubReasonEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class EquipmentSubReason:
    """
    Additional refinements TPEG Equipment event reason.
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: Optional[EquipmentSubReasonEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
