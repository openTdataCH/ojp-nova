from dataclasses import dataclass, field
from typing import Optional

from ojp2.capabilities_request import CapabilitiesRequest
from ojp2.check_status_request import CheckStatusRequest
from ojp2.data_ready_notification import DataReadyNotification
from ojp2.data_supply_request import DataSupplyRequest
from ojp2.heartbeat_notification import HeartbeatNotification
from ojp2.service_request import ServiceRequest
from ojp2.subscription_request import SubscriptionRequest
from ojp2.terminate_subscription_request import TerminateSubscriptionRequest

__NAMESPACE__ = "http://www.vdv.de/ojp"


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
        },
    )
    subscription_request: Optional[SubscriptionRequest] = field(
        default=None,
        metadata={
            "name": "SubscriptionRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    terminate_subscription_request: Optional[TerminateSubscriptionRequest] = (
        field(
            default=None,
            metadata={
                "name": "TerminateSubscriptionRequest",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
    )
    data_ready_notification: Optional[DataReadyNotification] = field(
        default=None,
        metadata={
            "name": "DataReadyNotification",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    data_supply_request: Optional[DataSupplyRequest] = field(
        default=None,
        metadata={
            "name": "DataSupplyRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    check_status_request: Optional[CheckStatusRequest] = field(
        default=None,
        metadata={
            "name": "CheckStatusRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    heartbeat_notification: Optional[HeartbeatNotification] = field(
        default=None,
        metadata={
            "name": "HeartbeatNotification",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    capabilities_request: Optional[CapabilitiesRequest] = field(
        default=None,
        metadata={
            "name": "CapabilitiesRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
