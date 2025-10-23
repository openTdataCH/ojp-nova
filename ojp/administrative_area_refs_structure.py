from dataclasses import dataclass, field
from typing import List
from ojp.administrative_area_versioned_ref_structure import AdministrativeAreaVersionedRefStructure

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class AdministrativeAreaRefsStructure:
    """
    Type for a collection of one or more references to ADMINISTRATIVE ZONEs.

    :ivar administrative_area_ref: Reference to the identifier of an
        ADMINISTRATIVE ZONE.
    """
    administrative_area_ref: List[AdministrativeAreaVersionedRefStructure] = field(
        default_factory=list,
        metadata={
            "name": "AdministrativeAreaRef",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
            "min_occurs": 1,
        }
    )
