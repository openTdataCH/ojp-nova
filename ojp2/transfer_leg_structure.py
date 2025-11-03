from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime, XmlDuration

from ojp2.feasibility_enumeration import FeasibilityEnumeration
from ojp2.general_attribute_structure import GeneralAttributeStructure
from ojp2.interchange_ref_structure import InterchangeRefStructure
from ojp2.international_text_structure import InternationalTextStructure
from ojp2.path_guidance_structure import PathGuidanceStructure
from ojp2.place_ref_structure import PlaceRefStructure
from ojp2.situation_ref_list import SituationRefList
from ojp2.transfer_type_enumeration import TransferTypeEnumeration

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class TransferLegStructure:
    """TRANSFER LEG or CONNECTION LEG according to TM 6.2.

    Description of a LEG which links other LEGs where a TRANSFER or
    CONNECTION between different LOCATIONs is required.

    :ivar transfer_type: TYPE that is used for this interchange between
        public services (TYPE OF TRANSFER, but also ACCESS MODE and
        PERSONAL MODE as far as a TRANSFER is concerned). In some
        constellations multiple TransferType are possible.
    :ivar leg_start: Stop/Station/Place where boarding is done (can be a
        PLACE, SCHEDULED STOP POINT or a VEHICLE MEETING POINT)
    :ivar leg_end: Stop/Station/Place to alight (can be a PLACE,
        SCHEDULED STOP POINT or a VEHICLE MEETING POINT).
    :ivar time_window_start: Time at which window begins.
    :ivar time_window_end: Time at which window ends.
    :ivar duration: Overall duration of this interchange (Transmodel: PT
        CONNECTION LEG.MEAN INTERCHANGE TIME).
    :ivar walk_duration: Walk time as part of the overall interchange
        duration (in Transmodel might be modelled as
        TRANSFER.CONNECTION.DefaultDuration).
    :ivar buffer_time: Buffer time as part of the overall interchange
        duration. Buffer times, e.g., check in/out times, sometimes are
        mandatory for using certain services as e.g., airplanes, ferries
        or highspeed trains.
    :ivar interchange_ref: Reference of an INTERCHANGE.
    :ivar extra_interchange: Whether this interchange is an addition to
        the plan. Can only be used when both participants recognise the
        same schedule version. If omitted, defaults to 'false': the
        interchange is not an addition. (since SIRI 2.1)
    :ivar interchange_cancellation: Whether this interchange is a
        cancellation of a previously announced interchange (or planned
        according to the long-term timetable. Can only be used when both
        participants recognise the same schedule version. If omitted,
        defaults to 'false': the interchange is not cancelled. (since
        SIRI 2.1)
    :ivar stay_seated: Whether the passenger can remain in VEHICLE (i.e.
        BLOCKlinking). Default is 'false': the passenger must change
        vehicles for this connection.
    :ivar guaranteed: Whether the SERVICE JOURNEY INTERCHANGE is
        guaranteed. Default is 'false'; SERVICE JOURNEY INTERCHANGE is
        not guaranteed.
    :ivar advertised: Whether the SERVICE JOURNEY INTERCHANGE is
        advertised as a connection. Default is 'false'.
    :ivar leg_description: Text that describes this interchange.
    :ivar length: Length of this interchange path.
    :ivar attribute: Note or service attribute.
    :ivar path_guidance: Structured model further describing this
        interchange, its geographic embedding and accessibility
        (LEG.PATH GUIDANCE).
    :ivar feasibility: Information about the feasibility of the
        TransferLeg, in particular with respect to the access features
        used.
    :ivar situation_full_refs: A list of references to SITUATIONs.
    :ivar extension:
    """

    transfer_type: list[TransferTypeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "TransferType",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "min_occurs": 1,
        },
    )
    leg_start: Optional[PlaceRefStructure] = field(
        default=None,
        metadata={
            "name": "LegStart",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
    leg_end: Optional[PlaceRefStructure] = field(
        default=None,
        metadata={
            "name": "LegEnd",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
    time_window_start: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TimeWindowStart",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    time_window_end: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TimeWindowEnd",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "Duration",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
    walk_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "WalkDuration",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    buffer_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "BufferTime",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    interchange_ref: Optional[InterchangeRefStructure] = field(
        default=None,
        metadata={
            "name": "InterchangeRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    extra_interchange: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ExtraInterchange",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    interchange_cancellation: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InterchangeCancellation",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    stay_seated: Optional[bool] = field(
        default=None,
        metadata={
            "name": "StaySeated",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    guaranteed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Guaranteed",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    advertised: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Advertised",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    leg_description: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "LegDescription",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    length: Optional[int] = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    attribute: list[GeneralAttributeStructure] = field(
        default_factory=list,
        metadata={
            "name": "Attribute",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    path_guidance: Optional[PathGuidanceStructure] = field(
        default=None,
        metadata={
            "name": "PathGuidance",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    feasibility: list[FeasibilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "Feasibility",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    situation_full_refs: Optional[SituationRefList] = field(
        default=None,
        metadata={
            "name": "SituationFullRefs",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    extension: Optional[object] = field(
        default=None,
        metadata={
            "name": "Extension",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
