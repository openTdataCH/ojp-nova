from dataclasses import dataclass

from ojp2.notify_user_action_structure import NotifyUserActionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class NotifyUserAction(NotifyUserActionStructure):
    """Action: Publish SITUATION To User by other means."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
