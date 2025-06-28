from dataclasses import dataclass, field
from typing import Optional

from ojp2.access_modes_list_of_enumerations import (
    AccessModesListOfEnumerations,
)
from ojp2.address_structure import AddressStructure
from ojp2.general_attribute_structure import GeneralAttributeStructure
from ojp2.international_text_structure import InternationalTextStructure
from ojp2.location_structure import LocationStructure
from ojp2.mode_structure import ModeStructure
from ojp2.point_of_interest_structure import PointOfInterestStructure
from ojp2.situation_ref_list import SituationRefList
from ojp2.stop_place_structure import StopPlaceStructure
from ojp2.stop_point_structure import StopPointStructure
from ojp2.topographic_place_structure import TopographicPlaceStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class PlaceStructure:
    """
    Geographic PLACE of any type which may be specified as the origin or
    destination of a trip.

    :ivar stop_point: Model of a stop point
    :ivar stop_place: Model of a stop place
    :ivar topographic_place: TopographicPlace. Region, village, or city.
    :ivar point_of_interest: Model of a POI
    :ivar address: Model of an address
    :ivar name: Public name of the place.
    :ivar geo_position: Position using WGS84/EPSG:4326 coordinates.
    :ivar mode: List of transport modes that call at this place object.
        This list should only be filled in case of stop points or stop
        places – and only when explicitly requested.
    :ivar access_mode_list: Access modes that are supported by this
        place.
    :ivar situation_full_refs: SITUATION reference. Mostly used for STOP
        PLACE, SCHEDULED STOP POINT (StopPoint). However, in future a
        situation reference may occur on many geographic elements (e.g.,
        roads) as well.
    :ivar attribute: Attributes associated with this place. This is
        used, e.g., for details, OSM attributes or key/value
        descriptions. Most of them will be implementation dependent
        (except OSM). From Transmodel, TYPE OF POINT might be an
        attribute.
    :ivar extension:
    """

    stop_point: Optional[StopPointStructure] = field(
        default=None,
        metadata={
            "name": "StopPoint",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    stop_place: Optional[StopPlaceStructure] = field(
        default=None,
        metadata={
            "name": "StopPlace",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    topographic_place: Optional[TopographicPlaceStructure] = field(
        default=None,
        metadata={
            "name": "TopographicPlace",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    point_of_interest: Optional[PointOfInterestStructure] = field(
        default=None,
        metadata={
            "name": "PointOfInterest",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    address: Optional[AddressStructure] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
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
    geo_position: Optional[LocationStructure] = field(
        default=None,
        metadata={
            "name": "GeoPosition",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
    mode: list[ModeStructure] = field(
        default_factory=list,
        metadata={
            "name": "Mode",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    access_mode_list: Optional[AccessModesListOfEnumerations] = field(
        default=None,
        metadata={
            "name": "AccessModeList",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    situation_full_refs: Optional[SituationRefList] = field(
        default=None,
        metadata={
            "name": "SituationFullRefs",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    attribute: list[GeneralAttributeStructure] = field(
        default_factory=list,
        metadata={
            "name": "Attribute",
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
