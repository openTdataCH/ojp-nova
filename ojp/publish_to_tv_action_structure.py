from dataclasses import dataclass, field
from typing import Optional
from ojp.parameterised_action_structure import ParameterisedActionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class PublishToTvActionStructure(ParameterisedActionStructure):
    """
    Type for Notify SITUATION to Tv.

    :ivar ceefax: Publish to Teltext. Default is 'true'.
    :ivar teletext: Publish to Ceefax. Default is 'true'.
    """
    ceefax: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ceefax",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    teletext: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Teletext",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
