from dataclasses import dataclass
from ojp.notify_by_pager_action_structure import NotifyByPagerActionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class NotifyByPagerAction(NotifyByPagerActionStructure):
    """Action: Publish SITUATION To pager."""
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
