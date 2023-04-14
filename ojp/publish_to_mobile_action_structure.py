from dataclasses import dataclass, field
from typing import Optional
from ojp.parameterised_action_structure import ParameterisedActionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class PublishToMobileActionStructure(ParameterisedActionStructure):
    """
    Type for Action Publish SITUATION To Displays.

    :ivar incidents: Include in SITUATION lists on mobile site. Default
        is 'true'.
    :ivar home_page: Include in home page on mobile site. Default is
        'false'.
    """
    incidents: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Incidents",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    home_page: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HomePage",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
