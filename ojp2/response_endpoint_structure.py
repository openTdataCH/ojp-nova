from dataclasses import dataclass, field
from typing import Optional

from ojp2.message_ref_structure import MessageRefStructure
from ojp2.participant_ref_structure import ParticipantRefStructure
from ojp2.response_structure import ResponseStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ResponseEndpointStructure(ResponseStructure):
    """Type for Unique reference to reponse.

    May be used to reference request in subsequent interactions. Used
    for WSDL.

    :ivar address: Address for further interaction.
    :ivar responder_ref: Participant reference that identifies
        responder.
    :ivar request_message_ref: Reference to an arbitrary unique
        reference associated with the request which gave rise to this
        response.
    :ivar delegator_address: Address of original Consumer, i.e.
        requesting system to which delegating response is to be
        returned. (since SIRI 2.0)
    :ivar delegator_ref: Identifier of delegating system that originated
        message. (since SIRI 2.0)
    """

    address: Optional[str] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    responder_ref: Optional[ParticipantRefStructure] = field(
        default=None,
        metadata={
            "name": "ResponderRef",
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
