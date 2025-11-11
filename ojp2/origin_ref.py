from dataclasses import dataclass

from ojp2.journey_place_ref_structure import JourneyPlaceRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class OriginRef(JourneyPlaceRefStructure):
    """
    Reference to the origin SCHEDULED STOP POINT of the journey.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
