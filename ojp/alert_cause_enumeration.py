from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class AlertCauseEnumeration(Enum):
    """Values for TPEG Pts38 - AlertCause, plus additional values from TPEG Pti19/20/21/22

    :cvar UNKNOWN: TPEG Pts38_0, unknown
    :cvar SECURITY_ALERT: TPEG Pts38_1, security alert
    :cvar EMERGENCY_SERVICES_CALL: TPEG Pts38_2, emergency services call
    :cvar POLICE_ACTIVITY: TPEG Pts38_3, police activity
    :cvar POLICE_ORDER: TPEG Pts38_4, police order
    :cvar FIRE: TPEG Pts38_5, fire
    :cvar CABLE_FIRE: TPEG Pts38_6, cable fire
    :cvar SMOKE_DETECTED_ON_VEHICLE: TPEG Pts38_7, smoke detected on
        vehicle
    :cvar FIRE_AT_STATION: TPEG Pts38_8, fire at the station
    :cvar FIRE_RUN: TPEG Pts38_9, fire run
    :cvar FIRE_BRIGADE_ORDER: TPEG Pts38_10, fire brigade order
    :cvar EXPLOSION: TPEG Pts38_11, explosion
    :cvar EXPLOSION_HAZARD: TPEG Pts38_12, explosion hazard
    :cvar BOMB_DISPOSAL: TPEG Pts38_13, bomb disposal
    :cvar EMERGENCY_MEDICAL_SERVICES: TPEG Pts38_14, emergency medical
        services
    :cvar EMERGENCY_BRAKE: TPEG Pts38_15, emergency brake
    :cvar VANDALISM: TPEG Pts38_16, vandalism
    :cvar CABLE_THEFT: TPEG Pts38_17, cable theft
    :cvar SIGNAL_PASSED_AT_DANGER: TPEG Pts38_18, signal passed at
        danger
    :cvar STATION_OVERRUN: TPEG Pts38_19, station overrun
    :cvar PASSENGERS_BLOCKING_DOORS: TPEG Pts38_20, passengers blocking
        doors
    :cvar DEFECTIVE_SECURITY_SYSTEM: TPEG Pts38_21, defective security
        system
    :cvar OVERCROWDED: TPEG Pts38_22, overcrowded
    :cvar BORDER_CONTROL: TPEG Pts38_23, border control
    :cvar UNATTENDED_BAG: TPEG Pts38_24, unattended bag
    :cvar TELEPHONED_THREAT: TPEG Pts38_25, telephoned threat
    :cvar SUSPECT_VEHICLE: TPEG Pts38_26, suspect vehicle
    :cvar EVACUATION: TPEG Pts38_27, evacuation
    :cvar TERRORIST_INCIDENT: TPEG Pts38_28, terrorist incident
    :cvar PUBLIC_DISTURBANCE: TPEG Pts38_29, public disturbance
    :cvar TECHNICAL_PROBLEM: TPEG Pts38_30, technical problem
    :cvar VEHICLE_FAILURE: TPEG Pts38_31, vehicle failure
    :cvar SERVICE_DISRUPTION: TPEG Pts38_32, service disruption
    :cvar DOOR_FAILURE: TPEG Pts38_33, door failure
    :cvar LIGHTING_FAILURE: TPEG Pts38_34, lighting failure
    :cvar POINTS_PROBLEM: TPEG Pts38_35, points problem
    :cvar POINTS_FAILURE: TPEG Pts38_36, points failure
    :cvar SIGNAL_PROBLEM: TPEG Pts38_37, signal problem
    :cvar SIGNAL_FAILURE: TPEG Pts38_38, signal failure
    :cvar OVERHEAD_WIRE_FAILURE: TPEG Pts38_39, overhead wire failure
    :cvar LEVEL_CROSSING_FAILURE: TPEG Pts38_40, level crossing failure
    :cvar TRAFFIC_MANAGEMENT_SYSTEM_FAILURE: TPEG Pts38_41, traffic
        management system failure
    :cvar ENGINE_FAILURE: TPEG Pts38_42, engine failure
    :cvar BREAK_DOWN: TPEG Pts38_43, break down
    :cvar REPAIR_WORK: TPEG Pts38_44, repair work
    :cvar CONSTRUCTION_WORK: TPEG Pts38_45, construction work
    :cvar MAINTENANCE_WORK: TPEG Pts38_46, maintenance work
    :cvar POWER_PROBLEM: TPEG Pts38_47, power problem
    :cvar TRACK_CIRCUIT_PROBLEM: TPEG Pts38_48, track circuit
    :cvar SWING_BRIDGE_FAILURE: TPEG Pts38_49, swing bridge failure
    :cvar ESCALATOR_FAILURE: TPEG Pts38_50, escalator failure
    :cvar LIFT_FAILURE: TPEG Pts38_51, lift failure
    :cvar GANGWAY_PROBLEM: TPEG Pts38_52, gangway problem
    :cvar DEFECTIVE_VEHICLE: TPEG Pts38_53, defective vehicle
    :cvar BROKEN_RAIL: TPEG Pts38_54, broken rail
    :cvar POOR_RAIL_CONDITIONS: TPEG Pts38_55, poor rail conditions
    :cvar DEICING_WORK: TPEG Pts38_56, de-icing work
    :cvar WHEEL_PROBLEM: TPEG Pts38_57, wheel problem
    :cvar ROUTE_BLOCKAGE: TPEG Pts38_58, route blockage
    :cvar CONGESTION: TPEG Pts38_59, congestion
    :cvar HEAVY_TRAFFIC: TPEG Pts38_60, heavy traffic
    :cvar ROUTE_DIVERSION: TPEG Pts38_61, route diversion
    :cvar ROADWORKS: TPEG Pts38_62, roadworks
    :cvar UNSCHEDULED_CONSTRUCTION_WORK: TPEG Pts38_63, unscheduled
        construction work
    :cvar LEVEL_CROSSING_INCIDENT: TPEG Pts38_64, level crossing
        incident
    :cvar SEWERAGE_MAINTENANCE: TPEG Pts38_65, sewerageMaintenance
    :cvar ROAD_CLOSED: TPEG Pts38_66, road closed
    :cvar ROADWAY_DAMAGE: TPEG Pts38_67, roadway damage
    :cvar BRIDGE_DAMAGE: TPEG Pts38_68, bridge damage
    :cvar PERSON_ON_THE_LINE: TPEG Pts38_69, person on the line
    :cvar OBJECT_ON_THE_LINE: TPEG Pts38_70, object on the line
    :cvar VEHICLE_ON_THE_LINE: TPEG Pts38_71, vehicle on the line
    :cvar ANIMAL_ON_THE_LINE: TPEG Pts38_72, animal on the line
    :cvar FALLEN_TREE_ON_THE_LINE: TPEG Pts38_73, fallen tree on the
        line
    :cvar VEGETATION: TPEG Pts38_74, vegetation
    :cvar SPEED_RESTRICTIONS: TPEG Pts38_75, speed restrictions
    :cvar PRECEDING_VEHICLE: TPEG Pts38_76, preceding vehicle
    :cvar ACCIDENT: TPEG Pts38_77, accident
    :cvar NEAR_MISS: TPEG Pts38_78, near miss
    :cvar PERSON_HIT_BY_VEHICLE: TPEG Pts38_79, person hit by vehicle
    :cvar VEHICLE_STRUCK_OBJECT: TPEG Pts38_80, vehicle struck object
    :cvar VEHICLE_STRUCK_ANIMAL: TPEG Pts38_81, vehicle struck animal
    :cvar DERAILMENT: TPEG Pts38_82, derailment
    :cvar COLLISION: TPEG Pts38_83, collision
    :cvar LEVEL_CROSSING_ACCIDENT: TPEG Pts38_84, level crossing
        accident
    :cvar POOR_WEATHER: TPEG Pts38_85, poor weather
    :cvar FOG: TPEG Pts38_86, fog
    :cvar HEAVY_SNOW_FALL: TPEG Pts38_87, heavy snowfall
    :cvar HEAVY_RAIN: TPEG Pts38_88, heavy rain
    :cvar STRONG_WINDS: TPEG Pts38_89, strong winds
    :cvar ICE: TPEG Pts38_90, ice
    :cvar HAIL: TPEG Pts38_91, hail
    :cvar HIGH_TEMPERATURES: TPEG Pts38_92, high temperatures
    :cvar FLOODING: TPEG Pts38_93, flooding
    :cvar LOW_WATER_LEVEL: TPEG Pts38_94, low water level
    :cvar RISK_OF_FLOODING: TPEG Pts38_95, risk of flooding
    :cvar HIGH_WATER_LEVEL: TPEG Pts38_96, high water level
    :cvar FALLEN_LEAVES: TPEG Pts38_97, fallen leaves
    :cvar FALLEN_TREE: TPEG Pts38_98, fallen tree
    :cvar LANDSLIDE: TPEG Pts38_99, landslide
    :cvar RISK_OF_LANDSLIDE: TPEG Pts38_100, risk of landslide
    :cvar DRIFTING_SNOW: TPEG Pts38_101, drifting snow
    :cvar BLIZZARD_CONDITIONS: TPEG Pts38_102, blizzard conditions
    :cvar STORM_DAMAGE: TPEG Pts38_103, storm damage
    :cvar LIGHTNING_STRIKE: TPEG Pts38_104, lightning strike
    :cvar ROUGH_SEA: TPEG Pts38_105, rough sea
    :cvar HIGH_TIDE: TPEG Pts38_106, high tide
    :cvar LOW_TIDE: TPEG Pts38_107, low tide
    :cvar ICE_DRIFT: TPEG Pts38_108, ice drift
    :cvar AVALANCHES: TPEG Pts38_109, avalanches
    :cvar RISK_OF_AVALANCHES: TPEG Pts38_110, risk of avalanches
    :cvar FLASH_FLOODS: TPEG Pts38_111, flash floods
    :cvar MUDSLIDE: TPEG Pts38_112, mudslide
    :cvar ROCKFALLS: TPEG Pts38_113, rockfalls
    :cvar SUBSIDENCE: TPEG Pts38_114, subsidence
    :cvar EARTHQUAKE_DAMAGE: TPEG Pts38_115, earthquake damage
    :cvar GRASS_FIRE: TPEG Pts38_116, grass fire
    :cvar WILDLAND_FIRE: TPEG Pts38_117, wildland fire
    :cvar ICE_ON_RAILWAY: TPEG Pts38_118, ice on railway
    :cvar ICE_ON_CARRIAGES: TPEG Pts38_119, ice on carriages
    :cvar SPECIAL_EVENT: TPEG Pts38_120, special event
    :cvar PROCESSION: TPEG Pts38_121, procession
    :cvar DEMONSTRATION: TPEG Pts38_122, demonstration
    :cvar INDUSTRIAL_ACTION: TPEG Pts38_123, industrial action
    :cvar STAFF_SICKNESS: TPEG Pts38_124, staff sickness
    :cvar STAFF_ABSENCE: TPEG Pts38_125, staff absence
    :cvar OPERATOR_CEASED_TRADING: TPEG Pts38_126, operator ceased
        trading
    :cvar PREVIOUS_DISTURBANCES: TPEG Pts38_127, previous disturbances
    :cvar VEHICLE_BLOCKING_TRACK: TPEG Pts38_128, vehicle blocking track
    :cvar FOREIGN_DISTURBANCES: TPEG Pts38_129, foreign disturbances
    :cvar AWAITING_SHUTTLE: TPEG Pts38_130, awaiting shuttle
    :cvar CHANGE_IN_CARRIAGES: TPEG Pts38_131, change in carriages
    :cvar TRAIN_COUPLING: TPEG Pts38_132, train coupling
    :cvar BOARDING_DELAY: TPEG Pts38_133, boarding delay
    :cvar AWAITING_APPROACH: TPEG Pts38_134, awaiting approach
    :cvar OVERTAKING: TPEG Pts38_135, overtaking
    :cvar PROVISION_DELAY: TPEG Pts38_136, provision delay
    :cvar MISCELLANEOUS: TPEG Pts38_137, miscellaneous
    :cvar UNDEFINED_ALERT_CAUSE: TPEG Pts38_255, undefined alert cause
    :cvar INCIDENT: TPEG Pti19_1, DEPRECATED since SIRI 2.1
    :cvar SAFETY_VIOLATION: TPEG Pti19_1_2, DEPRECATED since SIRI 2.1
    :cvar TRAIN_DOOR: TPEG Pti19_1_5, DEPRECATED since SIRI 2.1 -
        replaced by Pts38_33, door failure
    :cvar ALTERCATION: TPEG Pti19_1_7, DEPRECATED since SIRI 2.1
    :cvar ILL_VEHICLE_OCCUPANTS: TPEG Pti19_1_8, DEPRECATED since SIRI
        2.1
    :cvar SERVICE_FAILURE: TPEG Pti19_1_12, DEPRECATED since SIRI 2.1 -
        replaced by Pts38_32, service disruption
    :cvar BOMB_EXPLOSION: TPEG Pti19_2, DEPRECATED since SIRI 2.1
    :cvar FIRE_BRIGADE_SAFETY_CHECKS: TPEG Pti19_3_2, DEPRECATED since
        SIRI 2.1
    :cvar CIVIL_EMERGENCY: TPEG Pti19_3_6, DEPRECATED since SIRI 2.1
    :cvar AIR_RAID: TPEG Pti19_3_7, DEPRECATED since SIRI 2.1
    :cvar SABOTAGE: TPEG Pti19_3_8, DEPRECATED since SIRI 2.1
    :cvar BOMB_ALERT: TPEG Pti19_3_9, DEPRECATED since SIRI 2.1
    :cvar ATTACK: TPEG Pti19_3_10, DEPRECATED since SIRI 2.1
    :cvar GUNFIRE_ON_ROADWAY: TPEG Pti19_3_13, DEPRECATED since SIRI 2.1
    :cvar SECURITY_INCIDENT: TPEG Pti19_3_16, DEPRECATED since SIRI 2.1
    :cvar LINESIDE_FIRE: TPEG Pti19_4_1, DEPRECATED since SIRI 2.1
    :cvar PASSENGER_ACTION: TPEG Pti19_5_1, DEPRECATED since SIRI 2.1
    :cvar STAFF_ASSAULT: TPEG Pti19_5_2, DEPRECATED since SIRI 2.1
    :cvar RAILWAY_CRIME: TPEG Pti19_5_3, DEPRECATED since SIRI 2.1
    :cvar ASSAULT: TPEG Pti19_5_4, DEPRECATED since SIRI 2.1
    :cvar THEFT: TPEG Pti19_5_5, DEPRECATED since SIRI 2.1
    :cvar FATALITY: TPEG Pti19_6_1, DEPRECATED since SIRI 2.1
    :cvar PERSON_UNDER_TRAIN: TPEG Pti19_6_2, DEPRECATED since SIRI 2.1
    :cvar PERSON_HIT_BY_TRAIN: TPEG Pti19_6_3, DEPRECATED since SIRI 2.1
        - replaced by Pts38_79, person hit by vehicle
    :cvar PERSON_ILL_ON_VEHICLE: TPEG Pti19_6_4, DEPRECATED since SIRI
        2.1
    :cvar EMERGENCY_SERVICES: TPEG Pti19_6_5, DEPRECATED since SIRI 2.1
        - replaced by Pts38_14, emergency medical services
    :cvar INSUFFICIENT_DEMAND: TPEG Pti19_8, DEPRECATED since SIRI 2.1
    :cvar LEADER_BOARD_FAILURE: TPEG Pti19_10, DEPRECATED since SIRI 2.1
    :cvar SERVICE_INDICATOR_FAILURE: TPEG Pti19_11, DEPRECATED since
        SIRI 2.1
    :cvar OPERATOR_SUSPENDED: TPEG Pti19_14, DEPRECATED since SIRI 2.1
    :cvar PROBLEMS_AT_BORDER_POST: TPEG Pti19_15_1, DEPRECATED since
        SIRI 2.1 - replaced by Pts38_23, border control
    :cvar PROBLEMS_AT_CUSTOMS_POST: TPEG Pti19_15_2, DEPRECATED since
        SIRI 2.1
    :cvar TRAIN_STRUCK_ANIMAL: TPEG Pti19_19_3, DEPRECATED since SIRI
        2.1 - replaced by Pts38_81, vehicle struck animal
    :cvar TRAIN_STRUCK_OBJECT: TPEG Pti19_19_4, DEPRECATED since SIRI
        2.1 - replaced by Pts38_80, vehicle struck object
    :cvar ROAD_MAINTENANCE: TPEG Pti19_23_2, DEPRECATED since SIRI 2.1
    :cvar ASPHALTING: TPEG Pti19_23_3, DEPRECATED since SIRI 2.1
    :cvar PAVING: TPEG Pti19_23_4, DEPRECATED since SIRI 2.1
    :cvar MARCH: TPEG Pti19_24_1, DEPRECATED since SIRI 2.1
    :cvar FILTER_BLOCKADE: TPEG Pti19_24_5, DEPRECATED since SIRI 2.1
    :cvar SIGHTSEERS_OBSTRUCTING_ACCESS: TPEG Pti19_24_6, DEPRECATED
        since SIRI 2.1
    :cvar HOLIDAY: TPEG Pti19_24_7, DEPRECATED since SIRI 2.1
    :cvar BRIDGE_STRIKE: TPEG Pti19_25, DEPRECATED since SIRI 2.1 -
        replaced by Pts38_68, bridge damage
    :cvar VIADUCT_FAILURE: TPEG Pti19_25_1, DEPRECATED since SIRI 2.1
    :cvar OVERHEAD_OBSTRUCTION: TPEG Pti19_26, DEPRECATED since SIRI 2.1
    :cvar UNDEFINED_PROBLEM: TPEG Pti19_255, DEPRECATED since SIRI 2.1
    :cvar LOGISTIC_PROBLEMS: TPEG Pti19_255_1, DEPRECATED since SIRI 2.1
    :cvar PROBLEMS_ON_LOCAL_ROAD: TPEG Pti19_255_2, DEPRECATED since
        SIRI 2.1
    :cvar STAFF_INJURY: TPEG Pti20_1_1, DEPRECATED since SIRI 2.1
    :cvar CONTRACTOR_STAFF_INJURY: TPEG Pti20_1_2, DEPRECATED since SIRI
        2.1
    :cvar STAFF_IN_WRONG_PLACE: TPEG Pti20_3, DEPRECATED since SIRI 2.1
    :cvar STAFF_SHORTAGE: TPEG Pti20_4, DEPRECATED since SIRI 2.1
    :cvar UNOFFICIAL_INDUSTRIAL_ACTION: TPEG Pti20_5_1, DEPRECATED since
        SIRI 2.1
    :cvar WORK_TO_RULE: TPEG Pti20_6, DEPRECATED since SIRI 2.1
    :cvar UNDEFINED_PERSONNEL_PROBLEM: TPEG Pti20_255, DEPRECATED since
        SIRI 2.1 - replaced by Pts38_255, undefined alert cause
    :cvar TRAIN_WARNING_SYSTEM_PROBLEM: TPEG Pti21_3_1, DEPRECATED since
        SIRI 2.1
    :cvar SIGNAL_AND_SWITCH_FAILURE: TPEG Pti21_4_1, DEPRECATED since
        SIRI 2.1
    :cvar TRACTION_FAILURE: TPEG Pti21_6_1, DEPRECATED since SIRI 2.1
    :cvar DEFECTIVE_TRAIN: TPEG Pti21_6_2, DEPRECATED since SIRI 2.1 -
        replaced by Pts38_53, defective vehicle
    :cvar WHEEL_IMPACT_LOAD: TPEG Pti21_8_3, DEPRECATED since SIRI 2.1
    :cvar LACK_OF_OPERATIONAL_STOCK: TPEG Pti21_8_4, DEPRECATED since
        SIRI 2.1
    :cvar DEFECTIVE_FIRE_ALARM_EQUIPMENT: TPEG Pti21_8_5, DEPRECATED
        since SIRI 2.1
    :cvar DEFECTIVE_PLATFORM_EDGE_DOORS: TPEG Pti21_8_6, DEPRECATED
        since SIRI 2.1
    :cvar DEFECTIVE_CCTV: TPEG Pti21_8_7, DEPRECATED since SIRI 2.1
    :cvar DEFECTIVE_PUBLIC_ANNOUNCEMENT_SYSTEM: TPEG Pti21_8_8,
        DEPRECATED since SIRI 2.1
    :cvar TICKETING_SYSTEM_NOT_AVAILABLE: TPEG Pti21_8_9, DEPRECATED
        since SIRI 2.1
    :cvar EMERGENCY_ENGINEERING_WORK: TPEG Pti21_11_1, DEPRECATED since
        SIRI 2.1
    :cvar LATE_FINISH_TO_ENGINEERING_WORK: TPEG Pti21_11_2, DEPRECATED
        since SIRI 2.1
    :cvar FUEL_PROBLEM: TPEG Pti21_13, DEPRECATED since SIRI 2.1
    :cvar CLOSED_FOR_MAINTENANCE: TPEG Pti21_18, DEPRECATED since SIRI
        2.1
    :cvar FUEL_SHORTAGE: TPEG Pti21_19, DEPRECATED since SIRI 2.1
    :cvar SLIPPERY_TRACK: TPEG Pti21_21_1, DEPRECATED since SIRI 2.1
    :cvar LUGGAGE_CAROUSEL_PROBLEM: TPEG Pti21_22, DEPRECATED since SIRI
        2.1
    :cvar UNDEFINED_EQUIPMENT_PROBLEM: TPEG Pti21_255, DEPRECATED since
        SIRI 2.1 - replaced by Pts38_255, undefined alert cause
    :cvar STORM_CONDITIONS: TPEG Pti22_5_1, DEPRECATED since SIRI 2.1
    :cvar TIDAL_RESTRICTIONS: TPEG Pti22_6, DEPRECATED since SIRI 2.1
    :cvar SLIPPERINESS: TPEG Pti22_9_1, DEPRECATED since SIRI 2.1
    :cvar GLAZED_FROST: TPEG Pti22_9_3, DEPRECATED since SIRI 2.1
    :cvar FROZEN: TPEG Pti22_10, DEPRECATED since SIRI 2.1
    :cvar SLEET: TPEG Pti22_11_1, DEPRECATED since SIRI 2.1
    :cvar WATERLOGGED: TPEG Pti22_14, DEPRECATED since SIRI 2.1
    :cvar SEWER_OVERFLOW: TPEG Pti22_255_2, DEPRECATED since SIRI 2.1
    :cvar UNDEFINED_ENVIRONMENTAL_PROBLEM: TPEG Pti22_255, DEPRECATED
        since SIRI 2.1 - replaced by Pts38_255, undefined alert cause
    :cvar FIRE_AT_THE_STATION: See also TPEG Pts38_8 value
        'fireAtStation'.
    :cvar BREAKDOWN_1: See also TPEG Pts38_43 value 'breakDown'.
    :cvar LEVEL_CROSSING_BLOCKED: See also TPEG Pts38_64 value
        'levelCrossingIncident'.
    :cvar HEAVY_SNOWFALL_1: See also TPEG Pts38_87 value
        'heavySnowFall'.
    :cvar WAITING_FOR_TRANSFER_PASSENGERS: See also TPEG Pts38_130 value
        'awaitingShuttle'.
    :cvar AWAITING_ONCOMING_VEHICLE: See also TPEG Pts38_134 value
        'awaitingApproach'.
    """
    UNKNOWN = "unknown"
    SECURITY_ALERT = "securityAlert"
    EMERGENCY_SERVICES_CALL = "emergencyServicesCall"
    POLICE_ACTIVITY = "policeActivity"
    POLICE_ORDER = "policeOrder"
    FIRE = "fire"
    CABLE_FIRE = "cableFire"
    SMOKE_DETECTED_ON_VEHICLE = "smokeDetectedOnVehicle"
    FIRE_AT_STATION = "fireAtStation"
    FIRE_RUN = "fireRun"
    FIRE_BRIGADE_ORDER = "fireBrigadeOrder"
    EXPLOSION = "explosion"
    EXPLOSION_HAZARD = "explosionHazard"
    BOMB_DISPOSAL = "bombDisposal"
    EMERGENCY_MEDICAL_SERVICES = "emergencyMedicalServices"
    EMERGENCY_BRAKE = "emergencyBrake"
    VANDALISM = "vandalism"
    CABLE_THEFT = "cableTheft"
    SIGNAL_PASSED_AT_DANGER = "signalPassedAtDanger"
    STATION_OVERRUN = "stationOverrun"
    PASSENGERS_BLOCKING_DOORS = "passengersBlockingDoors"
    DEFECTIVE_SECURITY_SYSTEM = "defectiveSecuritySystem"
    OVERCROWDED = "overcrowded"
    BORDER_CONTROL = "borderControl"
    UNATTENDED_BAG = "unattendedBag"
    TELEPHONED_THREAT = "telephonedThreat"
    SUSPECT_VEHICLE = "suspectVehicle"
    EVACUATION = "evacuation"
    TERRORIST_INCIDENT = "terroristIncident"
    PUBLIC_DISTURBANCE = "publicDisturbance"
    TECHNICAL_PROBLEM = "technicalProblem"
    VEHICLE_FAILURE = "vehicleFailure"
    SERVICE_DISRUPTION = "serviceDisruption"
    DOOR_FAILURE = "doorFailure"
    LIGHTING_FAILURE = "lightingFailure"
    POINTS_PROBLEM = "pointsProblem"
    POINTS_FAILURE = "pointsFailure"
    SIGNAL_PROBLEM = "signalProblem"
    SIGNAL_FAILURE = "signalFailure"
    OVERHEAD_WIRE_FAILURE = "overheadWireFailure"
    LEVEL_CROSSING_FAILURE = "levelCrossingFailure"
    TRAFFIC_MANAGEMENT_SYSTEM_FAILURE = "trafficManagementSystemFailure"
    ENGINE_FAILURE = "engineFailure"
    BREAK_DOWN = "breakDown"
    REPAIR_WORK = "repairWork"
    CONSTRUCTION_WORK = "constructionWork"
    MAINTENANCE_WORK = "maintenanceWork"
    POWER_PROBLEM = "powerProblem"
    TRACK_CIRCUIT_PROBLEM = "trackCircuitProblem"
    SWING_BRIDGE_FAILURE = "swingBridgeFailure"
    ESCALATOR_FAILURE = "escalatorFailure"
    LIFT_FAILURE = "liftFailure"
    GANGWAY_PROBLEM = "gangwayProblem"
    DEFECTIVE_VEHICLE = "defectiveVehicle"
    BROKEN_RAIL = "brokenRail"
    POOR_RAIL_CONDITIONS = "poorRailConditions"
    DEICING_WORK = "deicingWork"
    WHEEL_PROBLEM = "wheelProblem"
    ROUTE_BLOCKAGE = "routeBlockage"
    CONGESTION = "congestion"
    HEAVY_TRAFFIC = "heavyTraffic"
    ROUTE_DIVERSION = "routeDiversion"
    ROADWORKS = "roadworks"
    UNSCHEDULED_CONSTRUCTION_WORK = "unscheduledConstructionWork"
    LEVEL_CROSSING_INCIDENT = "levelCrossingIncident"
    SEWERAGE_MAINTENANCE = "sewerageMaintenance"
    ROAD_CLOSED = "roadClosed"
    ROADWAY_DAMAGE = "roadwayDamage"
    BRIDGE_DAMAGE = "bridgeDamage"
    PERSON_ON_THE_LINE = "personOnTheLine"
    OBJECT_ON_THE_LINE = "objectOnTheLine"
    VEHICLE_ON_THE_LINE = "vehicleOnTheLine"
    ANIMAL_ON_THE_LINE = "animalOnTheLine"
    FALLEN_TREE_ON_THE_LINE = "fallenTreeOnTheLine"
    VEGETATION = "vegetation"
    SPEED_RESTRICTIONS = "speedRestrictions"
    PRECEDING_VEHICLE = "precedingVehicle"
    ACCIDENT = "accident"
    NEAR_MISS = "nearMiss"
    PERSON_HIT_BY_VEHICLE = "personHitByVehicle"
    VEHICLE_STRUCK_OBJECT = "vehicleStruckObject"
    VEHICLE_STRUCK_ANIMAL = "vehicleStruckAnimal"
    DERAILMENT = "derailment"
    COLLISION = "collision"
    LEVEL_CROSSING_ACCIDENT = "levelCrossingAccident"
    POOR_WEATHER = "poorWeather"
    FOG = "fog"
    HEAVY_SNOW_FALL = "heavySnowFall"
    HEAVY_RAIN = "heavyRain"
    STRONG_WINDS = "strongWinds"
    ICE = "ice"
    HAIL = "hail"
    HIGH_TEMPERATURES = "highTemperatures"
    FLOODING = "flooding"
    LOW_WATER_LEVEL = "lowWaterLevel"
    RISK_OF_FLOODING = "riskOfFlooding"
    HIGH_WATER_LEVEL = "highWaterLevel"
    FALLEN_LEAVES = "fallenLeaves"
    FALLEN_TREE = "fallenTree"
    LANDSLIDE = "landslide"
    RISK_OF_LANDSLIDE = "riskOfLandslide"
    DRIFTING_SNOW = "driftingSnow"
    BLIZZARD_CONDITIONS = "blizzardConditions"
    STORM_DAMAGE = "stormDamage"
    LIGHTNING_STRIKE = "lightningStrike"
    ROUGH_SEA = "roughSea"
    HIGH_TIDE = "highTide"
    LOW_TIDE = "lowTide"
    ICE_DRIFT = "iceDrift"
    AVALANCHES = "avalanches"
    RISK_OF_AVALANCHES = "riskOfAvalanches"
    FLASH_FLOODS = "flashFloods"
    MUDSLIDE = "mudslide"
    ROCKFALLS = "rockfalls"
    SUBSIDENCE = "subsidence"
    EARTHQUAKE_DAMAGE = "earthquakeDamage"
    GRASS_FIRE = "grassFire"
    WILDLAND_FIRE = "wildlandFire"
    ICE_ON_RAILWAY = "iceOnRailway"
    ICE_ON_CARRIAGES = "iceOnCarriages"
    SPECIAL_EVENT = "specialEvent"
    PROCESSION = "procession"
    DEMONSTRATION = "demonstration"
    INDUSTRIAL_ACTION = "industrialAction"
    STAFF_SICKNESS = "staffSickness"
    STAFF_ABSENCE = "staffAbsence"
    OPERATOR_CEASED_TRADING = "operatorCeasedTrading"
    PREVIOUS_DISTURBANCES = "previousDisturbances"
    VEHICLE_BLOCKING_TRACK = "vehicleBlockingTrack"
    FOREIGN_DISTURBANCES = "foreignDisturbances"
    AWAITING_SHUTTLE = "awaitingShuttle"
    CHANGE_IN_CARRIAGES = "changeInCarriages"
    TRAIN_COUPLING = "trainCoupling"
    BOARDING_DELAY = "boardingDelay"
    AWAITING_APPROACH = "awaitingApproach"
    OVERTAKING = "overtaking"
    PROVISION_DELAY = "provisionDelay"
    MISCELLANEOUS = "miscellaneous"
    UNDEFINED_ALERT_CAUSE = "undefinedAlertCause"
    INCIDENT = "incident"
    SAFETY_VIOLATION = "safetyViolation"
    TRAIN_DOOR = "trainDoor"
    ALTERCATION = "altercation"
    ILL_VEHICLE_OCCUPANTS = "illVehicleOccupants"
    SERVICE_FAILURE = "serviceFailure"
    BOMB_EXPLOSION = "bombExplosion"
    FIRE_BRIGADE_SAFETY_CHECKS = "fireBrigadeSafetyChecks"
    CIVIL_EMERGENCY = "civilEmergency"
    AIR_RAID = "airRaid"
    SABOTAGE = "sabotage"
    BOMB_ALERT = "bombAlert"
    ATTACK = "attack"
    GUNFIRE_ON_ROADWAY = "gunfireOnRoadway"
    SECURITY_INCIDENT = "securityIncident"
    LINESIDE_FIRE = "linesideFire"
    PASSENGER_ACTION = "passengerAction"
    STAFF_ASSAULT = "staffAssault"
    RAILWAY_CRIME = "railwayCrime"
    ASSAULT = "assault"
    THEFT = "theft"
    FATALITY = "fatality"
    PERSON_UNDER_TRAIN = "personUnderTrain"
    PERSON_HIT_BY_TRAIN = "personHitByTrain"
    PERSON_ILL_ON_VEHICLE = "personIllOnVehicle"
    EMERGENCY_SERVICES = "emergencyServices"
    INSUFFICIENT_DEMAND = "insufficientDemand"
    LEADER_BOARD_FAILURE = "leaderBoardFailure"
    SERVICE_INDICATOR_FAILURE = "serviceIndicatorFailure"
    OPERATOR_SUSPENDED = "operatorSuspended"
    PROBLEMS_AT_BORDER_POST = "problemsAtBorderPost"
    PROBLEMS_AT_CUSTOMS_POST = "problemsAtCustomsPost"
    TRAIN_STRUCK_ANIMAL = "trainStruckAnimal"
    TRAIN_STRUCK_OBJECT = "trainStruckObject"
    ROAD_MAINTENANCE = "roadMaintenance"
    ASPHALTING = "asphalting"
    PAVING = "paving"
    MARCH = "march"
    FILTER_BLOCKADE = "filterBlockade"
    SIGHTSEERS_OBSTRUCTING_ACCESS = "sightseersObstructingAccess"
    HOLIDAY = "holiday"
    BRIDGE_STRIKE = "bridgeStrike"
    VIADUCT_FAILURE = "viaductFailure"
    OVERHEAD_OBSTRUCTION = "overheadObstruction"
    UNDEFINED_PROBLEM = "undefinedProblem"
    LOGISTIC_PROBLEMS = "logisticProblems"
    PROBLEMS_ON_LOCAL_ROAD = "problemsOnLocalRoad"
    STAFF_INJURY = "staffInjury"
    CONTRACTOR_STAFF_INJURY = "contractorStaffInjury"
    STAFF_IN_WRONG_PLACE = "staffInWrongPlace"
    STAFF_SHORTAGE = "staffShortage"
    UNOFFICIAL_INDUSTRIAL_ACTION = "unofficialIndustrialAction"
    WORK_TO_RULE = "workToRule"
    UNDEFINED_PERSONNEL_PROBLEM = "undefinedPersonnelProblem"
    TRAIN_WARNING_SYSTEM_PROBLEM = "trainWarningSystemProblem"
    SIGNAL_AND_SWITCH_FAILURE = "signalAndSwitchFailure"
    TRACTION_FAILURE = "tractionFailure"
    DEFECTIVE_TRAIN = "defectiveTrain"
    WHEEL_IMPACT_LOAD = "wheelImpactLoad"
    LACK_OF_OPERATIONAL_STOCK = "lackOfOperationalStock"
    DEFECTIVE_FIRE_ALARM_EQUIPMENT = "defectiveFireAlarmEquipment"
    DEFECTIVE_PLATFORM_EDGE_DOORS = "defectivePlatformEdgeDoors"
    DEFECTIVE_CCTV = "defectiveCctv"
    DEFECTIVE_PUBLIC_ANNOUNCEMENT_SYSTEM = "defectivePublicAnnouncementSystem"
    TICKETING_SYSTEM_NOT_AVAILABLE = "ticketingSystemNotAvailable"
    EMERGENCY_ENGINEERING_WORK = "emergencyEngineeringWork"
    LATE_FINISH_TO_ENGINEERING_WORK = "lateFinishToEngineeringWork"
    FUEL_PROBLEM = "fuelProblem"
    CLOSED_FOR_MAINTENANCE = "closedForMaintenance"
    FUEL_SHORTAGE = "fuelShortage"
    SLIPPERY_TRACK = "slipperyTrack"
    LUGGAGE_CAROUSEL_PROBLEM = "luggageCarouselProblem"
    UNDEFINED_EQUIPMENT_PROBLEM = "undefinedEquipmentProblem"
    STORM_CONDITIONS = "stormConditions"
    TIDAL_RESTRICTIONS = "tidalRestrictions"
    SLIPPERINESS = "slipperiness"
    GLAZED_FROST = "glazedFrost"
    FROZEN = "frozen"
    SLEET = "sleet"
    WATERLOGGED = "waterlogged"
    SEWER_OVERFLOW = "sewerOverflow"
    UNDEFINED_ENVIRONMENTAL_PROBLEM = "undefinedEnvironmentalProblem"
    FIRE_AT_THE_STATION = "fireAtTheStation"
    BREAKDOWN_1 = "breakdown"
    LEVEL_CROSSING_BLOCKED = "levelCrossingBlocked"
    HEAVY_SNOWFALL_1 = "heavySnowfall"
    WAITING_FOR_TRANSFER_PASSENGERS = "waitingForTransferPassengers"
    AWAITING_ONCOMING_VEHICLE = "awaitingOncomingVehicle"
