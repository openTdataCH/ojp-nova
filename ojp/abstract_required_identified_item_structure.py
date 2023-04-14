from dataclasses import dataclass, field
from typing import Optional
from ojp.abstract_item_structure import AbstractItemStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AbstractRequiredIdentifiedItemStructure(AbstractItemStructure):
    """
    Type for an Activity that can be referenced.

    :ivar item_identifier: Identifier of item.
    """
    item_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItemIdentifier",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
