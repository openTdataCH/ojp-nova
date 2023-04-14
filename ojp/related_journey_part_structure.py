from dataclasses import dataclass
from ojp.journey_part_info_structure import JourneyPartInfoStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class RelatedJourneyPartStructure(JourneyPartInfoStructure):
    """The JOURNEY RELATION refers to this JOURNEY PART.

    (since SIRI 2.1)
    """
