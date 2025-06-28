from dataclasses import dataclass, field
from typing import Optional

from ojp2.empty_type import EmptyType
from ojp2.participant_ref_structure import ParticipantRefStructure
from ojp2.subscription_qualifier_structure import (
    SubscriptionQualifierStructure,
)

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

    subscriber_ref: Optional[ParticipantRefStructure] = field(
        default=None,
        metadata={
            "name": "SubscriberRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    all: Optional[EmptyType] = field(
        default=None,
        metadata={
            "name": "All",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    subscription_ref: list[SubscriptionQualifierStructure] = field(
        default_factory=list,
        metadata={
            "name": "SubscriptionRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
