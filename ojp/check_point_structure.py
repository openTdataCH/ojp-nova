from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration
from ojp.accessibility_feature_enumeration import AccessibilityFeatureEnumeration
from ojp.check_point_process_enumeration import CheckPointProcessEnumeration
from ojp.check_point_service_enumeration import CheckPointServiceEnumeration
from ojp.congestion_enumeration import CongestionEnumeration
from ojp.validity_condition_structure import ValidityConditionStructure

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class CheckPointStructure:
    """
    Type for a CHECK CONSTRAINT Hazard that can be associated with.

    :ivar check_point_id: Identifier of CHECK CONSTRAINt.
    :ivar validity_condition: Validty condition governing applicability
        of CHECK CONSTRAINT.
    :ivar check_point_process: Type of process that may occur at CHECK
        CONSTRAINt.
    :ivar check_point_service: Type of process that may occur at CHECK
        CONSTRAINt.
    :ivar access_feature_type: Type of physical featrue that may slow
        use of CHECK CONSTRAINt.
    :ivar congestion: Type of crowding that may slow use of CHECK
        CONSTRAINt.
    :ivar facility_ref: Classification of feature of CHECK CONSTRAINT.
    :ivar minimum_likely_delay: Minimum duration needed to pass through
        CHECK CONSTRAINT.
    :ivar average_delay: Average duration expected to pass through CHECK
        CONSTRAINT.
    :ivar maximum_likely_delay: Maximum duration expected to pass
        through CHECK CONSTRAINT.
    """
    check_point_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CheckPointId",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        }
    )
    validity_condition: Optional[ValidityConditionStructure] = field(
        default=None,
        metadata={
            "name": "ValidityCondition",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        }
    )
    check_point_process: Optional[CheckPointProcessEnumeration] = field(
        default=None,
        metadata={
            "name": "CheckPointProcess",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        }
    )
    check_point_service: Optional[CheckPointServiceEnumeration] = field(
        default=None,
        metadata={
            "name": "CheckPointService",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        }
    )
    access_feature_type: Optional[AccessibilityFeatureEnumeration] = field(
        default=None,
        metadata={
            "name": "AccessFeatureType",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        }
    )
    congestion: Optional[CongestionEnumeration] = field(
        default=None,
        metadata={
            "name": "Congestion",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        }
    )
    facility_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "FacilityRef",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        }
    )
    minimum_likely_delay: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MinimumLikelyDelay",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        }
    )
    average_delay: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "AverageDelay",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        }
    )
    maximum_likely_delay: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumLikelyDelay",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        }
    )
