from dataclasses import dataclass, field
from typing import List, Optional
from ojp.operator_filter_structure import OperatorFilterStructure
from ojp.place_type_enumeration import PlaceTypeEnumeration
from ojp.place_usage_enumeration import PlaceUsageEnumeration
from ojp.pt_mode_filter_structure import PtModeFilterStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class ExchangePointsParamStructure:
    """
    :ivar type: Allowed location object types. If none is given, all
        types are allowed.
    :ivar usage: Defines, whether the location object of this request
        acts as origin, via or destination point of the passenger
        journey.
    :ivar pt_modes: Allowed public transport modes. Defines, which
        public transport modes must be available at the returned
        location objects. Applies only to stops.
    :ivar operator_filter: Filter for locations that are operated by
        certain organisations.
    :ivar topographic_place_ref: If at least one is set, only location
        objects within the given localities are allowed.
    :ivar destination_system: Reference to system in which the
        destination (or origin) of the passenger is located.
    :ivar adjacent_system: One or more adjacent systems to which the
        exchange points should be retrieved.
    :ivar language: Preferred language in which to return text values.
    :ivar number_of_results:
    :ivar continue_at: Tells the server to skip the mentioned number of
        results in its response. Can be used in a follow-up request to
        get further results. The value is usually taken from the
        previous response.
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
    destination_system: Optional[str] = field(
        default=None,
        metadata={
            "name": "DestinationSystem",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    adjacent_system: List[str] = field(
        default_factory=list,
        metadata={
            "name": "AdjacentSystem",
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
