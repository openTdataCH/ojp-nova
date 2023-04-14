from dataclasses import dataclass, field
from typing import Optional
from ojp.natural_language_string_structure import NaturalLanguageStringStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class BrandingStructure:
    """An arbitrary marketing classification.

    (since SIRI 2.1)

    :ivar branding_code: Identity of BRANDING.
    :ivar name: Name of TYPE OF VALUE.
    :ivar short_name: Short Name for TYPE OF VALUE.
    :ivar description: Description of TYPE OF VALUE.
    :ivar image: Default image for TYPE OF VALUE.
    :ivar url: Default URL for TYPE OF VALUE.
    :ivar private_code: Arbitrary code (usually the technical part of
        the identifier).
    """
    branding_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "BrandingCode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    name: Optional[NaturalLanguageStringStructure] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    short_name: Optional[NaturalLanguageStringStructure] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    description: Optional[NaturalLanguageStringStructure] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    image: Optional[str] = field(
        default=None,
        metadata={
            "name": "Image",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "name": "Url",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    private_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
