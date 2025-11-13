from dataclasses import dataclass

from ojp2.stop_place_ref_structure_2 import StopPlaceRefStructure2

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class StopPlaceRef2(StopPlaceRefStructure2):
    """
    Reference to a Stop Place.
    """

    class Meta:
        name = "StopPlaceRef"
        namespace = "http://www.vdv.de/ojp"
