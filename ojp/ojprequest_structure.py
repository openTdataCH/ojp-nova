from dataclasses import dataclass, field
from typing import Optional
from ojp.capabilities_request import CapabilitiesRequest
from ojp.check_status_request import CheckStatusRequest
from ojp.data_ready_notification import DataReadyNotification
from ojp.data_supply_request import DataSupplyRequest
from ojp.heartbeat_notification import HeartbeatNotification
from ojp.service_request import ServiceRequest
from ojp.subscription_request import SubscriptionRequest
from ojp.terminate_subscription_request_1 import TerminateSubscriptionRequest1

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class OjprequestStructure:
    """Type for OJP Request - Groups individual functional requests."""
    class Meta:
        name = "OJPRequestStructure"

    service_request: Optional[ServiceRequest] = field(
        default=None,
        metadata={
            "name": "ServiceRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    subscription_request: Optional[SubscriptionRequest] = field(
        default=None,
        metadata={
            "name": "SubscriptionRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    terminate_subscription_request: Optional[TerminateSubscriptionRequest1] = field(
        default=None,
        metadata={
            "name": "TerminateSubscriptionRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    data_ready_notification: Optional[DataReadyNotification] = field(
        default=None,
        metadata={
            "name": "DataReadyNotification",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    data_supply_request: Optional[DataSupplyRequest] = field(
        default=None,
        metadata={
            "name": "DataSupplyRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    check_status_request: Optional[CheckStatusRequest] = field(
        default=None,
        metadata={
            "name": "CheckStatusRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    heartbeat_notification: Optional[HeartbeatNotification] = field(
        default=None,
        metadata={
            "name": "HeartbeatNotification",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    capabilities_request: Optional[CapabilitiesRequest] = field(
        default=None,
        metadata={
            "name": "CapabilitiesRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
