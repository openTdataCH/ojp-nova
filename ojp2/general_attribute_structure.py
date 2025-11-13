from dataclasses import dataclass, field
from typing import Optional

from ojp2.all_facilities_feature_structure import AllFacilitiesFeatureStructure
from ojp2.international_text_structure import InternationalTextStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class GeneralAttributeStructure:
    """Structured attribute classification with associated text.

    If URL is given, it refers to the whole attribute text.

    :ivar user_text: Text of the attribute to be shown to the user.
    :ivar code: Internal code of the attribute. Can be used for
        detection of double occurrences.
    :ivar key: Key if the attribute is used as a key/value pair.
    :ivar value: Value if the attribute is used as a key/value pair.
    :ivar facility: Facilities associated with this attribute.
    :ivar mandatory: Defines whether the attribute has to be shown to
        the user.
    :ivar importance: Importance of the attribute.
    :ivar url: URL to resource on web.
    :ivar mime_type: MIME type of the referenced resource. To which kind
        of resource does the URL point to?
    :ivar embeddable: Is the referenced resource meant to be embedded as
        a webview in a surrounding context, e.g., app or web page? If
        yes, the resource has to be fully responsive. Default is false.
    """

    user_text: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "UserText",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    facility: list[AllFacilitiesFeatureStructure] = field(
        default_factory=list,
        metadata={
            "name": "Facility",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    mandatory: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Mandatory",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    importance: Optional[int] = field(
        default=None,
        metadata={
            "name": "Importance",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "max_inclusive": 100,
        },
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "name": "Url",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
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
