from dataclasses import dataclass, field
from typing import Optional
from ojp.abstract_subscription_request_structure import AbstractSubscriptionRequestStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class AbstractOjpsubscriptionRequestStructure(AbstractSubscriptionRequestStructure):
    """
    Basic structure common for all OJP subscription requests.

    :ivar data_frame_ref: identifier of the set of data being used by an
        information system, which allows a comparison to be made with
        the versions of data being used by overlapping systems.
    :ivar language: Preferred language in which to return  text  values.
    :ivar signature: Authorisation signature (data for transmission of
        message signatures (public key cryptography), used to prove
        Message Integrity).
    :ivar certificate_id: form of identification that can be used as a
        Message Integrity Property (public key cryptography)
    :ivar extension:
    """
    class Meta:
        name = "AbstractOJPSubscriptionRequestStructure"

    data_frame_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DataFrameRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    signature: Optional[str] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    certificate_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CertificateId",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    extension: Optional[object] = field(
        default=None,
        metadata={
            "name": "Extension",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
