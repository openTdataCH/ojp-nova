from dataclasses import dataclass, field
from typing import Optional

from ojp2.administrative_area_ref_structure import (
    AdministrativeAreaRefStructure,
)
from ojp2.info_links_structure import InfoLinksStructure
from ojp2.versioned_object_structure import VersionedObjectStructure

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class DataManagedObjectStructure(VersionedObjectStructure):
    """
    Abstract Type for DATA MANAGED OBJECT, that is an object that may be assigned a
    RESPONSIBILITY SET dictating a responsible ORGANISATION and/or ADMINISTRATIVE
    ZONE.

    :ivar managed_by_area_ref: ADMINISTRATIVE ZONEthat manages object.
        If absent then manager same as for containing parent of object.
    :ivar info_links: Collection of URL's associated with object.
    """

    managed_by_area_ref: Optional[AdministrativeAreaRefStructure] = field(
        default=None,
        metadata={
            "name": "ManagedByAreaRef",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )
    info_links: Optional[InfoLinksStructure] = field(
        default=None,
        metadata={
            "name": "InfoLinks",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )
