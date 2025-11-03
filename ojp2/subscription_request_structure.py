from dataclasses import dataclass

from ojp2.abstract_subscription_request_structure import (
    AbstractSubscriptionRequestStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class SubscriptionRequestStructure(AbstractSubscriptionRequestStructure):
    """
    Type for SIRI Subscription Request.
    """
