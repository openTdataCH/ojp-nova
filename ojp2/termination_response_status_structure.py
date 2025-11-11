from dataclasses import dataclass, field
from typing import Optional

from ojp2.capability_not_supported_error import CapabilityNotSupportedError
from ojp2.error_description_structure import ErrorDescriptionStructure
from ojp2.message_ref_structure import MessageRefStructure
from ojp2.ojperror import Ojperror
from ojp2.other_error import OtherError
from ojp2.participant_ref_structure import ParticipantRefStructure
from ojp2.response_timestamp import ResponseTimestamp
from ojp2.status import Status
from ojp2.subscription_filter_ref_structure import (
    SubscriptionFilterRefStructure,
)
from ojp2.subscription_ref_structure import SubscriptionRefStructure
from ojp2.unknown_subscriber_error import UnknownSubscriberError
from ojp2.unknown_subscription_error import UnknownSubscriptionError

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class TerminationResponseStatusStructure:
    """
    Type for Status of termination response.

    :ivar response_timestamp:
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
    """

    response_timestamp: Optional[ResponseTimestamp] = field(
        default=None,
        metadata={
            "name": "ResponseTimestamp",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
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
    status: Optional[Status] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    error_condition: Optional[
        "TerminationResponseStatusStructure.ErrorCondition"
    ] = field(
        default=None,
        metadata={
            "name": "ErrorCondition",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )

    @dataclass
    class ErrorCondition:
        """
        :ivar capability_not_supported_error:
        :ivar unknown_subscriber_error:
        :ivar unknown_subscription_error:
        :ivar ojperror:
        :ivar other_error:
        :ivar description: Text description of error.
        """

        capability_not_supported_error: Optional[
            CapabilityNotSupportedError
        ] = field(
            default=None,
            metadata={
                "name": "CapabilityNotSupportedError",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        unknown_subscriber_error: Optional[UnknownSubscriberError] = field(
            default=None,
            metadata={
                "name": "UnknownSubscriberError",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        unknown_subscription_error: Optional[UnknownSubscriptionError] = field(
            default=None,
            metadata={
                "name": "UnknownSubscriptionError",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        ojperror: Optional[Ojperror] = field(
            default=None,
            metadata={
                "name": "OJPError",
                "type": "Element",
                "namespace": "http://www.vdv.de/ojp",
            },
        )
        other_error: Optional[OtherError] = field(
            default=None,
            metadata={
                "name": "OtherError",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        description: Optional[ErrorDescriptionStructure] = field(
            default=None,
            metadata={
                "name": "Description",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
