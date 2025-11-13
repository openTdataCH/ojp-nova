from dataclasses import dataclass

from ojp2.terminate_subscription_request_structure import (
    TerminateSubscriptionRequestStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class TerminateSubscriptionRequest(TerminateSubscriptionRequestStructure):
    """Request from Subscriber to Subscription Manager to terminate a subscription.

    Answered with a TerminateSubscriptionResponse.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
