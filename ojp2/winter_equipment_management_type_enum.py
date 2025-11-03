from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class WinterEquipmentManagementTypeEnum(Enum):
    DO_NO_USE_STUD_TYRES = "doNoUseStudTyres"
    USE_SNOW_CHAINS = "useSnowChains"
    USE_SNOW_CHAINS_OR_TYRES = "useSnowChainsOrTyres"
    USE_SNOW_TYRES = "useSnowTyres"
    WINTER_EQUIPMENT_ON_BOARD_REQUIRED = "winterEquipmentOnBoardRequired"
    OTHER = "other"
