from dataclasses import dataclass, field
from typing import Optional
from ojp.capabilities_request import CapabilitiesRequest
from ojp.capabilities_response import CapabilitiesResponse
from ojp.check_status_request import CheckStatusRequest
from ojp.check_status_response import CheckStatusResponse
from ojp.data_ready_acknowledgement import DataReadyAcknowledgement
from ojp.data_ready_notification import DataReadyNotification
from ojp.data_received_acknowledgement import DataReceivedAcknowledgement
from ojp.data_supply_request import DataSupplyRequest
from ojp.extensions_1 import Extensions1
from ojp.heartbeat_notification import HeartbeatNotification
from ojp.service_delivery import ServiceDelivery
from ojp.service_request import ServiceRequest
from ojp.subscription_request import SubscriptionRequest
from ojp.subscription_response import SubscriptionResponse
from ojp.terminate_subscription_request_1 import TerminateSubscriptionRequest1
from ojp.terminate_subscription_response import TerminateSubscriptionResponse

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class SiriSchema:
    """
    :ivar service_request:
    :ivar subscription_request:
    :ivar terminate_subscription_request:
    :ivar data_ready_notification:
    :ivar data_supply_request:
    :ivar check_status_request:
    :ivar heartbeat_notification:
    :ivar capabilities_request:
    :ivar subscription_response:
    :ivar terminate_subscription_response:
    :ivar data_ready_acknowledgement:
    :ivar service_delivery:
    :ivar data_received_acknowledgement:
    :ivar check_status_response:
    :ivar capabilities_response: Responses with the capabilities of an
        implementation. Answers a CapabilityRequest.
    :ivar extensions:
    :ivar version:
    """
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
    subscription_response: Optional[SubscriptionResponse] = field(
        default=None,
        metadata={
            "name": "SubscriptionResponse",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    terminate_subscription_response: Optional[TerminateSubscriptionResponse] = field(
        default=None,
        metadata={
            "name": "TerminateSubscriptionResponse",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    data_ready_acknowledgement: Optional[DataReadyAcknowledgement] = field(
        default=None,
        metadata={
            "name": "DataReadyAcknowledgement",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    service_delivery: Optional[ServiceDelivery] = field(
        default=None,
        metadata={
            "name": "ServiceDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    data_received_acknowledgement: Optional[DataReceivedAcknowledgement] = field(
        default=None,
        metadata={
            "name": "DataReceivedAcknowledgement",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    check_status_response: Optional[CheckStatusResponse] = field(
        default=None,
        metadata={
            "name": "CheckStatusResponse",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    capabilities_response: Optional[CapabilitiesResponse] = field(
        default=None,
        metadata={
            "name": "CapabilitiesResponse",
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
    version: str = field(
        default="2.0",
        metadata={
            "type": "Attribute",
        }
    )
