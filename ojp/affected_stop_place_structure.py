from dataclasses import dataclass, field
from typing import List, Optional
from ojp.affected_facility_structure import AffectedFacilityStructure
from ojp.affected_stop_place_component_structure import AffectedStopPlaceComponentStructure
from ojp.affected_stop_place_element_structure import AffectedStopPlaceElementStructure
from ojp.extensions_1 import Extensions1
from ojp.natural_language_string_structure import NaturalLanguageStringStructure
from ojp.stop_place_type_enumeration import StopPlaceTypeEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AffectedStopPlaceStructure(AffectedStopPlaceElementStructure):
    """
    Type for information about the Stop Places affected by an SITUATION.

    :ivar stop_place_ref: Stop Place affected by SITUATION.
    :ivar place_name: Name of stop place.  (Unbounded since SIRI 2.0)
    :ivar stop_place_type: Type of Stop Place.
    :ivar affected_facilities: Facilities available for VEHICLE JOURNEY
        (+SIRI 2.0)
    :ivar affected_components: Quays affected by SITUATION.
    :ivar affected_navigation_paths: PathLinks affected by SITUATION.
    :ivar extensions:
    """
    stop_place_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "StopPlaceRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    place_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "PlaceName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    stop_place_type: Optional[StopPlaceTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "StopPlaceType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    affected_facilities: Optional["AffectedStopPlaceStructure.AffectedFacilities"] = field(
        default=None,
        metadata={
            "name": "AffectedFacilities",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    affected_components: Optional["AffectedStopPlaceStructure.AffectedComponents"] = field(
        default=None,
        metadata={
            "name": "AffectedComponents",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    affected_navigation_paths: Optional["AffectedStopPlaceStructure.AffectedNavigationPaths"] = field(
        default=None,
        metadata={
            "name": "AffectedNavigationPaths",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )

    @dataclass
    class AffectedFacilities:
        """
        :ivar affected_facility: Facililitiy available for VEHICLE
            JOURNEY   (+SIRI 2.0)
        """
        affected_facility: List[AffectedFacilityStructure] = field(
            default_factory=list,
            metadata={
                "name": "AffectedFacility",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            }
        )

    @dataclass
    class AffectedComponents:
        """
        :ivar affected_component: Quay affected by SITUATION.
        """
        affected_component: List[AffectedStopPlaceComponentStructure] = field(
            default_factory=list,
            metadata={
                "name": "AffectedComponent",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            }
        )

    @dataclass
    class AffectedNavigationPaths:
        navigation_path_ref: List[str] = field(
            default_factory=list,
            metadata={
                "name": "NavigationPathRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            }
        )
