from dataclasses import dataclass, field
from typing import Optional

from ojp2.error_condition_structure import ErrorConditionStructure
from ojp2.extensions_2 import Extensions2
from ojp2.participant_ref_structure import ParticipantRefStructure
from ojp2.producer_response_structure import ProducerResponseStructure
from ojp2.subscription_filter_ref_structure import (
    SubscriptionFilterRefStructure,
)
from ojp2.subscription_ref_structure import SubscriptionRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class SubscriptionTerminatedNotificationStructure(ProducerResponseStructure):
    """
    Type for Notification to terminate a subscription or subscriptions.

    :ivar subscriber_ref: Unique identifier of Subscriber - reference to
        a Participant.
    :ivar subscription_filter_ref: Unique identifier of Subscription
        filter to which this subscription is assigned. If there is onlya
        single filter, then can be omitted.
    :ivar subscription_ref: Reference to a service subscription: unique
        within Service and Subscriber.
    :ivar errror_condition: Text description providing additional
        information about the reason for the subscription termination.
    :ivar extensions:
    """

    subscriber_ref: list[ParticipantRefStructure] = field(
        default_factory=list,
        metadata={
            "name": "SubscriberRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    subscription_filter_ref: list[SubscriptionFilterRefStructure] = field(
        default_factory=list,
        metadata={
            "name": "SubscriptionFilterRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    subscription_ref: list[SubscriptionRefStructure] = field(
        default_factory=list,
        metadata={
            "name": "SubscriptionRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
    errror_condition: Optional[ErrorConditionStructure] = field(
        default=None,
        metadata={
            "name": "ErrrorCondition",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    extensions: Optional[Extensions2] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
