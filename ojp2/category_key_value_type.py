from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class CategoryKeyValueType:
    """Category Key Value triplets.

    Category can be empty. Several such elements form the information
    necessary for a given category.
    """

    category: Optional[str] = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
