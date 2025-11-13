from dataclasses import dataclass, field
from typing import Optional

from ojp2.equipment_availability_structure import (
    EquipmentAvailabilityStructure,
)
from ojp2.mobility_disruption_structure import MobilityDisruptionStructure
from ojp2.situation_ref import SituationRef

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class FacilityChangeStructure:
    """Type for change to equipment availability.

    Basic structure defined in the first 1.0 SIRI XSd.

    :ivar equipment_availability: Availability change for Equipment
        item.
    :ivar situation_ref:
    :ivar mobility_disruption: Effect of change on impaired access
        users.
    """

    equipment_availability: Optional[EquipmentAvailabilityStructure] = field(
        default=None,
        metadata={
            "name": "EquipmentAvailability",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    situation_ref: Optional[SituationRef] = field(
        default=None,
        metadata={
            "name": "SituationRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    mobility_disruption: Optional[MobilityDisruptionStructure] = field(
        default=None,
        metadata={
            "name": "MobilityDisruption",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
