from dataclasses import dataclass, field
from typing import Optional

from ojp2.international_text_structure import InternationalTextStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class WebLinkStructure:
    """
    URL of a web resource with label.

    :ivar label: Label for link description.
    :ivar url: URL to resource on web.
    :ivar mime_type: MIME type of the referenced resource. To which kind
        of resource does the URL point to?
    :ivar embeddable: Is the referenced resource meant to be embedded as
        a webview in a surrounding context, e.g., app or web page? If
        yes, the resource has to be fully responsive. Default is false.
    """

    label: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "name": "Url",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
    mime_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "MimeType",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    embeddable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Embeddable",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
