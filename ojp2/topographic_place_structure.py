from dataclasses import dataclass, field
from typing import Optional

from ojp2.area_structure import AreaStructure
from ojp2.international_text_structure import InternationalTextStructure
from ojp2.participant_ref_structure import ParticipantRefStructure
from ojp2.private_code_structure import PrivateCodeStructure
from ojp2.topographic_place_ref_structure import TopographicPlaceRefStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class TopographicPlaceStructure:
    """[TMv6] A type of PLACE providing the topographical context when searching
    for or presenting travel information, for example as the origin or destination
    of a trip.

    It may be of any size (e.g., County,City, Town, Village) and of
    different specificity (e.g., Greater London, London, West End,
    Westminster, St James's).

    :ivar topographic_place_code: TopographicPlace ID.
    :ivar topographic_place_name: Name or description of
        TopographicPlace for use in passenger information.
    :ivar private_code: Code of this TopographicPlace in
        private/foreign/proprietary coding schemes.
    :ivar parent_ref: Reference to a parent TopographicPlace.
    :ivar referred_system: Used in distributed environments (e.g., EU-
        Spirit). If set, this topographic place resides within the given
        system (in EU-Spirit "passive server"). This system can be
        queried for actual places within this topographic place. This is
        used in a distributed environment for a two-steps place
        identification. In EU-Spirit the system IDs were previously
        called "provider code". See https://eu-spirit.eu/
    :ivar area: Area covered by the locality described as a polygon.
    """

    topographic_place_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "TopographicPlaceCode",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
    topographic_place_name: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "TopographicPlaceName",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
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
    parent_ref: Optional[TopographicPlaceRefStructure] = field(
        default=None,
        metadata={
            "name": "ParentRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    referred_system: Optional[ParticipantRefStructure] = field(
        default=None,
        metadata={
            "name": "ReferredSystem",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    area: Optional[AreaStructure] = field(
        default=None,
        metadata={
            "name": "Area",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
