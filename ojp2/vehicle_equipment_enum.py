from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class VehicleEquipmentEnum(Enum):
    NOT_USING_SNOW_CHAINS = "notUsingSnowChains"
    NOT_USING_SNOW_CHAINS_OR_TYRES = "notUsingSnowChainsOrTyres"
    SNOW_CHAINS_IN_USE = "snowChainsInUse"
    SNOW_TYRES_IN_USE = "snowTyresInUse"
    SNOW_CHAINS_OR_TYRES_IN_USE = "snowChainsOrTyresInUse"
    WITHOUT_SNOW_TYRES_OR_CHAINS_ON_BOARD = "withoutSnowTyresOrChainsOnBoard"
