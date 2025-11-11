from dataclasses import dataclass, field
from typing import Optional

from ojp2.pushed_action_structure import PushedActionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class NotifyByEmailActionStructure(PushedActionStructure):
    """
    Type for Notify a named workgroup or individual user by email.

    :ivar email: Email address to which notice should be sent.
    """

    email: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
