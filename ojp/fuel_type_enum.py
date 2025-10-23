from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class FuelTypeEnum(Enum):
    BATTERY = "battery"
    BIODIESEL = "biodiesel"
    DIESEL = "diesel"
    DIESEL_BATTERY_HYBRID = "dieselBatteryHybrid"
    ETHANOL = "ethanol"
    HYDROGEN = "hydrogen"
    LIQUID_GAS = "liquidGas"
    LPG = "lpg"
    METHANE = "methane"
    PETROL = "petrol"
    PETROL_BATTERY_HYBRID = "petrolBatteryHybrid"
