from dataclasses import dataclass, field
from typing import Optional

from ojp2.location_structure import LocationStructure
from ojp2.mode_filter_structure import ModeFilterStructure
from ojp2.operator_filter_structure import OperatorFilterStructure
from ojp2.place_type_enumeration import PlaceTypeEnumeration
from ojp2.place_usage_enumeration import PlaceUsageEnumeration
from ojp2.point_of_interest_filter_structure import (
    PointOfInterestFilterStructure,
)
from ojp2.topographic_place_ref_structure import TopographicPlaceRefStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class PlaceParamStructure:
    """
    :ivar type_value: Allowed location/place object types. If none is
        given, all types are allowed.
    :ivar usage: Defines, whether location/place objects for origin,
        via, or destination are searched.
    :ivar modes: Allowed public transport modes. Defines, which public
        transport modes must be available at the returned location/place
        objects. Applies only to stops.
    :ivar operator_filter: Filter for locations/places that are operated
        by certain organisations.
    :ivar topographic_place_ref: If at least one is set, only
        location/place objects within the given localities are allowed.
    :ivar point_of_interest_filter: Filter to narrow down POI searches.
    :ivar language: Preferred language in which to return text values.
    :ivar number_of_results: Maximum number of results to be returned.
        The service is allowed to return fewer objects if reasonable or
        otherwise appropriate. If the number of matching objects is
        expected to be large (e.g.: in the case that all objects should
        be delivered) this parameter can be used to partition the
        response delivery into smaller chunks. The place information
        service is expected to support a response volume of at least 500
        objects within one single response.
    :ivar continue_at: Tells the server to skip the mentioned number of
        results in its response. Can be used in a follow-up request to
        get further results. The value is usually taken from the
        previous response.
    :ivar include_pt_modes: Tells the service to include the available
        public transport modes at returned stops.
    :ivar include_operators: Tells the service to include the available
        operators at returned stops.
    :ivar sorting_method: If there are multiple sorting methods
        supported by the system, the client can choose one of the
        existing. Which methods are available needs to be known to the
        client and may differ from system to system. Therefore, use with
        care.
    :ivar geo_position: WGS84 coordinates position. Locations closer to
        this GeoPosition are preferred.
    :ivar minimal_probability: Ignore locations with a lower
        probability.
    :ivar extension:
    """

    type_value: list[PlaceTypeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    usage: Optional[PlaceUsageEnumeration] = field(
        default=None,
        metadata={
            "name": "Usage",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    modes: Optional[ModeFilterStructure] = field(
        default=None,
        metadata={
            "name": "Modes",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    operator_filter: Optional[OperatorFilterStructure] = field(
        default=None,
        metadata={
            "name": "OperatorFilter",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    topographic_place_ref: list[TopographicPlaceRefStructure] = field(
        default_factory=list,
        metadata={
            "name": "TopographicPlaceRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    point_of_interest_filter: Optional[PointOfInterestFilterStructure] = field(
        default=None,
        metadata={
            "name": "PointOfInterestFilter",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    language: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Language",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    number_of_results: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfResults",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    continue_at: Optional[int] = field(
        default=None,
        metadata={
            "name": "ContinueAt",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    include_pt_modes: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludePtModes",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    include_operators: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludeOperators",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    sorting_method: Optional[str] = field(
        default=None,
        metadata={
            "name": "SortingMethod",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    geo_position: Optional[LocationStructure] = field(
        default=None,
        metadata={
            "name": "GeoPosition",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    minimal_probability: Optional[float] = field(
        default=None,
        metadata={
            "name": "MinimalProbability",
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
