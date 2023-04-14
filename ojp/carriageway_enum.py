from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class CarriagewayEnum(Enum):
    CONNECTING_CARRIAGEWAY = "connectingCarriageway"
    ENTRY_SLIP_ROAD = "entrySlipRoad"
    EXIT_SLIP_ROAD = "exitSlipRoad"
    FLYOVER = "flyover"
    LEFT_HAND_FEEDER_ROAD = "leftHandFeederRoad"
    LEFT_HAND_PARALLEL_CARRIAGEWAY = "leftHandParallelCarriageway"
    MAIN_CARRIAGEWAY = "mainCarriageway"
    OPPOSITE_CARRIAGEWAY = "oppositeCarriageway"
    PARALLEL_CARRIAGEWAY = "parallelCarriageway"
    RIGHT_HAND_FEEDER_ROAD = "rightHandFeederRoad"
    RIGHT_HAND_PARALLEL_CARRIAGEWAY = "rightHandParallelCarriageway"
    SERVICE_ROAD = "serviceRoad"
    SLIP_ROADS = "slipRoads"
    UNDERPASS = "underpass"
