from dataclasses import dataclass, field
from typing import List, Optional
from ojp.defaulted_text_structure import DefaultedTextStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class RemarkContentStructure:
    """
    :ivar remark: Further remark to passengers, e,g, "For more
        information call xy".
    :ivar remark_priority: Prioritises a remark from the information
        owner's point of view, e.g. usable for sorting or hiding
        individual remarks. 1 = highest priority.
    """
    remark: List[DefaultedTextStructure] = field(
        default_factory=list,
        metadata={
            "name": "Remark",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        }
    )
    remark_priority: Optional[int] = field(
        default=None,
        metadata={
            "name": "RemarkPriority",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
