from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from ojp2.extension_type import ExtensionType
from ojp2.multilingual_string import MultilingualString

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class Comment:
    comment: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    comment_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "commentDateTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    comment_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "commentExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
