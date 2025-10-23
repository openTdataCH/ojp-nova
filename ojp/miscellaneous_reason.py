from dataclasses import dataclass, field
from typing import Optional
from ojp.miscellaneous_reason_enumeration import MiscellaneousReasonEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class MiscellaneousReason:
    """
    TPEG Pti18_1/TPEG Pti_19 miscellaneous event reason.
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: Optional[MiscellaneousReasonEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
