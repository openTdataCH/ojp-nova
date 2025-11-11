from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime, XmlDuration

from ojp2.error_description_structure import ErrorDescriptionStructure
from ojp2.extensions_2 import Extensions2
from ojp2.message_qualifier_structure import MessageQualifierStructure
from ojp2.message_ref_structure import MessageRefStructure
from ojp2.ojperror import Ojperror
from ojp2.other_error import OtherError
from ojp2.participant_ref_structure import ParticipantRefStructure
from ojp2.response_structure import ResponseStructure
from ojp2.service_not_available_error import ServiceNotAvailableError
from ojp2.status import Status

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class CheckStatusResponseStructure(ResponseStructure):
    """
    Type for Service Status Check Response.

    :ivar producer_ref: Unique identifier of Producer - Participant
        reference.
    :ivar address: Endpoint Address to which acknowledgements to confirm
        delivery are to be sent.
    :ivar response_message_identifier: An arbitrary unique reference
        associated with the response which may be used to reference it.
    :ivar request_message_ref: Reference to an arbitrary unique
        identifier associated with the request which gave rise to this
        response.
    :ivar delegator_address: Address of original Consumer, i.e.
        requesting system to which delegating response is to be
        returned. (since SIRI 2.0)
    :ivar delegator_ref: Identifier of delegating system that originated
        message. (since SIRI 2.0)
    :ivar status:
    :ivar data_ready: Whether data delivery is ready to be fetched SIRI
        v 2.0
    :ivar error_condition: Description of any error or warning condition
        that applies to the status check.
    :ivar valid_until: End of data horizon of the data producer.
    :ivar shortest_possible_cycle: Minimum interval at which updates can
        be sent.
    :ivar service_started_time: Time at which current instantiation of
        service started.
    :ivar extensions:
    """

    producer_ref: Optional[ParticipantRefStructure] = field(
        default=None,
        metadata={
            "name": "ProducerRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    address: Optional[str] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    response_message_identifier: Optional[MessageQualifierStructure] = field(
        default=None,
        metadata={
            "name": "ResponseMessageIdentifier",
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
    data_ready: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DataReady",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    error_condition: Optional[
        "CheckStatusResponseStructure.ErrorCondition"
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

    @dataclass
    class ErrorCondition:
        """
        :ivar service_not_available_error:
        :ivar ojperror:
        :ivar other_error:
        :ivar description: Text description of error.
        """

        service_not_available_error: Optional[ServiceNotAvailableError] = (
            field(
                default=None,
                metadata={
                    "name": "ServiceNotAvailableError",
                    "type": "Element",
                    "namespace": "http://www.siri.org.uk/siri",
                },
            )
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
