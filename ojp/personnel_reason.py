from dataclasses import dataclass, field
from typing import Optional
from ojp.personnel_reason_enumeration import PersonnelReasonEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class PersonnelReason:
    """
    TPEG Pti18_2/TPEG Pti_20 personnel event reason.
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: Optional[PersonnelReasonEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
