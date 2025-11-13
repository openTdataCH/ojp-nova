from dataclasses import dataclass, field
from typing import Optional

from ojp2.compound_train_ref import CompoundTrainRef
from ojp2.entrance_to_vehicle_ref import EntranceToVehicleRef
from ojp2.stop_assignment_structure import StopAssignmentStructure
from ojp2.train_component_ref import TrainComponentRef
from ojp2.train_element_ref import TrainElementRef
from ojp2.train_in_compound_train_ref import TrainInCompoundTrainRef
from ojp2.train_ref import TrainRef
from ojp2.vehicle_in_formation_status_structure import (
    VehicleInFormationStatusStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class FormationAssignmentStructure:
    """Assignment of the arrival/departure of a VEHICLE within a formation, e.g.
    carriage in a TRAIN composition, to a physical QUAY or nested QUAY (i.e.
    platform or sector of a platform).

    (since SIRI 2.1)

    :ivar compound_train_ref:
    :ivar train_ref:
    :ivar train_in_compound_train_ref:
    :ivar train_element_ref:
    :ivar train_component_ref:
    :ivar entrance_to_vehicle_ref:
    :ivar vehicle_in_formation_status: Information about a change of a
        VEHICLE within the formation, e.g., whether a VEHICLE is open,
        booked or has defective doors.
    :ivar train_stop_assignment: References to the QUAY on which the
        particular VEHICLE, i.e., component of the formation, arrives or
        departs from. If a QUAY is divided into sub-QUAYs or sectors
        (with the help of STOP ASSIGNMENTs), and a TRAIN COMPONENT spans
        over multiple sectors of the QUAY, the FORMATION ASSIGNMENT must
        reference all of them (in multiple STOP ASSIGNMENTs).
    """

    compound_train_ref: Optional[CompoundTrainRef] = field(
        default=None,
        metadata={
            "name": "CompoundTrainRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    train_ref: Optional[TrainRef] = field(
        default=None,
        metadata={
            "name": "TrainRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    train_in_compound_train_ref: Optional[TrainInCompoundTrainRef] = field(
        default=None,
        metadata={
            "name": "TrainInCompoundTrainRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    train_element_ref: Optional[TrainElementRef] = field(
        default=None,
        metadata={
            "name": "TrainElementRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    train_component_ref: Optional[TrainComponentRef] = field(
        default=None,
        metadata={
            "name": "TrainComponentRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    entrance_to_vehicle_ref: Optional[EntranceToVehicleRef] = field(
        default=None,
        metadata={
            "name": "EntranceToVehicleRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_in_formation_status: Optional[
        VehicleInFormationStatusStructure
    ] = field(
        default=None,
        metadata={
            "name": "VehicleInFormationStatus",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    train_stop_assignment: list[StopAssignmentStructure] = field(
        default_factory=list,
        metadata={
            "name": "TrainStopAssignment",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
