from dataclasses import dataclass, field
from typing import Optional
from ojp.international_text_structure import InternationalTextStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class ErrorMessageStructure:
    """
    Structured error messages.

    :ivar code: Code of the error situation.
    :ivar text: Description of the error situation.
    """
    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
    text: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "Text",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
