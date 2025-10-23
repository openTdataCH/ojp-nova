from dataclasses import dataclass, field
from typing import Optional
from ojp.geo_restrictions_structure import GeoRestrictionsStructure
from ojp.location_structure import LocationStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class InitialLocationInputStructure:
    """
    :ivar location_name: Name of the location object which is looked
        after. This is usually the user's input. If not given, the name
        of the resulting location objects is not relevant.
    :ivar geo_position: Coordinate where to look for locations. If
        given, the result should prefer location objects near to this
        GeoPosition.
    :ivar geo_restriction: Restricts the resulting location objects to
        the given geographical area.
    """
    location_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocationName",
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
    geo_restriction: Optional[GeoRestrictionsStructure] = field(
        default=None,
        metadata={
            "name": "GeoRestriction",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
