from dataclasses import dataclass, field
from typing import Optional
from ojp.pushed_action_structure import PushedActionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class PublishToAlertsActionStructure(PushedActionStructure):
    """
    Type for Action Publish SITUATION To Alert Service.

    :ivar by_email: Send as email alert.
    :ivar by_mobile: Send as mobile alert by SMS or WAP push.
    """
    by_email: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ByEmail",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    by_mobile: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ByMobile",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
