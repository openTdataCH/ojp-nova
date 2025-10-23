from dataclasses import dataclass
from ojp.notify_by_sms_action_structure import NotifyBySmsActionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class NotifyBySmsAction(NotifyBySmsActionStructure):
    """Action: Publish SITUATION to an individual by SMS."""
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
