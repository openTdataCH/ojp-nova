from dataclasses import dataclass, field

from ojp2.administrative_area_versioned_ref_structure import (
    AdministrativeAreaVersionedRefStructure,
)

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class AdministrativeAreaRefsStructure:
    """
    Type for a collection of one or more references to ADMINISTRATIVE ZONEs.

    :ivar administrative_area_ref: Reference to the identifier of an
        ADMINISTRATIVE ZONE.
    """

    administrative_area_ref: list[AdministrativeAreaVersionedRefStructure] = (
        field(
            default_factory=list,
            metadata={
                "name": "AdministrativeAreaRef",
                "type": "Element",
                "namespace": "http://www.ifopt.org.uk/ifopt",
                "min_occurs": 1,
            },
        )
    )
