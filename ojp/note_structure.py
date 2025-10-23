from dataclasses import dataclass, field
from typing import Optional
from ojp.natural_language_string_structure import NaturalLanguageStringStructure
from ojp.situation_full_ref_1 import SituationFullRef1
from ojp.situation_ref import SituationRef

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class NoteStructure:
    """
    DataType for a NOTICe.

    :ivar situation_ref:
    :ivar situation_simple_ref:
    :ivar situation_full_ref:
    :ivar note: Text annotation that applies to an element.
    """
    situation_ref: Optional[SituationRef] = field(
        default=None,
        metadata={
            "name": "SituationRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    situation_simple_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SituationSimpleRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    situation_full_ref: Optional[SituationFullRef1] = field(
        default=None,
        metadata={
            "name": "SituationFullRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    note: Optional[NaturalLanguageStringStructure] = field(
        default=None,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
