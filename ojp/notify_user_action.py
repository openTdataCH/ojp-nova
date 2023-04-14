from dataclasses import dataclass
from ojp.notify_user_action_structure import NotifyUserActionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class NotifyUserAction(NotifyUserActionStructure):
    """Action: Publish SITUATION To User."""
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
