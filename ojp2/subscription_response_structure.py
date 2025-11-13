from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from ojp2.extensions_2 import Extensions2
from ojp2.response_endpoint_structure import ResponseEndpointStructure
from ojp2.response_status import ResponseStatus

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class SubscriptionResponseStructure(ResponseEndpointStructure):
    """
    Type for Subscription Response.

    :ivar response_status:
    :ivar subscription_manager_address: Endpoint address of subscription
        manager if different from that of the Producer or known default.
    :ivar service_started_time: Time at which service providing the
        subscription was last started. Can be used to detect restarts.
        If absent, unknown.
    :ivar extensions:
    """

    response_status: list[ResponseStatus] = field(
        default_factory=list,
        metadata={
            "name": "ResponseStatus",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
    subscription_manager_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubscriptionManagerAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    service_started_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ServiceStartedTime",
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
