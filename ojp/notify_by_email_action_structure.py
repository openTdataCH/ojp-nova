from dataclasses import dataclass, field
from typing import Optional
from ojp.pushed_action_structure import PushedActionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class NotifyByEmailActionStructure(PushedActionStructure):
    """
    Type for Notify user by Email.

    :ivar email: Email address to which notice should be sent.
    """
    email: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
