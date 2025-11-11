from dataclasses import dataclass, field
from typing import Optional

from ojp2.authenticated_request_structure import AuthenticatedRequestStructure
from ojp2.empty_type import EmptyType
from ojp2.extensions_2 import Extensions2
from ojp2.message_qualifier_structure import MessageQualifierStructure
from ojp2.participant_ref_structure import ParticipantRefStructure
from ojp2.requestor_ref import RequestorRef
from ojp2.subscription_qualifier_structure import (
    SubscriptionQualifierStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class TerminateSubscriptionRequestStructure(AuthenticatedRequestStructure):
    """
    Type for request to terminate a subscription or subscriptions.

    :ivar address: Address to which response is to be sent. This may
        also be determined from RequestorRef and preconfigured data.
    :ivar requestor_ref:
    :ivar message_identifier: Arbitrary unique identifier that can be
        used to reference this message in subsequent interactions.
    :ivar delegator_address: Address of original Consumer, i.e.
        requesting system to which delegating response is to be
        returned. (since SIRI 2.0)
    :ivar delegator_ref: Identifier of delegating system that originated
        message. (since SIRI 2.0)
    :ivar subscriber_ref: Participant identifier of Subscriber.
        Subscription ref will be unique within this.
    :ivar all: Terminate all subscriptions for the requestor.
    :ivar subscription_ref: Terminate the subscription identfiied by the
        reference.
    :ivar extensions:
    """

    address: Optional[str] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    requestor_ref: Optional[RequestorRef] = field(
        default=None,
        metadata={
            "name": "RequestorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    message_identifier: Optional[MessageQualifierStructure] = field(
        default=None,
        metadata={
            "name": "MessageIdentifier",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    delegator_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "DelegatorAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    delegator_ref: Optional[ParticipantRefStructure] = field(
        default=None,
        metadata={
            "name": "DelegatorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
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
    extensions: Optional[Extensions2] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
