from dataclasses import dataclass, field
from typing import Optional

from ojp2.compound_train_ref import CompoundTrainRef
from ojp2.entrance_to_vehicle_ref import EntranceToVehicleRef
from ojp2.extensions_2 import Extensions2
from ojp2.formation_status_structure import FormationStatusStructure
from ojp2.recommended_action_structure import RecommendedActionStructure
from ojp2.situation_ref import SituationRef
from ojp2.train_component_ref import TrainComponentRef
from ojp2.train_element_ref import TrainElementRef
from ojp2.train_in_compound_train_ref import TrainInCompoundTrainRef
from ojp2.train_ref import TrainRef
from ojp2.vehicle_in_formation_status_structure import (
    VehicleInFormationStatusStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class FormationConditionStructure:
    """Type for FORMATION CONDITION.

    (since SIRI 2.1)

    :ivar compound_train_ref:
    :ivar train_ref:
    :ivar train_in_compound_train_ref:
    :ivar train_element_ref:
    :ivar train_component_ref:
    :ivar entrance_to_vehicle_ref:
    :ivar formation_status: Status of formation, e.g., whether it has
        changed compared to the plan, certain VEHICLEs or features are
        missing or extra VEHICLEs are added.
    :ivar vehicle_in_formation_status: Status of a VEHICLE within
        formation, e.g., whether a VEHICLE is open, booked or has
        defective doors.
    :ivar situation_ref:
    :ivar recommended_action: Information on recommendations for
        passengers on how to deal with the formation change.
    :ivar extensions:
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
    formation_status: Optional[FormationStatusStructure] = field(
        default=None,
        metadata={
            "name": "FormationStatus",
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
    situation_ref: Optional[SituationRef] = field(
        default=None,
        metadata={
            "name": "SituationRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    recommended_action: Optional[RecommendedActionStructure] = field(
        default=None,
        metadata={
            "name": "RecommendedAction",
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
