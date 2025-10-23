from dataclasses import dataclass, field
from typing import Optional
from ojp.international_text_structure import InternationalTextStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class WebLinkStructure:
    """
    URL of a web resource with label.

    :ivar label: Label for link description.
    :ivar url: URL to resource on web.
    """
    label: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "name": "Url",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
