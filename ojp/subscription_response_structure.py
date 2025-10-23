from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from ojp.extensions_1 import Extensions1
from ojp.response_endpoint_structure import ResponseEndpointStructure
from ojp.response_status import ResponseStatus

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
    response_status: List[ResponseStatus] = field(
        default_factory=list,
        metadata={
            "name": "ResponseStatus",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        }
    )
    subscription_manager_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubscriptionManagerAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    service_started_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ServiceStartedTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
