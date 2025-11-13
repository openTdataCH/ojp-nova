from dataclasses import dataclass, field
from typing import Optional

from ojp2.affected_road_structure import AffectedRoadStructure
from ojp2.group_of_locations import GroupOfLocations

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AffectedRoadsStructure:
    """
    Type for Location model for scope of SITUATION or effect.

    :ivar datex2_locations: Refereences to road network locations
        affected by the SITUATION.
    :ivar affected_road: Description of affected road.
    """

    datex2_locations: Optional[GroupOfLocations] = field(
        default=None,
        metadata={
            "name": "Datex2Locations",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    affected_road: list[AffectedRoadStructure] = field(
        default_factory=list,
        metadata={
            "name": "AffectedRoad",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
