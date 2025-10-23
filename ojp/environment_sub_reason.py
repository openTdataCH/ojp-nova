from dataclasses import dataclass, field
from typing import Optional
from ojp.environment_sub_reason_enumeration import EnvironmentSubReasonEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class EnvironmentSubReason:
    """
    Additional refinements TPEG Environmentevent reason.
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: Optional[EnvironmentSubReasonEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
