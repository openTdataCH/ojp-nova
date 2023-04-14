from dataclasses import dataclass, field
from typing import Optional
from ojp.image_content_enumeration import ImageContentEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ImageStructure:
    """
    Type for image.

    :ivar image_ref: Reference to an image.
    :ivar image_binary: Embedded image.
    :ivar image_content: Categorisation of image content.
    """
    image_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ImageRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    image_binary: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "ImageBinary",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "format": "base64",
        }
    )
    image_content: Optional[ImageContentEnumeration] = field(
        default=None,
        metadata={
            "name": "ImageContent",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
