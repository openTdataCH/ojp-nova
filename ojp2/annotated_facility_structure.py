from dataclasses import dataclass, field
from typing import Optional

from ojp2.facility_ref import FacilityRef
from ojp2.facility_structure import FacilityStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AnnotatedFacilityStructure:
    """Summary information about Facility.

    Used in DISCOVERY.

    :ivar facility_ref:
    :ivar monitored: Whether real-time data is available for the stop.
        Default is 'true'.
    :ivar facility: Description of the facility (without its status)
    """

    facility_ref: Optional[FacilityRef] = field(
        default=None,
        metadata={
            "name": "FacilityRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    monitored: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Monitored",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    facility: Optional[FacilityStructure] = field(
        default=None,
        metadata={
            "name": "Facility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
