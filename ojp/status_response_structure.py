from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime, XmlDuration
from ojp.response_structure import ResponseStructure
from ojp.service_delivery_error_condition_structure import ServiceDeliveryErrorConditionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class StatusResponseStructure(ResponseStructure):
    """
    Type for Response Status.

    :ivar request_message_ref: Arbitrary unique reference to the request
        which gave rise to this message.
    :ivar subscriber_ref: Unique identifier of Subscriber - reference to
        a Participant.
    :ivar subscription_filter_ref: Unique identifier of Subscription
        filter to which this subscription is assigned. If there is onlya
        single filter, then can be omitted.
    :ivar subscription_ref: Reference to a service subscription: unique
        within Service and Subscriber.
    :ivar status:
    :ivar error_condition: Description of any error or warning
        condition.
    :ivar valid_until: End of data horizon of the data producer.
    :ivar shortest_possible_cycle: Minimum interval at which updates can
        be sent.
    """
    request_message_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "RequestMessageRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    subscriber_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubscriberRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    subscription_filter_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubscriptionFilterRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    subscription_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubscriptionRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    status: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    error_condition: Optional[ServiceDeliveryErrorConditionStructure] = field(
        default=None,
        metadata={
            "name": "ErrorCondition",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    valid_until: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ValidUntil",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    shortest_possible_cycle: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "ShortestPossibleCycle",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
