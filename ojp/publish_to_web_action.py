from dataclasses import dataclass
from ojp.publish_to_web_action_structure import PublishToWebActionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class PublishToWebAction(PublishToWebActionStructure):
    """Action: Publish SITUATION To Web."""
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
