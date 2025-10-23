from dataclasses import dataclass, field
from typing import Optional
from ojp.request_structure import RequestStructure
from ojp.subscription_context_structure import SubscriptionContextStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AbstractSubscriptionRequestStructure(RequestStructure):
    """
    Type for COmmon Subscription Request.

    :ivar consumer_address: Address to which data is to be sent, if
        different from Address. This may also be determined from
        RequestorRef and preconfigured data.
    :ivar subscription_filter_identifier: Reference to a Subscription
        Filter with which this subscription is to be aggregated for
        purposes of notification and delivery. If absent, use the
        default filter. If present, use any existing filter with that
        identifier, if none found, create a new one. Optional SIRI
        feature.
    :ivar subscription_context: General values that apply to
        subscription. Usually set by configuration.
    """
    consumer_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConsumerAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    subscription_filter_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubscriptionFilterIdentifier",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    subscription_context: Optional[SubscriptionContextStructure] = field(
        default=None,
        metadata={
            "name": "SubscriptionContext",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
