from dataclasses import dataclass, field
from typing import Optional
from ojp.parameterised_action_structure import ParameterisedActionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class PublishToDisplayActionStructure(ParameterisedActionStructure):
    """
    Type for Action Publish SITUATION To Web.

    :ivar on_place: Include in SITUATION lists on station displays.
    :ivar on_board: Include onboard displays.
    """
    on_place: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OnPlace",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    on_board: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OnBoard",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
