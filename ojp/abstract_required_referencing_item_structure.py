from dataclasses import dataclass, field
from typing import Optional
from ojp.abstract_item_structure import AbstractItemStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AbstractRequiredReferencingItemStructure(AbstractItemStructure):
    """
    Type for an Activity that references a previous Activity.

    :ivar item_ref: Reference to an Activity Element of  a delivery.
    """
    item_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItemRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
