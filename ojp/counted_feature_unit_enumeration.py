from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class CountedFeatureUnitEnumeration(Enum):
    """Allowed values for units of what is counted
    bay: parking bay for cars, bicycle, scooter, etc
    otherSpaces: any other kind of spaces: lockers, standing spaces, toilets, etc.
    devices: electronic devices (audio guide, headphones, etc.) and physical devices (walking stick, wheelchair, etc.)
    vehicles: any type of vehicles (cycle, car, scooter, hoverboard, motorbike, etc.)
    kW (kiloWatt) or kWh (kiloWatt-hour): means that an available or consumed power is measured
    mAh (milliAmpere per hour): typically used for battery charging level
    litres and cubicMeters: means that a volume is measured
    squareMeters: means that a surface is measured
    meters: means that a distance is measured
    kg (kilogram): means that a mass is measured
    A (Ampere): means that an electric current is measured
    C (degree Celsius): means that a temperature is measured
    other: use of "other" requires the additional open ended TypeOfCountedFeature (monitoredCountingStructure) to be filled"""
    BAYS = "bays"
    SEATS = "seats"
    OTHER_SPACES = "otherSpaces"
    DEVICES = "devices"
    VEHICLES = "vehicles"
    PERSONS = "persons"
    LITRES = "litres"
    SQUARE_METERS = "squareMeters"
    CUBIC_METERS = "cubicMeters"
    METERS = "meters"
    K_WH = "kWh"
    M_AH = "mAh"
    K_W = "kW"
    KG = "kg"
    A = "A"
    C = "C"
    OTHER = "other"
