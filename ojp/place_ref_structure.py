from dataclasses import dataclass, field
from typing import Optional
from ojp.international_text_structure import InternationalTextStructure
from ojp.location_structure import LocationStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class PlaceRefStructure:
    """
    Reference to a geographic PLACE of any type which may be specified as the
    origin or destination of a trip.

    :ivar stop_point_ref:
    :ivar stop_place_ref:
    :ivar geo_position: WGS84 coordinates position.
    :ivar topographic_place_ref:
    :ivar point_of_interest_ref:
    :ivar address_ref:
    :ivar location_name: Public name of the location.
    """
    stop_point_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "StopPointRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    stop_place_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "StopPlaceRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    geo_position: Optional[LocationStructure] = field(
        default=None,
        metadata={
            "name": "GeoPosition",
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
    point_of_interest_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "PointOfInterestRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    address_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "AddressRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    location_name: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "LocationName",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
