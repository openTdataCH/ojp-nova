from dataclasses import dataclass

from ojp2.manual_action_structure import ManualActionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ManualAction(ManualActionStructure):
    """Action: Publish SITUATION to Manual publication channel."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
