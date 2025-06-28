from dataclasses import dataclass, field
from typing import Optional

from ojp2.geo_restrictions_structure import GeoRestrictionsStructure
from ojp2.location_structure import LocationStructure
from ojp2.participant_ref_structure import ParticipantRefStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class InitialLocationInputStructure:
    """
    :ivar name: Name of the LOCATION object which is looked for. This is
        usually the user's input. If not given, the name of the
        resulting location objects is not relevant.
    :ivar geo_position: Coordinate where to look for locations/places.
        If given, the result should prefer locations/place objects near
        to this GeoPosition.
    :ivar geo_restriction: Restricts the resulting location/place
        objects to the given geographical area.
    :ivar allowed_system: Used in distributed environments. e.g., EU-
        Spirit. If none is given, the location/place information request
        refers to all known systems (in EU-Spirit "passive servers"). If
        at least one is given, the location/place information request
        refers only to the given systems (in EU-Spirit "passive
        servers"). In EU-Spirit the system IDs were previously called
        "provider code". See https://eu-spirit.eu/
    """

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    geo_position: Optional[LocationStructure] = field(
        default=None,
        metadata={
            "name": "GeoPosition",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    geo_restriction: Optional[GeoRestrictionsStructure] = field(
        default=None,
        metadata={
            "name": "GeoRestriction",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    allowed_system: list[ParticipantRefStructure] = field(
        default_factory=list,
        metadata={
            "name": "AllowedSystem",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
