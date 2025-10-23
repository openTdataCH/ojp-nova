from dataclasses import dataclass
from ojp.terminate_subscription_request_structure import TerminateSubscriptionRequestStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class TerminateSubscriptionRequest2(TerminateSubscriptionRequestStructure):
    """
    Request element for terminating subscriptions (from SIRI).
    """
    class Meta:
        name = "TerminateSubscriptionRequest"
        namespace = "http://www.vdv.de/ojp"
