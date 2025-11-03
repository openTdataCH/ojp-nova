from dataclasses import dataclass, field
from typing import Optional

from ojp2.parameterised_action_structure import ParameterisedActionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class PublishToTvActionStructure(ParameterisedActionStructure):
    """
    Type for Notify SITUATION to TV channel.

    :ivar ceefax: Publish to Ceefax. Default is 'true'.
    :ivar teletext: Publish to Teletext. Default is 'true'.
    """

    ceefax: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ceefax",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    teletext: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Teletext",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
