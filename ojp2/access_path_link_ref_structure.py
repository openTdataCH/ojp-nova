from dataclasses import dataclass

from ojp2.stop_place_component_ref_structure import (
    StopPlaceComponentRefStructure,
)

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class AccessPathLinkRefStructure(StopPlaceComponentRefStructure):
    """
    Type for reference to identifier of PATHLINK.
    """
