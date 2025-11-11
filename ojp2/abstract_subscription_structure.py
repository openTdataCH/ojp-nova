from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from ojp2.participant_ref_structure import ParticipantRefStructure
from ojp2.subscription_qualifier_structure import (
    SubscriptionQualifierStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AbstractSubscriptionStructure:
    """
    Type for SIRI Service subscriptions.

    :ivar subscriber_ref: Participant identifier of Subscriber. Normally
        this will be given by context, i.e. be the same as on the
        Subscription Request.
    :ivar subscription_identifier: Identifier to be given to
        Subscription.
    :ivar initial_termination_time: Requested end time for subscription.
    :ivar subscription_renewal: By using this element, the subscriber
        asks the data provider for an extension of the
        InitialTerminationTime of the subscription. If
        SubscriptionRenewal is omitted, this request is to be treated as
        a re-subscription and therefore all data corresponding to the
        SubscriptionRequest must be sent in the initial response (or a
        portion of the data if MoreData is set to 'true'). (since SIRI
        2.1)
    """

    subscriber_ref: Optional[ParticipantRefStructure] = field(
        default=None,
        metadata={
            "name": "SubscriberRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    subscription_identifier: Optional[SubscriptionQualifierStructure] = field(
        default=None,
        metadata={
            "name": "SubscriptionIdentifier",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    initial_termination_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "InitialTerminationTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    subscription_renewal: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SubscriptionRenewal",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
