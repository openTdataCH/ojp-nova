from dataclasses import dataclass, field
from typing import Optional

from ojp2.pushed_action_structure import PushedActionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class NotifyByPagerActionStructure(PushedActionStructure):
    """
    Type for Notify user by Pager.

    :ivar pager_group_ref: Reference to a pager group to be notified.
    :ivar pager: Pager number of pager to be notified.
    """

    pager_group_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "PagerGroupRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    pager: Optional[str] = field(
        default=None,
        metadata={
            "name": "Pager",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
