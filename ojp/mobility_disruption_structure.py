from dataclasses import dataclass, field
from typing import List, Optional
from ojp.access_facility_enumeration import AccessFacilityEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class MobilityDisruptionStructure:
    """
    Type for effect of EQUIPMENT availability change on impaired access users.

    :ivar mobility_impaired_access: Whether stop or service is
        accessible to mobility impaired users. This may be further
        qualified by one ore more MobilityFacility instances to specify
        which types of mobility access are available (true) or not
        available (false). For example suitableForWheelChair, or
        'tepFreeAccess.
    :ivar access_facility: Classification of Mobility Facility type -
        Based on Tpeg pti23.
    """
    mobility_impaired_access: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MobilityImpairedAccess",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    access_facility: List[AccessFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "AccessFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
