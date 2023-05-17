from dataclasses import dataclass, field
from typing import List, Optional
from ojp.natural_language_string_structure import NaturalLanguageStringStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class StopAssignmentStructure:
    """
    Type for assignment of a SCHEDULED STOP POINT to a specific QUAY or platform
    +SIRI v2.0.

    :ivar aimed_quay_ref: Physical QUAY to use according to the planned
        timetable. +SIRI v2.0
    :ivar aimed_quay_name: Scheduled Platform name. Can be used to
        indicate platfrom change. +SIRI v2.0
    :ivar expected_quay_ref: Physical QUAY to use accoring to the real-
        time prediction. +SIRI v2.0
    :ivar actual_quay_ref: Physical QUAY actually used. +SIRI v2.0
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
    expected_quay_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExpectedQuayRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    actual_quay_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ActualQuayRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
