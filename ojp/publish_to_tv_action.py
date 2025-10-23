from dataclasses import dataclass
from ojp.publish_to_tv_action_structure import PublishToTvActionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class PublishToTvAction(PublishToTvActionStructure):
    """Action: Publish SITUATION To TvService."""
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
