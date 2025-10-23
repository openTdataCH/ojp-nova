from dataclasses import dataclass, field
from typing import Optional
from ojp.pushed_action_structure import PushedActionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class NotifyBySmsActionStructure(PushedActionStructure):
    """
    Type for Notify user by SMS.

    :ivar phone: MSISDN of user to which to send messages.
    :ivar premium: Whether content is flagged as subject to premium
        charge.
    """
    phone: Optional[str] = field(
        default=None,
        metadata={
            "name": "Phone",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    premium: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Premium",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
