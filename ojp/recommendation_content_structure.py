from dataclasses import dataclass, field
from typing import List, Optional
from ojp.defaulted_text_structure import DefaultedTextStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class RecommendationContentStructure:
    """
    :ivar recommendation_text: Recommendation of passenger information
        action in a specific language.
    :ivar recommendation_priority: Prioritises a recommendation from the
        information owner's point of view, e.g. usable for sorting or
        hiding individual recommendations. 1 = highest priority.
    """
    recommendation_text: List[DefaultedTextStructure] = field(
        default_factory=list,
        metadata={
            "name": "RecommendationText",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        }
    )
    recommendation_priority: Optional[int] = field(
        default=None,
        metadata={
            "name": "RecommendationPriority",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
