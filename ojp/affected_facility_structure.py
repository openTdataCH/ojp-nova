from dataclasses import dataclass, field
from typing import List, Optional
from ojp.extensions_1 import Extensions1
from ojp.facility_status_enumeration import FacilityStatusEnumeration
from ojp.natural_language_string_structure import NaturalLanguageStringStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AffectedFacilityStructure:
    """Type for information about a FACILITY affected by an SITUATION.

    (+SIRI 2.0)

    :ivar facility_ref:
    :ivar start_stop_point_ref: Identifier of stop point at which
        availability first applies.
    :ivar end_stop_point_ref: Identifier of stop point at which
        availability last applies.
    :ivar facility_name: Name of FACILITY.
    :ivar facility_status: Status of Facility
    :ivar extensions:
    """
    facility_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "FacilityRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    start_stop_point_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "StartStopPointRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    end_stop_point_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "EndStopPointRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    facility_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "FacilityName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    facility_status: List[FacilityStatusEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "FacilityStatus",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    extensions: List[Extensions1] = field(
        default_factory=list,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
