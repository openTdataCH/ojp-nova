from dataclasses import dataclass, field
from typing import Optional
from ojp.miscellaneous_sub_reason_enumeration import MiscellaneousSubReasonEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class MiscellaneousSubReason:
    """
    Additional refinements TPEG miscellaneous event reason.
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: Optional[MiscellaneousSubReasonEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
