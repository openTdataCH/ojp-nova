from dataclasses import dataclass
from ojp.unknown_subscription_error_structure import UnknownSubscriptionErrorStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class UnknownSubscriptionError(UnknownSubscriptionErrorStructure):
    """Error: Subscription not found."""
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
