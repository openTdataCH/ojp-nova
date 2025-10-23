from dataclasses import dataclass, field
from typing import List, Optional
from ojp.address_structure import AddressStructure
from ojp.general_attribute_structure import GeneralAttributeStructure
from ojp.international_text_structure import InternationalTextStructure
from ojp.location_structure import LocationStructure
from ojp.point_of_interest_structure import PointOfInterestStructure
from ojp.stop_place_structure import StopPlaceStructure
from ojp.stop_point_structure import StopPointStructure
from ojp.topographic_place_structure import TopographicPlaceStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class PlaceStructure:
    """
    Geographic PLACE of any type which may be specified as the origin or
    destination of a trip.

    :ivar stop_point:
    :ivar stop_place:
    :ivar topographic_place: TopographicPlace, village or city.
    :ivar point_of_interest:
    :ivar address:
    :ivar location_name: Public name of the location.
    :ivar geo_position:
    :ivar attribute: Attribute associated with this location.
    :ivar extension:
    """
    stop_point: Optional[StopPointStructure] = field(
        default=None,
        metadata={
            "name": "StopPoint",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    stop_place: Optional[StopPlaceStructure] = field(
        default=None,
        metadata={
            "name": "StopPlace",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    topographic_place: Optional[TopographicPlaceStructure] = field(
        default=None,
        metadata={
            "name": "TopographicPlace",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    point_of_interest: Optional[PointOfInterestStructure] = field(
        default=None,
        metadata={
            "name": "PointOfInterest",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    address: Optional[AddressStructure] = field(
        default=None,
        metadata={
            "name": "Address",
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
    geo_position: Optional[LocationStructure] = field(
        default=None,
        metadata={
            "name": "GeoPosition",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
    attribute: List[GeneralAttributeStructure] = field(
        default_factory=list,
        metadata={
            "name": "Attribute",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    extension: Optional[object] = field(
        default=None,
        metadata={
            "name": "Extension",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
