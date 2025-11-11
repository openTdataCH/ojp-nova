from dataclasses import dataclass, field
from typing import Optional

from ojp2.pushed_action_structure import PushedActionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class NotifyUserActionStructure(PushedActionStructure):
    """
    Type for Notify user by other means.

    :ivar workgroup_ref: Workgroup of user to be notified.
    :ivar user_name: Name of user to be notified.
    :ivar user_ref: Reference to a user to be notified.
    """

    workgroup_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "WorkgroupRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    user_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "UserName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    user_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "UserRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
