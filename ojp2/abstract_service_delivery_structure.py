from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime, XmlDuration

from ojp2.message_ref_structure import MessageRefStructure
from ojp2.participant_ref_structure import ParticipantRefStructure
from ojp2.response_structure import ResponseStructure
from ojp2.service_delivery_error_condition_structure import (
    ServiceDeliveryErrorConditionStructure,
)
from ojp2.status import Status
from ojp2.subscription_filter_ref_structure import (
    SubscriptionFilterRefStructure,
)
from ojp2.subscription_ref_structure import SubscriptionRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AbstractServiceDeliveryStructure(ResponseStructure):
    """
    Type for Common elementd for a SIRI service delivery of the Form xxxDelivery.

    :ivar request_message_ref: Arbitrary unique reference to the request
        which gave rise to this message.
    :ivar subscriber_ref: Unique identifier of Subscriber - reference to
        a Participant.
    :ivar subscription_filter_ref: Unique identifier of Subscription
        filter to which this subscription is assigned. If there is onlya
        single filter, then can be omitted.
    :ivar subscription_ref: Reference to a service subscription: unique
        within Service and Subscriber.
    :ivar delegator_address: Address of original Consumer, i.e.
        requesting system to which delegating response is to be
        returned. (since SIRI 2.0)
    :ivar delegator_ref: Identifier of delegating system that originated
        message. (since SIRI 2.0)
    :ivar status:
    :ivar siri_org_uk_siri_error_condition: Description of any error or
        warning condition.
    :ivar valid_until: End of data horizon of the data producer.
    :ivar shortest_possible_cycle: Minimum interval at which updates can
        be sent.
    :ivar default_language: Default language for text elements.
    """

    request_message_ref: Optional[MessageRefStructure] = field(
        default=None,
        metadata={
            "name": "RequestMessageRef",
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
    subscription_filter_ref: Optional[SubscriptionFilterRefStructure] = field(
        default=None,
        metadata={
            "name": "SubscriptionFilterRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    subscription_ref: Optional[SubscriptionRefStructure] = field(
        default=None,
        metadata={
            "name": "SubscriptionRef",
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
    status: Optional[Status] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    siri_org_uk_siri_error_condition: Optional[
        ServiceDeliveryErrorConditionStructure
    ] = field(
        default=None,
        metadata={
            "name": "ErrorCondition",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    valid_until: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ValidUntil",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    shortest_possible_cycle: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "ShortestPossibleCycle",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    default_language: Optional[str] = field(
        default=None,
        metadata={
            "name": "DefaultLanguage",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
