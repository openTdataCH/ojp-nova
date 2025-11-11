from dataclasses import dataclass

from ojp2.parameterised_action_structure import ParameterisedActionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ManualActionStructure(ParameterisedActionStructure):
    """
    Type for Action Publish SITUATION to Manual publication channel.
    """
