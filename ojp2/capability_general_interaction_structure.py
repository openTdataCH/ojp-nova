from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class CapabilityGeneralInteractionStructure:
    """
    Type for Common Request Policy capabilities.

    :ivar interaction: Interaction capabilities.
    :ivar delivery: Delivery capabilities.
    :ivar multipart_despatch: Whether the service supports multiple part
        despatch with MoreData flag. Default is 'true'.
    :ivar multiple_subscriber_filter: Whether the service supports
        multiple Subscriber Filters. Default is ' false'.
    :ivar has_confirm_delivery: Whether the service supports Delivery
        confirm.
    :ivar has_heartbeat: Whether the service has a heartbeat message.
        Default is 'false'.
    :ivar visit_numberis_order: Whether VisitNumber can be used as a
        strict order number within JOURNEY PATTERN. Default is 'false'.
    """

    interaction: Optional[
        "CapabilityGeneralInteractionStructure.Interaction"
    ] = field(
        default=None,
        metadata={
            "name": "Interaction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    delivery: Optional["CapabilityGeneralInteractionStructure.Delivery"] = (
        field(
            default=None,
            metadata={
                "name": "Delivery",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "required": True,
            },
        )
    )
    multipart_despatch: bool = field(
        default=True,
        metadata={
            "name": "MultipartDespatch",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    multiple_subscriber_filter: bool = field(
        default=False,
        metadata={
            "name": "MultipleSubscriberFilter",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    has_confirm_delivery: bool = field(
        default=False,
        metadata={
            "name": "HasConfirmDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    has_heartbeat: bool = field(
        default=False,
        metadata={
            "name": "HasHeartbeat",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    visit_numberis_order: Optional[bool] = field(
        default=None,
        metadata={
            "name": "VisitNumberisOrder",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )

    @dataclass
    class Interaction:
        """
        :ivar request_response: Whether the service supports Request
            Response Interaction. Default is 'true'.
        :ivar publish_subscribe: Whether the service supports Publish
            Subscribe Interaction. Default is 'true'.
        """

        request_response: bool = field(
            default=True,
            metadata={
                "name": "RequestResponse",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "required": True,
            },
        )
        publish_subscribe: bool = field(
            default=True,
            metadata={
                "name": "PublishSubscribe",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "required": True,
            },
        )

    @dataclass
    class Delivery:
        """
        :ivar direct_delivery: Whether the service supports Direct
            delivery.
        :ivar fetched_delivery: Whether the service supports Fetched
            delivery (VDV Style)
        """

        direct_delivery: Optional[bool] = field(
            default=None,
            metadata={
                "name": "DirectDelivery",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "required": True,
            },
        )
        fetched_delivery: Optional[bool] = field(
            default=None,
            metadata={
                "name": "FetchedDelivery",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "required": True,
            },
        )
