from dataclasses import dataclass, field
from typing import List, Optional
from ojp.empty_type import EmptyType

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class TerminateSubscriptionRequestBodyStructure:
    """Type for Body of Terminate Subscription Request content.

    Used in WSDL.

    :ivar subscriber_ref: Participant identifier of Subscriber.
        Subscription ref will be unique within this.
    :ivar all: Terminate all subscriptions for the requestor.
    :ivar subscription_ref: Terminate the subscription identfiied by the
        reference.
    """
    subscriber_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubscriberRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    all: Optional[EmptyType] = field(
        default=None,
        metadata={
            "name": "All",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    subscription_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SubscriptionRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
