from dataclasses import dataclass, field
from typing import List, Optional
from ojp.point_of_interest_category_structure import PointOfInterestCategoryStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class PointOfInterestFilterStructure:
    """
    :ivar exclude: Whether categories in list are to include or exclude
        from search. Default is FALSE.
    :ivar point_of_interest_category: These can be used to filter POI
        types of locations even more by additional category filters. If
        more than one is given the filtering is by logical "OR" (when
        Exclude=FALSE) and logical "AND" (when Exclude=TRUE).
    """
    exclude: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Exclude",
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
