from dataclasses import dataclass

from ojp2.stop_place_space_ref_structure import StopPlaceSpaceRefStructure

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class StopPlaceEntranceRefStructure(StopPlaceSpaceRefStructure):
    """
    Type for reference to STOP PLACE Entrance.
    """
