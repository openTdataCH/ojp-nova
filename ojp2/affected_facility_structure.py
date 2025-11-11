from dataclasses import dataclass, field
from typing import Optional

from ojp2.extensions_2 import Extensions2
from ojp2.facility_ref import FacilityRef
from ojp2.facility_status_enumeration import FacilityStatusEnumeration
from ojp2.natural_language_string_structure import (
    NaturalLanguageStringStructure,
)
from ojp2.stop_point_ref_structure import StopPointRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AffectedFacilityStructure:
    """Type for information about a FACILITY affected by an SITUATION.

    (since SIRI 2.0)

    :ivar facility_ref:
    :ivar start_stop_point_ref: Identifier of stop point at which
        availability first applies.
    :ivar end_stop_point_ref: Identifier of stop point at which
        availability last applies.
    :ivar facility_name: Name of FACILITY.
    :ivar facility_status: Status of Facility
    :ivar extensions:
    """

    facility_ref: Optional[FacilityRef] = field(
        default=None,
        metadata={
            "name": "FacilityRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    start_stop_point_ref: Optional[StopPointRefStructure] = field(
        default=None,
        metadata={
            "name": "StartStopPointRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    end_stop_point_ref: Optional[StopPointRefStructure] = field(
        default=None,
        metadata={
            "name": "EndStopPointRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    facility_name: list[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "FacilityName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    facility_status: list[FacilityStatusEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "FacilityStatus",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    extensions: list[Extensions2] = field(
        default_factory=list,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
