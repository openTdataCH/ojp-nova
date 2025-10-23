from dataclasses import dataclass, field
from typing import Optional
from ojp.verification_status_enumeration import VerificationStatusEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class Predictability:
    """
    Classification of Predictability status.
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: Optional[VerificationStatusEnumeration] = field(
        default=None
    )
