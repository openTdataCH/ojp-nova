from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class TpegLoc03AreaDescriptorSubtypeEnum(Enum):
    ADMINISTRATIVE_AREA_NAME = "administrativeAreaName"
    ADMINISTRATIVE_REFERENCE_NAME = "administrativeReferenceName"
    AREA_NAME = "areaName"
    COUNTY_NAME = "countyName"
    LAKE_NAME = "lakeName"
    NATION_NAME = "nationName"
    POLICE_FORCE_CONTROL_AREA_NAME = "policeForceControlAreaName"
    REGION_NAME = "regionName"
    SEA_NAME = "seaName"
    TOWN_NAME = "townName"
    OTHER = "other"
