from dataclasses import dataclass

from ojp2.journey_ref_structure import JourneyRefStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class JourneyRef(JourneyRefStructure):
    """
    Reference to a Journey.
    """

    class Meta:
        namespace = "http://www.vdv.de/ojp"
