from dataclasses import dataclass

from ojp2.related_journey_structure import RelatedJourneyStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class RelatedJourney(RelatedJourneyStructure):
    """Refers to the JOURNEY to which the current JOURNEY is related.

    (since SIRI 2.1)
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
