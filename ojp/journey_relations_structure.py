from dataclasses import dataclass, field
from typing import List
from ojp.journey_relation_structure import JourneyRelationStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class JourneyRelationsStructure:
    """Provides information about relations to other journeys.

    (since SIRI 2.1)
    """
    journey_relation: List[JourneyRelationStructure] = field(
        default_factory=list,
        metadata={
            "name": "JourneyRelation",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        }
    )
