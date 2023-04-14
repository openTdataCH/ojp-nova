from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class RoadsideAssistanceTypeEnum(Enum):
    AIR_AMBULANCE = "airAmbulance"
    BUS_PASSENGER_ASSISTANCE = "busPassengerAssistance"
    EMERGENCY_SERVICES = "emergencyServices"
    FIRST_AID = "firstAid"
    FOOD_DELIVERY = "foodDelivery"
    HELICOPTER_RESCUE = "helicopterRescue"
    VEHICLE_REPAIR = "vehicleRepair"
    VEHICLE_RECOVERY = "vehicleRecovery"
    OTHER = "other"
