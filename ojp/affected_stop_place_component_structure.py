from dataclasses import dataclass, field
from typing import List, Optional
from ojp.accessibility_feature_enumeration import AccessibilityFeatureEnumeration
from ojp.affected_facility_structure import AffectedFacilityStructure
from ojp.affected_stop_place_element_structure import AffectedStopPlaceElementStructure
from ojp.extensions_1 import Extensions1
from ojp.link_projection import LinkProjection
from ojp.natural_language_string_structure import NaturalLanguageStringStructure
from ojp.offset_structure import OffsetStructure
from ojp.point_projection import PointProjection
from ojp.stop_place_component_type_enumeration import StopPlaceComponentTypeEnumeration
from ojp.zone_projection import ZoneProjection

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AffectedStopPlaceComponentStructure(AffectedStopPlaceElementStructure):
    """
    Type for information about the quays affected by an SITUATION.

    :ivar component_ref: Reference to a Stop Place.
    :ivar component_name: Name of component.  (Unbounded since SIRI 2.0)
    :ivar component_type: Type of Component.
    :ivar point_projection:
    :ivar link_projection:
    :ivar zone_projection:
    :ivar offset: Further qualifcation of affected part of Link
        projection,
    :ivar access_feature_type: Type of AccessFeature  (+SIRI.20)
    :ivar affected_facilities: Facilities available for component
        (+SIRI 2.0)
    :ivar extensions:
    """
    component_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ComponentRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    component_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "ComponentName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    component_type: Optional[StopPlaceComponentTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "ComponentType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    point_projection: Optional[PointProjection] = field(
        default=None,
        metadata={
            "name": "PointProjection",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        }
    )
    link_projection: Optional[LinkProjection] = field(
        default=None,
        metadata={
            "name": "LinkProjection",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        }
    )
    zone_projection: Optional[ZoneProjection] = field(
        default=None,
        metadata={
            "name": "ZoneProjection",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        }
    )
    offset: Optional[OffsetStructure] = field(
        default=None,
        metadata={
            "name": "Offset",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    access_feature_type: Optional[AccessibilityFeatureEnumeration] = field(
        default=None,
        metadata={
            "name": "AccessFeatureType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    affected_facilities: Optional["AffectedStopPlaceComponentStructure.AffectedFacilities"] = field(
        default=None,
        metadata={
            "name": "AffectedFacilities",
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
