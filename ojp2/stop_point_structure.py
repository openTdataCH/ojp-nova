from dataclasses import dataclass, field
from typing import Optional

from ojp2.international_text_structure import InternationalTextStructure
from ojp2.private_code_structure import PrivateCodeStructure
from ojp2.stop_place_ref_structure_2 import StopPlaceRefStructure2
from ojp2.stop_point_ref import StopPointRef
from ojp2.topographic_place_ref import TopographicPlaceRef

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class StopPointStructure:
    """
    [an extended view of SCHEDULED STOP POINT in TMv6] a SCHEDULED STOP POINT
    extended by ACCESSIBILITY LIMITATION attributes and with identifier and name
    where passengers can board or alight from vehicles.

    :ivar stop_point_ref: Reference to a stop point.
    :ivar stop_point_name: Name or description of stop point for use in
        passenger information.
    :ivar name_suffix: Additional description of the stop point that may
        be appended to the name if enough space is available. E.g.
        "opposite main entrance".
    :ivar planned_quay: Name of the bay where to board/alight from the
        vehicle. According to planned timetable.
    :ivar estimated_quay: Name of the bay where to board/alight from the
        vehicle. As to the latest real-time status.
    :ivar private_code: Code of this stop point in
        private/foreign/proprietary coding schemes.
    :ivar parent_ref: Reference to the stop place to which this stop
        point belongs.
    :ivar topographic_place_ref:
    :ivar wheelchair_accessible: Whether this stop is accessible for
        wheelchair users.
    :ivar lighting: Whether this stop is lit.
    :ivar covered: Whether this stop offers protection from weather
        conditions like rain, snow, storm etc.
    """

    stop_point_ref: Optional[StopPointRef] = field(
        default=None,
        metadata={
            "name": "StopPointRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    stop_point_name: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "StopPointName",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
    name_suffix: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "NameSuffix",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    planned_quay: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "PlannedQuay",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    estimated_quay: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "EstimatedQuay",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    private_code: list[PrivateCodeStructure] = field(
        default_factory=list,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    parent_ref: Optional[StopPlaceRefStructure2] = field(
        default=None,
        metadata={
            "name": "ParentRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    topographic_place_ref: Optional[TopographicPlaceRef] = field(
        default=None,
        metadata={
            "name": "TopographicPlaceRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    wheelchair_accessible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "WheelchairAccessible",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    lighting: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Lighting",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    covered: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Covered",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
