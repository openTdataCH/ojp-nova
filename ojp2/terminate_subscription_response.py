from dataclasses import dataclass

from ojp2.terminate_subscription_response_structure import (
    TerminateSubscriptionResponseStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class TerminateSubscriptionResponse(TerminateSubscriptionResponseStructure):
    """Request from Subscriber to Subscription Manager to terminate a subscription.

    Answered with a TerminateSubscriptionResponse.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
