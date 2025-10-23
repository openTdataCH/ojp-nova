from dataclasses import dataclass, field
from typing import Optional
from ojp.action_status_enumeration import ActionStatusEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class SimpleActionStructure:
    """
    Type for list of SITUATIONs.

    :ivar action_status: Processing Status of action at time of
        SITUATION publication.
    """
    action_status: Optional[ActionStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "ActionStatus",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
