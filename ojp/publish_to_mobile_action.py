from dataclasses import dataclass
from ojp.publish_to_mobile_action_structure import PublishToMobileActionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class PublishToMobileAction(PublishToMobileActionStructure):
    """Action: Publish SITUATION To WAP and PDA."""
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
