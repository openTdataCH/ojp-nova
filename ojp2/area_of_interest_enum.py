from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class AreaOfInterestEnum(Enum):
    CONTINENT_WIDE = "continentWide"
    NATIONAL = "national"
    NEIGHBOURING_COUNTRIES = "neighbouringCountries"
    NOT_SPECIFIED = "notSpecified"
    REGIONAL = "regional"
