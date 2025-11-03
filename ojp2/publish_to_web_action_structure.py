from dataclasses import dataclass, field
from typing import Optional

from ojp2.parameterised_action_structure import ParameterisedActionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class PublishToWebActionStructure(ParameterisedActionStructure):
    """
    Type for Action Publish SITUATION To Web channel.

    :ivar incidents: Include in SITUATION lists on web site. Default is
        'true'.
    :ivar home_page: Include on home page on web site. Default is
        'false'.
    :ivar ticker: Include in moving ticker band. Default is 'false'.
    :ivar social_network: Include in social NETWORK indicated by this
        name. Possible value could be "twitter.com", "facebook.com",
        "vk.com" and so on. Parameters may be specified as Action data.
        (SIRI 2.1)
    """

    incidents: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Incidents",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    home_page: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HomePage",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    ticker: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ticker",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    social_network: list[str] = field(
        default_factory=list,
        metadata={
            "name": "SocialNetwork",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
