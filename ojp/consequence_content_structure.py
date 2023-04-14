from dataclasses import dataclass, field
from typing import List, Optional
from ojp.defaulted_text_structure import DefaultedTextStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ConsequenceContentStructure:
    """
    :ivar consequence_text: Consequence of passenger information action
        in a specific language.
    :ivar consequence_priority: Prioritises a consequence from the
        information owner's point of view, e.g. usable for sorting or
        hiding individual consequences. 1 = highest priority.
    """
    consequence_text: List[DefaultedTextStructure] = field(
        default_factory=list,
        metadata={
            "name": "ConsequenceText",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        }
    )
    consequence_priority: Optional[int] = field(
        default=None,
        metadata={
            "name": "ConsequencePriority",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
