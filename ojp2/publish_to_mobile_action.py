from dataclasses import dataclass

from ojp2.publish_to_mobile_action_structure import (
    PublishToMobileActionStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class PublishToMobileAction(PublishToMobileActionStructure):
    """Action: Publish SITUATION To Mobile Applications."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
