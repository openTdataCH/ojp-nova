from dataclasses import dataclass, field
from typing import Optional

from ojp2.mode_filter_structure import ModeFilterStructure
from ojp2.operator_filter_structure import OperatorFilterStructure
from ojp2.participant_ref_structure import ParticipantRefStructure
from ojp2.place_type_enumeration import PlaceTypeEnumeration
from ojp2.place_usage_enumeration import PlaceUsageEnumeration
from ojp2.topographic_place_ref_structure import TopographicPlaceRefStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class ExchangePointsParamStructure:
    """
    :ivar type_value: Allowed location/place object types. If none is
        given, all types are allowed.
    :ivar usage: Defines, whether the location/place object of this
        request acts as origin, via or destination point of the
        passenger journey.
    :ivar modes: Allowed public transport modes. Defines, which public
        transport modes must be available at the returned location/place
        objects. Applies only to stops.
    :ivar operator_filter: Filter for locations/places that are operated
        by certain organisations.
    :ivar topographic_place_ref: If at least one is set, only
        location/place objects within the given localities are allowed.
    :ivar destination_system: Reference to system in which the
        destination (or origin) of the passenger is located.
    :ivar adjacent_system: One or more adjacent systems to which the
        exchange points should be retrieved.
    :ivar language: Preferred language in which to return text values.
    :ivar number_of_results: Maximum number of results to be returned.
        The service is allowed to return fewer objects if reasonable or
        otherwise appropriate. If the number of matching objects is
        expected to be large (e.g., in the case that all objects should
        be delivered) this parameter can be used to partition the
        response delivery into smaller chunks. The location information
        service is expected to support a response volume of at least 500
        location objects within one single response.
    :ivar continue_at: Tells the server to skip the mentioned number of
        results in its response. Can be used in a follow-up request to
        get further results. The value is usually taken from the
        previous response.
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
    destination_system: Optional[ParticipantRefStructure] = field(
        default=None,
        metadata={
            "name": "DestinationSystem",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    adjacent_system: list[ParticipantRefStructure] = field(
        default_factory=list,
        metadata={
            "name": "AdjacentSystem",
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
    extension: Optional[object] = field(
        default=None,
        metadata={
            "name": "Extension",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
