from dataclasses import dataclass, field
from typing import Optional
from ojp.environment_reason_enumeration import EnvironmentReasonEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class EnvironmentReason:
    """
    TPEG Pti18_4/TPEG Pti_22 environment event reason.
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: Optional[EnvironmentReasonEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
