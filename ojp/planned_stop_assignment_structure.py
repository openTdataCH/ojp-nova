from dataclasses import dataclass, field
from typing import List, Optional
from ojp.natural_language_string_structure import NaturalLanguageStringStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class PlannedStopAssignmentStructure:
    """
    Type for assignment of a SCHEDULED STOP POINT to a specific QUAY or platform
    +SIRI v2.0.

    :ivar aimed_quay_ref: Physical QUAY to use according to the planned
        timetable. +SIRI v2.0
    :ivar aimed_quay_name: Scheduled Platform name. +SIRI v2.0
    """
    aimed_quay_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "AimedQuayRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    aimed_quay_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "AimedQuayName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
