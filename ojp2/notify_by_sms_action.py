from dataclasses import dataclass

from ojp2.notify_by_sms_action_structure import NotifyBySmsActionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class NotifyBySmsAction(NotifyBySmsActionStructure):
    """Action: Publish SITUATION to an individual user by SMS."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
