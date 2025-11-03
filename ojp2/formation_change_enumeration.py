from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class FormationChangeEnumeration(Enum):
    """Allowed values for FORMATION CHANGE CODE.

    (since SIRI 2.1)
    """

    CHANGED_FORMATION = "changedFormation"
    REVERSED_FORMATION = "reversedFormation"
    MISSING_VEHICLES = "missingVehicles"
    EXTRA_VEHICLES = "extraVehicles"
    MISSING_TRAIN_IN_COMPOUND_TRAIN = "missingTrainInCompoundTrain"
    EXTRA_TRAIN_IN_COMPOUND_TRAIN = "extraTrainInCompoundTrain"
    MISSING_FAMILY_COACH = "missingFamilyCoach"
    MISSING_THROUGH_COACH = "missingThroughCoach"
    MISSING_LOW_FLOOR_COACH = "missingLowFloorCoach"
    MISSING_RESTAURANT_COACH = "missingRestaurantCoach"
    MISSING_WHEELCHAIR_SPACES = "missingWheelchairSpaces"
