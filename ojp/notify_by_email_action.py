from dataclasses import dataclass
from ojp.notify_by_email_action_structure import NotifyByEmailActionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class NotifyByEmailAction(NotifyByEmailActionStructure):
    """Action: Publish SITUATION to a named workgroup or individual by email."""
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
