from dataclasses import dataclass, field
from typing import Optional
from ojp.verification_status_enumeration import VerificationStatusEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class VerificationStatus:
    """
    Classification of verification status TPEG Pti13 Service Condition values.
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: Optional[VerificationStatusEnumeration] = field(
        default=None
    )
