from dataclasses import dataclass, field
from typing import List, Optional
from ojp.natural_language_string_structure import NaturalLanguageStringStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class PtAdviceStructure:
    """
    Type for advice.

    :ivar advice_ref: Reference to a standardis advisory NOTICE to be
        given to passengers if a particular condition arises .
    :ivar details: Further Textual advice to passengers.  (Unbounded
        since SIRI 2.0)
    """
    advice_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdviceRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    details: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "Details",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
