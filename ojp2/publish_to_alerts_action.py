from dataclasses import dataclass

from ojp2.publish_to_alerts_action_structure import (
    PublishToAlertsActionStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class PublishToAlertsAction(PublishToAlertsActionStructure):
    """Action: Publish SITUATION To Alert channel."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
