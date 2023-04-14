from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration
from ojp.sharing_model_enumeration import SharingModelEnumeration
from ojp.web_link_structure import WebLinkStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class SharingServiceStructure:
    """
    Service that provides shared vehicles.

    :ivar operator_ref:
    :ivar name: Public name of the service.
    :ivar sharing_model: Type of the sharing scheme.
    :ivar time_buffer_before: Typical time a user will need  to check in
        and unlock the vehicle.
    :ivar time_buffer_after: Typical time a user will need  to lock the
        vehicle and check out.
    :ivar info_url: Link to web page providing more details on service.
    """
    operator_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "OperatorRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    sharing_model: Optional[SharingModelEnumeration] = field(
        default=None,
        metadata={
            "name": "SharingModel",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    time_buffer_before: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "TimeBufferBefore",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    time_buffer_after: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "TimeBufferAfter",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    info_url: Optional[WebLinkStructure] = field(
        default=None,
        metadata={
            "name": "InfoURL",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
