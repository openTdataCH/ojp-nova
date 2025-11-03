from dataclasses import dataclass, field
from typing import Optional

from ojp2.international_text_structure import InternationalTextStructure
from ojp2.point_of_interest_additional_information_structure import (
    PointOfInterestAdditionalInformationStructure,
)
from ojp2.point_of_interest_category_structure import (
    PointOfInterestCategoryStructure,
)
from ojp2.private_code_structure import PrivateCodeStructure
from ojp2.topographic_place_ref import TopographicPlaceRef

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class PointOfInterestStructure:
    """
    [corresponds to POINT OF INTEREST in TMv6 with related information] type of
    PLACE to or through which passengers may wish to navigate as part of their
    journey and which is modelled in detail by journey planners.

    :ivar public_code: ID of this Point of Interest.
    :ivar name: Name or description of point of interest for use in
        passenger information.
    :ivar name_suffix: Additional description of the point of interest
        that may be appended to the name if enough space is available.
        E.g. "Exhibition Center".
    :ivar point_of_interest_category: Categories this POI is associated
        with. Order indicates descending relevance.
    :ivar private_code: Code of this point of interest in
        private/foreign/proprietary coding schemes.
    :ivar topographic_place_ref:
    :ivar poiadditional_information: Additional information for this POI
        (e.g., information on available parking slots, charging
        infrastructure, sharing vehicles).
    """

    public_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
    name: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "Name",
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
    point_of_interest_category: list[PointOfInterestCategoryStructure] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterestCategory",
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
    topographic_place_ref: Optional[TopographicPlaceRef] = field(
        default=None,
        metadata={
            "name": "TopographicPlaceRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    poiadditional_information: Optional[
        PointOfInterestAdditionalInformationStructure
    ] = field(
        default=None,
        metadata={
            "name": "POIAdditionalInformation",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
