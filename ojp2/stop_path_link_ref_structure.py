from dataclasses import dataclass

from ojp2.stop_place_component_ref_structure import (
    StopPlaceComponentRefStructure,
)

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class StopPathLinkRefStructure(StopPlaceComponentRefStructure):
    """
    Type for reference to STOP PLACE Space.
    """
