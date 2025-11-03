from dataclasses import dataclass, field
from typing import Optional

from ojp2.image_structure import ImageStructure
from ojp2.link_content_enumeration import LinkContentEnumeration
from ojp2.natural_language_string_structure import (
    NaturalLanguageStringStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class InfoLinkStructure2:
    """
    Type for a general hyperlink.

    :ivar uri: URI for link.
    :ivar label: Label for Link.  (Unbounded since SIRI 2.0)
    :ivar image: Image to use when presenting hyperlink.
    :ivar link_content: Categorisation of link content.
    """

    class Meta:
        name = "InfoLinkStructure"

    uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "Uri",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    label: list[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "Label",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    image: Optional[ImageStructure] = field(
        default=None,
        metadata={
            "name": "Image",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    link_content: Optional[LinkContentEnumeration] = field(
        default=None,
        metadata={
            "name": "LinkContent",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
