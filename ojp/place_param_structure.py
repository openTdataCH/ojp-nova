from dataclasses import dataclass, field
from typing import List, Optional
from ojp.operator_filter_structure import OperatorFilterStructure
from ojp.place_type_enumeration import PlaceTypeEnumeration
from ojp.place_usage_enumeration import PlaceUsageEnumeration
from ojp.point_of_interest_filter_structure import PointOfInterestFilterStructure
from ojp.pt_mode_filter_structure import PtModeFilterStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class PlaceParamStructure:
    """
    :ivar type: Allowed location object types. If none is given, all
        types are allowed.
    :ivar usage: Defines, whether location objects for origin, via, or
        destination are searched.
    :ivar pt_modes: Allowed public transport modes. Defines, which
        public transport modes must be available at the returned
        location objects. Applies only to stops.
    :ivar operator_filter: Filter for locations that are operated by
        certain organisations.
    :ivar topographic_place_ref: If at least one is set, only location
        objects within the given localities are allowed.
    :ivar point_of_interest_filter: Filter to narrow down POI searches.
    :ivar language: Preferred language in which to return text values.
    :ivar number_of_results:
    :ivar continue_at: Tells the server to skip the mentioned number of
        results in its response. Can be used in a follow-up request to
        get further results. The value is usually taken from the
        previous response.
    :ivar include_pt_modes: Tells the service to include the available
        public transport modes at returned stops.
    """
    type: List[PlaceTypeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    usage: Optional[PlaceUsageEnumeration] = field(
        default=None,
        metadata={
            "name": "Usage",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    pt_modes: Optional[PtModeFilterStructure] = field(
        default=None,
        metadata={
            "name": "PtModes",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    operator_filter: Optional[OperatorFilterStructure] = field(
        default=None,
        metadata={
            "name": "OperatorFilter",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    topographic_place_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "TopographicPlaceRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    point_of_interest_filter: Optional[PointOfInterestFilterStructure] = field(
        default=None,
        metadata={
            "name": "PointOfInterestFilter",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    number_of_results: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfResults",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    continue_at: Optional[int] = field(
        default=None,
        metadata={
            "name": "ContinueAt",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    include_pt_modes: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludePtModes",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
