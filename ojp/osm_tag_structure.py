from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OsmTagStructure:
    """
    Structure of an Open Street Map tag.

    :ivar tag: Name of Open Street Map tag (amenity, leisure, tourism,
        bike, ...)
    :ivar value: Value for Open Street Map tag (charging_station,
        hostel, yes, ...)
    """
    tag: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tag",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
