from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class PlacesEnum(Enum):
    AROUND_BENDS_IN_THE_ROAD = "aroundBendsInTheRoad"
    AT_CUSTOMS_POSTS = "atCustomsPosts"
    AT_HIGH_ALTITUDES = "atHighAltitudes"
    AT_TOLL_PLAZAS = "atTollPlazas"
    IN_GALLERIES = "inGalleries"
    IN_LOW_LYING_AREAS = "inLowLyingAreas"
    IN_ROADWORKS_AREAS = "inRoadworksAreas"
    IN_SHADED_AREAS = "inShadedAreas"
    IN_THE_CITY_CENTRE = "inTheCityCentre"
    IN_THE_INNER_CITY_AREAS = "inTheInnerCityAreas"
    IN_TUNNELS = "inTunnels"
    ON_BRIDGES = "onBridges"
    ON_ELEVATED_SECTIONS = "onElevatedSections"
    ON_ENTERING_OR_LEAVING_TUNNELS = "onEnteringOrLeavingTunnels"
    ON_ENTERING_THE_COUNTRY = "onEnteringTheCountry"
    ON_FLYOVERS = "onFlyovers"
    ON_LEAVING_THE_COUNTRY = "onLeavingTheCountry"
    ON_MOTORWAYS = "onMotorways"
    ON_NON_MOTORWAYS = "onNonMotorways"
    ON_ROUNDABOUTS = "onRoundabouts"
    ON_SLIP_ROADS = "onSlipRoads"
    ON_UNDERGROUND_SECTIONS = "onUndergroundSections"
    ON_UNDERPASSES = "onUnderpasses"
    OVER_THE_CREST_OF_HILLS = "overTheCrestOfHills"
    OTHER = "other"
