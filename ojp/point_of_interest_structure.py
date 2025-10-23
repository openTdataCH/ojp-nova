from dataclasses import dataclass, field
from typing import List, Optional
from ojp.international_text_structure import InternationalTextStructure
from ojp.point_of_interest_category_structure import PointOfInterestCategoryStructure
from ojp.private_code_structure import PrivateCodeStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class PointOfInterestStructure:
    """
    [corresponds to POINT OF INTEREST in TMv6 with related information] type of
    PLACE to or through which passengers may wish to navigate as part of their
    journey and which is modelled in detail by journey planners.

    :ivar point_of_interest_code: ID of this Point of Interest.
    :ivar point_of_interest_name: Name or description of point of
        interest for use in passenger information.
    :ivar name_suffix: Additional description of the point of interest
        that may be appended to the name if enough space is available.
        F.e. "Exhibition Center".
    :ivar point_of_interest_category: Categories this POI is associated
        with. Order indicates descending relevance.
    :ivar private_code: Code of this point of interest in
        private/foreign/proprietary coding schemes.
    :ivar topographic_place_ref:
    """
    point_of_interest_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PointOfInterestCode",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
    point_of_interest_name: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "PointOfInterestName",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
    name_suffix: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "NameSuffix",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    point_of_interest_category: List[PointOfInterestCategoryStructure] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterestCategory",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
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
    topographic_place_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "TopographicPlaceRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
