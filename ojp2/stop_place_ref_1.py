from dataclasses import dataclass

from ojp2.stop_place_ref_structure_1 import StopPlaceRefStructure1

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class StopPlaceRef1(StopPlaceRefStructure1):
    """
    Reference to a STOP PLACE.
    """

    class Meta:
        name = "StopPlaceRef"
        namespace = "http://www.ifopt.org.uk/ifopt"
