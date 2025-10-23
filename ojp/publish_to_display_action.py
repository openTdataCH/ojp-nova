from dataclasses import dataclass
from ojp.publish_to_display_action_structure import PublishToDisplayActionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class PublishToDisplayAction(PublishToDisplayActionStructure):
    """Action: Publish SITUATION To Displays."""
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
