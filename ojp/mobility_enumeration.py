from enum import Enum

__NAMESPACE__ = "http://www.ifopt.org.uk/acsb"


class MobilityEnumeration(Enum):
    """
    Identification of mobility USER NEEDs.
    """
    WHEELCHAIR = "wheelchair"
    ASSISTED_WHEELCHAIR = "assistedWheelchair"
    MOTORIZED_WHEELCHAIR = "motorizedWheelchair"
    WALKING_FRAME = "walkingFrame"
    RESTRICTED_MOBILITY = "restrictedMobility"
    OTHER_MOBILITY_NEED = "otherMobilityNeed"
