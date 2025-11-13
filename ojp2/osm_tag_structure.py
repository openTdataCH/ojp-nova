from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OsmTagStructure:
    """
    Structure of an OpenStreetMap tag.

    :ivar tag: Name of OpenStreetMap tag (amenity, leisure, tourism,
        bike, ...)
    :ivar value: Value for OpenStreetMap tag (charging_station, hostel,
        yes, ...)
    """

    tag: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tag",
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
