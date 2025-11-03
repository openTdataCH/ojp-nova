from dataclasses import dataclass, field
from typing import Optional

from ojp2.accessibility_feature_enumeration_2 import (
    AccessibilityFeatureEnumeration2,
)
from ojp2.affected_facility_structure import AffectedFacilityStructure
from ojp2.affected_stop_place_element_structure import (
    AffectedStopPlaceElementStructure,
)
from ojp2.extensions_2 import Extensions2
from ojp2.link_projection import LinkProjection
from ojp2.natural_language_string_structure import (
    NaturalLanguageStringStructure,
)
from ojp2.offset_structure import OffsetStructure
from ojp2.point_projection import PointProjection
from ojp2.stop_place_component_ref_structure import (
    StopPlaceComponentRefStructure,
)
from ojp2.stop_place_component_type_enumeration import (
    StopPlaceComponentTypeEnumeration,
)
from ojp2.zone_projection import ZoneProjection

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AffectedStopPlaceComponentStructure(AffectedStopPlaceElementStructure):
    """
    Type for information about the quays affected by an SITUATION.

    :ivar component_ref: Reference to a STOP PLACE.
    :ivar component_name: Name of component.  (Unbounded since SIRI 2.0)
    :ivar component_type: Type of Component.
    :ivar point_projection:
    :ivar link_projection:
    :ivar zone_projection:
    :ivar offset: Further qualifcation of affected part of Link
        projection,
    :ivar access_feature_type: Type of AccessFeature  (+SIRI.20)
    :ivar affected_facilities: Facilities available for component
        (since SIRI 2.0)
    :ivar extensions:
    """

    component_ref: Optional[StopPlaceComponentRefStructure] = field(
        default=None,
        metadata={
            "name": "ComponentRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    component_name: list[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "ComponentName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    component_type: Optional[StopPlaceComponentTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "ComponentType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    point_projection: Optional[PointProjection] = field(
        default=None,
        metadata={
            "name": "PointProjection",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )
    link_projection: Optional[LinkProjection] = field(
        default=None,
        metadata={
            "name": "LinkProjection",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )
    zone_projection: Optional[ZoneProjection] = field(
        default=None,
        metadata={
            "name": "ZoneProjection",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )
    offset: Optional[OffsetStructure] = field(
        default=None,
        metadata={
            "name": "Offset",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    access_feature_type: Optional[AccessibilityFeatureEnumeration2] = field(
        default=None,
        metadata={
            "name": "AccessFeatureType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    affected_facilities: Optional[
        "AffectedStopPlaceComponentStructure.AffectedFacilities"
    ] = field(
        default=None,
        metadata={
            "name": "AffectedFacilities",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    extensions: Optional[Extensions2] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )

    @dataclass
    class AffectedFacilities:
        """
        :ivar affected_facility: Facility available for VEHICLE JOURNEY
            (since SIRI 2.0)
        """

        affected_facility: list[AffectedFacilityStructure] = field(
            default_factory=list,
            metadata={
                "name": "AffectedFacility",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )
