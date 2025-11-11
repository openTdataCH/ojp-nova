from dataclasses import dataclass

from ojp2.point_of_interest_ref_structure import PointOfInterestRefStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class PointOfInterestRef(PointOfInterestRefStructure):
    """
    Reference to a Point of Interest.
    """

    class Meta:
        namespace = "http://www.vdv.de/ojp"
