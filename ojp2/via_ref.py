from dataclasses import dataclass

from ojp2.journey_place_ref_structure import JourneyPlaceRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ViaRef(JourneyPlaceRefStructure):
    """
    Reference to a SCHEDULED STOP POINT that is a VIA point on the journey.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
