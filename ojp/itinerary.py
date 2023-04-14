from dataclasses import dataclass, field
from typing import List, Optional
from ojp.destination import Destination
from ojp.extension_type import ExtensionType
from ojp.group_of_locations import GroupOfLocations
from ojp.location import Location

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class Itinerary(GroupOfLocations):
    location_contained_in_itinerary: List["Itinerary.LocationContainedInItinerary"] = field(
        default_factory=list,
        metadata={
            "name": "locationContainedInItinerary",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        }
    )
    route_destination: List[Destination] = field(
        default_factory=list,
        metadata={
            "name": "routeDestination",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    itinerary_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "itineraryExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )

    @dataclass
    class LocationContainedInItinerary(Location):
        index: Optional[int] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
