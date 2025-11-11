from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDuration

from ojp2.international_text_structure import InternationalTextStructure
from ojp2.operator_ref_structure import OperatorRefStructure
from ojp2.web_link_structure import WebLinkStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class AlternativeServiceStructure:
    """
    Service that provides shared vehicles (The Transmodel MODE OF OPERATION is
    VEHICLE SHARING; other related Transmodel concepts: ALTERNATIVE MODE LEG.SINGLE
    JOURNEY.COMMON.VEHICLE SERVICE.TRANSPORT ORGANISATION).

    :ivar operator_ref: Identifier of the operator of the sharing
        service
    :ivar name: Public name of the service.
    :ivar time_buffer_before: Typical time a user will need  to check in
        and unlock the vehicle.
    :ivar time_buffer_after: Typical time a user will need  to lock the
        vehicle and check out.
    :ivar info_url: Link to the web page providing more details on the
        service.
    :ivar restricted: This flag is set if the service can only be used
        in a restricted way. For example, a specific ACCESS MODE is
        required (e.g., dragLift) or the LINE is only made available to
        certain passenger groups (e.g., school buses, hotel shuttles).
    :ivar restriction_note: Information about the restriction.
    """

    operator_ref: Optional[OperatorRefStructure] = field(
        default=None,
        metadata={
            "name": "OperatorRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    time_buffer_before: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "TimeBufferBefore",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    time_buffer_after: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "TimeBufferAfter",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    info_url: Optional[WebLinkStructure] = field(
        default=None,
        metadata={
            "name": "InfoUrl",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    restricted: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Restricted",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    restriction_note: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "RestrictionNote",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
