from dataclasses import dataclass, field
from typing import Optional
from ojp.personnel_sub_reason_enumeration import PersonnelSubReasonEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class PersonnelSubReason:
    """
    Additional refinements TPEG Personnelevent reason.
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: Optional[PersonnelSubReasonEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
