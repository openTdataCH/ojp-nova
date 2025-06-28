from dataclasses import dataclass, field
from typing import Optional

from ojp2.address_ref import AddressRef
from ojp2.international_text_structure import InternationalTextStructure
from ojp2.location_structure import LocationStructure
from ojp2.point_of_interest_ref import PointOfInterestRef
from ojp2.stop_place_ref_2 import StopPlaceRef2
from ojp2.stop_point_ref import StopPointRef
from ojp2.topographic_place_ref import TopographicPlaceRef

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class PlaceRefStructure:
    """
    Reference to a geographic PLACE of any type which may be specified as the
    origin or destination of a trip.

    :ivar stop_point_ref: Reference to a stop point.
    :ivar stop_place_ref:
    :ivar geo_position: WGS84 coordinates position.
    :ivar topographic_place_ref:
    :ivar point_of_interest_ref:
    :ivar address_ref:
    :ivar name: Public name of the place.
    :ivar allowed_system_id: Used in distributed environments. e.g., EU-
        Spirit. If none is given, the place information request refers
        to all known systems (in EU-Spirit "passive servers"). If at
        least one is given, the place information request refers only to
        the given systems (in EU-Spirit "passive servers"). In EU-Spirit
        the system IDs were previously called "provider code". See
        https://eu-spirit.eu/
    """

    stop_point_ref: Optional[StopPointRef] = field(
        default=None,
        metadata={
            "name": "StopPointRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_place_ref: Optional[StopPlaceRef2] = field(
        default=None,
        metadata={
            "name": "StopPlaceRef",
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
    topographic_place_ref: Optional[TopographicPlaceRef] = field(
        default=None,
        metadata={
            "name": "TopographicPlaceRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    point_of_interest_ref: Optional[PointOfInterestRef] = field(
        default=None,
        metadata={
            "name": "PointOfInterestRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    address_ref: Optional[AddressRef] = field(
        default=None,
        metadata={
            "name": "AddressRef",
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
    allowed_system_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "AllowedSystemId",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
