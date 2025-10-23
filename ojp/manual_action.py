from dataclasses import dataclass
from ojp.manual_action_structure import ManualActionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ManualAction(ManualActionStructure):
    """Action: Publish SITUATION Manually. i.e. a procedure must be carried out."""
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
