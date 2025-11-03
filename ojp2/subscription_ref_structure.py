from dataclasses import dataclass

from ojp2.subscription_qualifier_structure import (
    SubscriptionQualifierStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class SubscriptionRefStructure(SubscriptionQualifierStructure):
    """
    Type for reference to a subscription.
    """
