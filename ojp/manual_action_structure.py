from dataclasses import dataclass
from ojp.parameterised_action_structure import ParameterisedActionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ManualActionStructure(ParameterisedActionStructure):
    """
    Type for Action Publish SITUATION Manual process.
    """
