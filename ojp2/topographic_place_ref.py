from dataclasses import dataclass

from ojp2.topographic_place_ref_structure import TopographicPlaceRefStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class TopographicPlaceRef(TopographicPlaceRefStructure):
    """
    Reference to a TopographicPlace.
    """

    class Meta:
        namespace = "http://www.vdv.de/ojp"
