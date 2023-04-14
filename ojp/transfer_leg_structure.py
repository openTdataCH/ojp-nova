from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime, XmlDuration
from ojp.continuous_modes_enumeration import ContinuousModesEnumeration
from ojp.general_attribute_structure import GeneralAttributeStructure
from ojp.international_text_structure import InternationalTextStructure
from ojp.path_guidance_structure import PathGuidanceStructure
from ojp.place_ref_structure import PlaceRefStructure
from ojp.situation_full_ref_2 import SituationFullRef2
from ojp.transfer_modes_enumeration import TransferModesEnumeration

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class TransferLegStructure:
    """
    [a specialised type of NAVIGATION PATH in TMv6] description of a LEG which
    links other LEGs of a TRIP where a TRANSFER between different LOCATIONs is
    required.

    :ivar transfer_mode: Mode that is used for this interchange between
        public services.
    :ivar continuous_mode: Mode that is used for this interchange
        between public services.
    :ivar leg_start: Stop/Station where boarding is done
    :ivar leg_end: Stop/Station to alight
    :ivar time_window_start: Time at which window begins.
    :ivar time_window_end: Time at which window ends.
    :ivar duration: Overall duration of this interchange.
    :ivar walk_duration: Walk time as part of the overall interchange
        duration.
    :ivar buffer_time: Buffer time as part of the overall interchange
        duration. Buffer times, f.e. check in/out times, sometimes are
        mandatory for using certain services as f.e. airplanes, ferries
        or highspeed trains.
    :ivar leg_description: Text that describes this interchange.
    :ivar length: Length of this interchange path.
    :ivar attribute: Note or service attribute.
    :ivar path_guidance: Structured model further describing this
        interchange, its geographic embedding and accessibility.
    :ivar situation_full_ref:
    :ivar extension:
    """
    transfer_mode: Optional[TransferModesEnumeration] = field(
        default=None,
        metadata={
            "name": "TransferMode",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    continuous_mode: Optional[ContinuousModesEnumeration] = field(
        default=None,
        metadata={
            "name": "ContinuousMode",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    leg_start: Optional[PlaceRefStructure] = field(
        default=None,
        metadata={
            "name": "LegStart",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
    leg_end: Optional[PlaceRefStructure] = field(
        default=None,
        metadata={
            "name": "LegEnd",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
    time_window_start: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TimeWindowStart",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    time_window_end: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TimeWindowEnd",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "Duration",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
    walk_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "WalkDuration",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    buffer_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "BufferTime",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    leg_description: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "LegDescription",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    length: Optional[int] = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    attribute: List[GeneralAttributeStructure] = field(
        default_factory=list,
        metadata={
            "name": "Attribute",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    path_guidance: Optional[PathGuidanceStructure] = field(
        default=None,
        metadata={
            "name": "PathGuidance",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    situation_full_ref: List[SituationFullRef2] = field(
        default_factory=list,
        metadata={
            "name": "SituationFullRef",
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
