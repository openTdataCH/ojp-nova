from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class RoadsideServiceDisruptionTypeEnum(Enum):
    BAR_CLOSED = "barClosed"
    DIESEL_SHORTAGE = "dieselShortage"
    FUEL_SHORTAGE = "fuelShortage"
    LPG_SHORTAGE = "lpgShortage"
    METHANE_SHORTAGE = "methaneShortage"
    NO_DIESEL_FOR_HEAVY_VEHICLES = "noDieselForHeavyVehicles"
    NO_DIESEL_FOR_LIGHT_VEHICLES = "noDieselForLightVehicles"
    NO_PUBLIC_TELEPHONES = "noPublicTelephones"
    NO_TOILET_FACILITIES = "noToiletFacilities"
    NO_VEHICLE_REPAIR_FACILITIES = "noVehicleRepairFacilities"
    PETROL_SHORTAGE = "petrolShortage"
    REST_AREA_BUSY = "restAreaBusy"
    REST_AREA_CLOSED = "restAreaClosed"
    REST_AREA_OVERCROWDED_DRIVE_TO_ANOTHER_REST_AREA = "restAreaOvercrowdedDriveToAnotherRestArea"
    SERVICE_AREA_BUSY = "serviceAreaBusy"
    SERVICE_AREA_CLOSED = "serviceAreaClosed"
    SERVICE_AREA_FUEL_STATION_CLOSED = "serviceAreaFuelStationClosed"
    SERVICE_AREA_OVERCROWDED_DRIVE_TO_ANOTHER_SERVICE_AREA = "serviceAreaOvercrowdedDriveToAnotherServiceArea"
    SERVICE_AREA_RESTAURANT_CLOSED = "serviceAreaRestaurantClosed"
    SOME_COMMERCIAL_SERVICES_CLOSED = "someCommercialServicesClosed"
    WATER_SHORTAGE = "waterShortage"
