from dataclasses import dataclass, field
from typing import Optional

from ojp2.abstract_item_structure import AbstractItemStructure
from ojp2.item_ref_structure import ItemRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AbstractRequiredReferencingItemStructure(AbstractItemStructure):
    """
    Type for an Activity that references a previous Activity.

    :ivar item_ref: Reference to an Activity Element of a delivery.
    """

    item_ref: Optional[ItemRefStructure] = field(
        default=None,
        metadata={
            "name": "ItemRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
