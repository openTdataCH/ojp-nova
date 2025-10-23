from dataclasses import dataclass, field
from typing import List, Optional
from ojp.international_text_structure import InternationalTextStructure
from ojp.location_structure import LocationStructure
from ojp.private_code_structure import PrivateCodeStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class TopographicPlaceStructure:
    """[TMv6] A type of PLACE providing the topographical context when searching
    for or presenting travel information, for example as the origin or destination
    of a trip.

    It may be of any size (e.g. County,City, Town, Village) and of
    different specificity (e.g. Greater London, London, West End,
    Westminster, St James's).

    :ivar topographic_place_code: TopographicPlace ID.
    :ivar topographic_place_name: Name or description of
        TopographicPlace for use in passenger information.
    :ivar private_code: Code of this TopographicPlace in
        private/foreign/proprietary coding schemes.
    :ivar parent_ref: Reference to a parent TopographicPlace.
    :ivar area: Area covered by the locality described as a polygon.
    """
    topographic_place_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "TopographicPlaceCode",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
    topographic_place_name: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "TopographicPlaceName",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
    private_code: List[PrivateCodeStructure] = field(
        default_factory=list,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    parent_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ParentRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    area: Optional["TopographicPlaceStructure.Area"] = field(
        default=None,
        metadata={
            "name": "Area",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )

    @dataclass
    class Area:
        points: List[LocationStructure] = field(
            default_factory=list,
            metadata={
                "name": "Points",
                "type": "Element",
                "namespace": "http://www.vdv.de/ojp",
                "min_occurs": 3,
            }
        )
