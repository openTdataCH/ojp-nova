from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class MiscellaneousReasonEnumeration(Enum):
    """
    Values for Miscellaneous incident reason types TPEG Pti18_1/TPEG Pti_19.

    :cvar PTI19_0:
    :cvar UNKNOWN: TPEG Pti_19_0 unknown.
    :cvar PTI19_0_1:
    :cvar PREVIOUS_DISTURBANCES: 19:0_1 Previous disturbances - alias to
        TPEG Pti_19_0 unknown
    :cvar PTI19_1:
    :cvar INCIDENT: TPEG Pti_19_1 incident.
    :cvar PTI19_1_ALIAS_1:
    :cvar NEAR_MISS: Near Miss - alias to TPEG Pti_19_1 incident.
    :cvar PTI19_1_ALIAS_2:
    :cvar SAFETY_VIOLATION: Near Miss - alias to TPEG Pti_19_1 incident.
    :cvar PTI19_1_ALIAS_3:
    :cvar SIGNAL_PASSED_AT_DANGER: Signal passed at danger - alias to
        TPEG Pti_19_1 incident.
    :cvar PTI19_1_ALIAS_4:
    :cvar STATION_OVERRUN: Station overrun - alias to TPEG Pti_19_1
        incident.
    :cvar PTI19_1_ALIAS_5:
    :cvar TRAIN_DOOR: trainDoor- alias to TPEG Pti_19_1 incident.
    :cvar PTI19_1_ALIAS_6:
    :cvar EMERGENCY_SERVICES_CALL: Unspecified emergency service visit.
        Alias to pti19
    :cvar PTI19_2:
    :cvar BOMB_EXPLOSION: TPEG Pti_19_2 bomb explosion.
    :cvar PTI19_3:
    :cvar SECURITY_ALERT: TPEG Pti_19_3 security alert.
    :cvar PTI19_3_ALIAS_1:
    :cvar POLICE_REQUEST: pti19_3_1 request of the police Alias to TPEG
        Pti_19_3 security alert.
    :cvar PTI19_3_ALIAS_2:
    :cvar FIRE_BRIGADE_SAFETY_CHECKS: pti19_3_2 fire brigade safety
        checksAlias to TPEG Pti_19_3 security alert.
    :cvar PTI19_3_ALIAS_3:
    :cvar UNATTENDED_BAG: pti19_3_3 an unattended bag Talias to PEG
        Pti_19_3 security alert.
    :cvar PTI19_3_ALIAS_4:
    :cvar TELEPHONED_THREAT: telephoned threat TPEG Pti_19_3 security
        alert.
    :cvar PTI19_3_ALIAS_5:
    :cvar SUSPECT_VEHICLE: telephoned threat TPEG Pti_19_3 security
        alert.
    :cvar PTI19_3_ALIAS_6:
    :cvar CIVIL_EMERGENCY: civilEmergency alias to  TPEG Pti_19_3
        security alert.
    :cvar PTI19_3_ALIAS_7:
    :cvar AIR_RAID: civilEmergency alias to  TPEG Pti_19_3 security
        alert.
    :cvar PTI19_3_ALIAS_8:
    :cvar SABOTAGE: sabotage alias to TPEG Pti_19_3 security alert.
    :cvar PTI19_3_ALIAS_9:
    :cvar BOMB_ALERT:
    :cvar PTI19_3_ALIAS_10:
    :cvar ATTACK:
    :cvar PTI19_3_ALIAS_11:
    :cvar EVACUATION:
    :cvar PTI19_3_ALIAS_12:
    :cvar TERRORIST_INCIDENT:
    :cvar PTI19_3_ALIAS_13:
    :cvar GUNFIRE_ON_ROADWAY:
    :cvar PTI19_3_ALIAS_14:
    :cvar EXPLOSION:
    :cvar PTI19_3_ALIAS_15:
    :cvar EXPLOSION_HAZARD:
    :cvar PTI19_3_ALIAS_16:
    :cvar SECURITY_INCIDENT:
    :cvar PTI19_3_ALIAS_17:
    :cvar FIRE_BRIGADE_ORDER:
    :cvar PTI19_3_ALIAS_18:
    :cvar POLICE_ACTIVITY:
    :cvar PTI19_4:
    :cvar FIRE: TPEG Pti_19_4 fire.
    :cvar PTI19_4_ALIAS_1:
    :cvar LINESIDE_FIRE: linesideFire alias to TPEG Pti_19_4 fire.
    :cvar PTI19_5:
    :cvar VANDALISM: TPEG Pti_19_5 vandalism.
    :cvar PTI19_5_ALIAS_1:
    :cvar PASSENGER_ACTION: passengerActionAlias to pti19
    :cvar PTI19_5_ALIAS_2:
    :cvar STAFF_ASSAULT: Assault on stafft.Alias to pti19
    :cvar PTI19_5_ALIAS_3:
    :cvar RAILWAY_CRIME: Railway Crime Alias to pti19
    :cvar PTI19_5_ALIAS_4:
    :cvar ASSAULT: Assault Alias to pti19
    :cvar PTI19_5_ALIAS_5:
    :cvar THEFT: Theft Alias to pti19
    :cvar ALTERCATION: altercation. Alias to pti19
    :cvar PTI19_1_ALIAS_7:
    :cvar ILL_VEHICLE_OCCUPANTS: illVehicleOccupants. Alias to pti19
    :cvar PTI19_6:
    :cvar ACCIDENT: TPEG Pti_19_6 accident.
    :cvar PTI19_6_ALIAS_1:
    :cvar FATALITY: fatality alias to TPEG Pti_19_6 accident.
    :cvar PTI19_6_ALIAS_2:
    :cvar PERSON_UNDER_TRAIN: a person under a train - alias to TPEG
        Pti_19_6 accident.
    :cvar PTI19_6_ALIAS_3:
    :cvar PERSON_HIT_BY_TRAIN: a person hit by a train - alias to TPEG
        Pti_19_6 accident.
    :cvar PTI19_6_ALIAS_4:
    :cvar PERSON_ILL_ON_VEHICLE: person ill On Vehicle -Alias to pti19_6
    :cvar PTI19_6_ALIAS_5:
    :cvar EMERGENCY_SERVICES: emergencyServices - alias to TPEG Pti_19_6
        accident.
    :cvar PTI19_6_ALIAS_6:
    :cvar COLLISION: Collision - Alias to pti19_6
    :cvar PTI19_7:
    :cvar OVERCROWDED: TPEG Pti_19_7 overcrowded.
    :cvar PTI19_8:
    :cvar INSUFFICIENT_DEMAND: TPEG Pti_19_8 insufficient demand.
    :cvar PTI19_9:
    :cvar LIGHTING_FAILURE: TPEG Pti_19_9 lighting failure.
    :cvar PTI19_10:
    :cvar LEADER_BOARD_FAILURE: TPEG Pti_19_10 leader board failure.
    :cvar PTI19_11:
    :cvar SERVICE_INDICATOR_FAILURE: TPEG Pti_19_11 service indicator
        failure.
    :cvar PTI19_12:
    :cvar SERVICE_FAILURE: TPEG Pti_19_12 service failure.
    :cvar PTI19_13:
    :cvar OPERATOR_CEASED_TRADING: TPEG Pti_19_13 OPERATOR ceased
        trading.
    :cvar PTI19_14:
    :cvar OPERATOR_SUSPENDED: TPEG Pti_19_14 OPERATOR suspended.
    :cvar PTI19_15:
    :cvar CONGESTION: TPEG Pti_19_15 congestion.
    :cvar PTI19_16:
    :cvar ROUTE_BLOCKAGE: TPEG Pti_19_16 route blockage.
    :cvar PTI19_17:
    :cvar PERSON_ON_THE_LINE: TPEG Pti_19_17 person on the line.
    :cvar PTI19_18:
    :cvar VEHICLE_ON_THE_LINE: TPEG Pti_19_18 VEHICLE on the line.
    :cvar PTI19_18_ALIAS_1:
    :cvar LEVEL_CROSSING_INCIDENT: Level Crossing Incident - alias to
        TPEG Pti_19_18 VEHICLE on the line.
    :cvar PTI19_19:
    :cvar OBJECT_ON_THE_LINE: TPEG Pti_19_19 object on the line.
    :cvar PTI19_19_ALIAS_1:
    :cvar FALLEN_TREE_ON_THE_LINE: fallen tree on line- alias to TPEG
        Pti_19_19 object on the line.
    :cvar PTI19_19_ALIAS_2:
    :cvar VEGETATION: vegetation - alias to TPEG Pti_19_19 object on the
        line.
    :cvar PTI19_19_ALIAS_3:
    :cvar TRAIN_STRUCK_ANIMAL: Train struck animal alias to TPEG
        Pti_19_19 object on the line.
    :cvar PTI19_19_ALIAS_4:
    :cvar TRAIN_STRUCK_OBJECT: Train struck object alias to TPEG
        Pti_19_19 object on the line.
    :cvar PTI19_20:
    :cvar ANIMAL_ON_THE_LINE: TPEG Pti_19_20 animal on the line.
    :cvar PTI19_21:
    :cvar ROUTE_DIVERSION: TPEG Pti_19_21 route diversion.
    :cvar PTI19_22:
    :cvar ROAD_CLOSED: TPEG Pti_19_22 road closed.
    :cvar PTI19_23:
    :cvar ROADWORKS: TPEG Pti_19_23 roadworks.
    :cvar PTI19_23_ALIAS_1:
    :cvar SEWERAGE_MAINTENANCE: 19:23_1 sewerageMaintenance - alias to
        TPEG Pti_19_23 roadworks..
    :cvar PTI19_23_ALIAS_2:
    :cvar ROAD_MAINTENANCE: 19:23_2 roadMaintenance - alias to TPEG
        Pti_19_23 roadworks..
    :cvar PTI19_23_ALIAS_3:
    :cvar ASPHALTING: 19:23_3 asphalting - alias to TPEG Pti_19_23
        roadworks..
    :cvar PTI19_23_ALIAS_4:
    :cvar PAVING: 19:23_4 paving - alias to TPEG Pti_19_23 roadworks..
    :cvar PTI19_24:
    :cvar SPECIAL_EVENT: TPEG Pti_19_24 special event.
    :cvar PTI19_24_ALIAS_1:
    :cvar MARCH:
    :cvar PTI19_24_ALIAS_2:
    :cvar PROCESSION:
    :cvar PTI19_24_ALIAS_3:
    :cvar DEMONSTRATION:
    :cvar PTI19_24_ALIAS_4:
    :cvar PUBLIC_DISTURBANCE:
    :cvar PTI19_24_ALIAS_5:
    :cvar FILTER_BLOCKADE:
    :cvar PTI19_24_ALIAS_6:
    :cvar SIGHTSEERS_OBSTRUCTING_ACCESS:
    :cvar PTI19_24_ALIAS_7:
    :cvar HOLIDAY:
    :cvar PTI19_25:
    :cvar BRIDGE_STRIKE: TPEG Pti_19_25 bridge strike.
    :cvar PTI19_25_ALIAS_1:
    :cvar VIADUCT_FAILURE: 19:25_1 viaductFailure - alias to TPEG
        Pti_19_24 bridgeStrike
    :cvar PTI19_26:
    :cvar OVERHEAD_OBSTRUCTION: TPEG Pti_19_26 overhead obstruction.
    :cvar PTI19_27:
    :cvar UNDEFINED_PROBLEM: TPEG Pti_19_255 undefined problem.
    :cvar PTI19_15_ALIAS_1:
    :cvar PROBLEMS_AT_BORDER_POST:
    :cvar PTI19_15_ALIAS_2:
    :cvar PROBLEMS_AT_CUSTOMS_POST:
    :cvar PTI19_15_ALIAS_3:
    :cvar SPEED_RESTRICTIONS: 19:255_1 speedRestrictions alias to TPEG
        Pti_19_15 unknown
    :cvar PTI19_255_ALIAS_1:
    :cvar LOGISTIC_PROBLEMS: 19:255_2 logisticProblems alias to TPEG
        Pti_19_15 unknown
    :cvar PTI19_255_ALIAS_2:
    :cvar PROBLEMS_ON_LOCAL_ROAD:
    """
    PTI19_0 = "pti19_0"
    UNKNOWN = "unknown"
    PTI19_0_1 = "pti19_0_1"
    PREVIOUS_DISTURBANCES = "previousDisturbances"
    PTI19_1 = "pti19_1"
    INCIDENT = "incident"
    PTI19_1_ALIAS_1 = "pti19_1_Alias_1"
    NEAR_MISS = "nearMiss"
    PTI19_1_ALIAS_2 = "pti19_1_Alias_2"
    SAFETY_VIOLATION = "safetyViolation"
    PTI19_1_ALIAS_3 = "pti19_1_Alias_3"
    SIGNAL_PASSED_AT_DANGER = "signalPassedAtDanger"
    PTI19_1_ALIAS_4 = "pti19_1_Alias_4"
    STATION_OVERRUN = "stationOverrun"
    PTI19_1_ALIAS_5 = "pti19_1_Alias_5"
    TRAIN_DOOR = "trainDoor"
    PTI19_1_ALIAS_6 = "pti19_1_Alias_6"
    EMERGENCY_SERVICES_CALL = "emergencyServicesCall"
    PTI19_2 = "pti19_2"
    BOMB_EXPLOSION = "bombExplosion"
    PTI19_3 = "pti19_3"
    SECURITY_ALERT = "securityAlert"
    PTI19_3_ALIAS_1 = "pti19_3_Alias_1"
    POLICE_REQUEST = "policeRequest"
    PTI19_3_ALIAS_2 = "pti19_3_Alias_2"
    FIRE_BRIGADE_SAFETY_CHECKS = "fireBrigadeSafetyChecks"
    PTI19_3_ALIAS_3 = "pti19_3_Alias_3"
    UNATTENDED_BAG = "unattendedBag"
    PTI19_3_ALIAS_4 = "pti19_3_Alias_4"
    TELEPHONED_THREAT = "telephonedThreat"
    PTI19_3_ALIAS_5 = "pti19_3_Alias_5"
    SUSPECT_VEHICLE = "suspectVehicle"
    PTI19_3_ALIAS_6 = "pti19_3_Alias_6"
    CIVIL_EMERGENCY = "civilEmergency"
    PTI19_3_ALIAS_7 = "pti19_3_Alias_7"
    AIR_RAID = "airRaid"
    PTI19_3_ALIAS_8 = "pti19_3_Alias_8"
    SABOTAGE = "sabotage"
    PTI19_3_ALIAS_9 = "pti19_3_Alias_9"
    BOMB_ALERT = "bombAlert"
    PTI19_3_ALIAS_10 = "pti19_3_Alias_10"
    ATTACK = "attack"
    PTI19_3_ALIAS_11 = "pti19_3_Alias_11"
    EVACUATION = "evacuation"
    PTI19_3_ALIAS_12 = "pti19_3_Alias_12"
    TERRORIST_INCIDENT = "terroristIncident"
    PTI19_3_ALIAS_13 = "pti19_3_Alias_13"
    GUNFIRE_ON_ROADWAY = "gunfireOnRoadway"
    PTI19_3_ALIAS_14 = "pti19_3_Alias_14"
    EXPLOSION = "explosion"
    PTI19_3_ALIAS_15 = "pti19_3_Alias_15"
    EXPLOSION_HAZARD = "explosionHazard"
    PTI19_3_ALIAS_16 = "pti19_3_Alias_16"
    SECURITY_INCIDENT = "securityIncident"
    PTI19_3_ALIAS_17 = "pti19_3_Alias_17"
    FIRE_BRIGADE_ORDER = "fireBrigadeOrder"
    PTI19_3_ALIAS_18 = "pti19_3_Alias_18"
    POLICE_ACTIVITY = "policeActivity"
    PTI19_4 = "pti19_4"
    FIRE = "fire"
    PTI19_4_ALIAS_1 = "pti19_4_Alias_1"
    LINESIDE_FIRE = "linesideFire"
    PTI19_5 = "pti19_5"
    VANDALISM = "vandalism"
    PTI19_5_ALIAS_1 = "pti19_5_Alias_1"
    PASSENGER_ACTION = "passengerAction"
    PTI19_5_ALIAS_2 = "pti19_5_Alias_2"
    STAFF_ASSAULT = "staffAssault"
    PTI19_5_ALIAS_3 = "pti19_5_Alias_3"
    RAILWAY_CRIME = "railwayCrime"
    PTI19_5_ALIAS_4 = "pti19_5_Alias_4"
    ASSAULT = "assault"
    PTI19_5_ALIAS_5 = "pti19_5_Alias_5"
    THEFT = "theft"
    ALTERCATION = "altercation"
    PTI19_1_ALIAS_7 = "pti19_1_Alias_7"
    ILL_VEHICLE_OCCUPANTS = "illVehicleOccupants"
    PTI19_6 = "pti19_6"
    ACCIDENT = "accident"
    PTI19_6_ALIAS_1 = "pti19_6_Alias_1"
    FATALITY = "fatality"
    PTI19_6_ALIAS_2 = "pti19_6_Alias_2"
    PERSON_UNDER_TRAIN = "personUnderTrain"
    PTI19_6_ALIAS_3 = "pti19_6_Alias_3"
    PERSON_HIT_BY_TRAIN = "personHitByTrain"
    PTI19_6_ALIAS_4 = "pti19_6_Alias_4"
    PERSON_ILL_ON_VEHICLE = "personIllOnVehicle"
    PTI19_6_ALIAS_5 = "pti19_6_Alias_5"
    EMERGENCY_SERVICES = "emergencyServices"
    PTI19_6_ALIAS_6 = "pti19_6_Alias_6"
    COLLISION = "collision"
    PTI19_7 = "pti19_7"
    OVERCROWDED = "overcrowded"
    PTI19_8 = "pti19_8"
    INSUFFICIENT_DEMAND = "insufficientDemand"
    PTI19_9 = "pti19_9"
    LIGHTING_FAILURE = "lightingFailure"
    PTI19_10 = "pti19_10"
    LEADER_BOARD_FAILURE = "leaderBoardFailure"
    PTI19_11 = "pti19_11"
    SERVICE_INDICATOR_FAILURE = "serviceIndicatorFailure"
    PTI19_12 = "pti19_12"
    SERVICE_FAILURE = "serviceFailure"
    PTI19_13 = "pti19_13"
    OPERATOR_CEASED_TRADING = "operatorCeasedTrading"
    PTI19_14 = "pti19_14"
    OPERATOR_SUSPENDED = "operatorSuspended"
    PTI19_15 = "pti19_15"
    CONGESTION = "congestion"
    PTI19_16 = "pti19_16"
    ROUTE_BLOCKAGE = "routeBlockage"
    PTI19_17 = "pti19_17"
    PERSON_ON_THE_LINE = "personOnTheLine"
    PTI19_18 = "pti19_18"
    VEHICLE_ON_THE_LINE = "vehicleOnTheLine"
    PTI19_18_ALIAS_1 = "pti19_18_Alias_1"
    LEVEL_CROSSING_INCIDENT = "levelCrossingIncident"
    PTI19_19 = "pti19_19"
    OBJECT_ON_THE_LINE = "objectOnTheLine"
    PTI19_19_ALIAS_1 = "pti19_19_Alias_1"
    FALLEN_TREE_ON_THE_LINE = "fallenTreeOnTheLine"
    PTI19_19_ALIAS_2 = "pti19_19_Alias_2"
    VEGETATION = "vegetation"
    PTI19_19_ALIAS_3 = "pti19_19_Alias_3"
    TRAIN_STRUCK_ANIMAL = "trainStruckAnimal"
    PTI19_19_ALIAS_4 = "pti19_19_Alias_4"
    TRAIN_STRUCK_OBJECT = "trainStruckObject"
    PTI19_20 = "pti19_20"
    ANIMAL_ON_THE_LINE = "animalOnTheLine"
    PTI19_21 = "pti19_21"
    ROUTE_DIVERSION = "routeDiversion"
    PTI19_22 = "pti19_22"
    ROAD_CLOSED = "roadClosed"
    PTI19_23 = "pti19_23"
    ROADWORKS = "roadworks"
    PTI19_23_ALIAS_1 = "pti19_23_Alias_1"
    SEWERAGE_MAINTENANCE = "sewerageMaintenance"
    PTI19_23_ALIAS_2 = "pti19_23_Alias_2"
    ROAD_MAINTENANCE = "roadMaintenance"
    PTI19_23_ALIAS_3 = "pti19_23_Alias_3"
    ASPHALTING = "asphalting"
    PTI19_23_ALIAS_4 = "pti19_23_Alias_4"
    PAVING = "paving"
    PTI19_24 = "pti19_24"
    SPECIAL_EVENT = "specialEvent"
    PTI19_24_ALIAS_1 = "pti19_24_Alias_1"
    MARCH = "march"
    PTI19_24_ALIAS_2 = "pti19_24_Alias_2"
    PROCESSION = "procession"
    PTI19_24_ALIAS_3 = "pti19_24_Alias_3"
    DEMONSTRATION = "demonstration"
    PTI19_24_ALIAS_4 = "pti19_24_Alias_4"
    PUBLIC_DISTURBANCE = "publicDisturbance"
    PTI19_24_ALIAS_5 = "pti19_24_Alias_5"
    FILTER_BLOCKADE = "filterBlockade"
    PTI19_24_ALIAS_6 = "pti19_24_Alias_6"
    SIGHTSEERS_OBSTRUCTING_ACCESS = "sightseersObstructingAccess"
    PTI19_24_ALIAS_7 = "pti19_24_Alias_7"
    HOLIDAY = "holiday"
    PTI19_25 = "pti19_25"
    BRIDGE_STRIKE = "bridgeStrike"
    PTI19_25_ALIAS_1 = "pti19_25_Alias_1"
    VIADUCT_FAILURE = "viaductFailure"
    PTI19_26 = "pti19_26"
    OVERHEAD_OBSTRUCTION = "overheadObstruction"
    PTI19_27 = "pti19_27"
    UNDEFINED_PROBLEM = "undefinedProblem"
    PTI19_15_ALIAS_1 = "pti19_15_Alias_1"
    PROBLEMS_AT_BORDER_POST = "problemsAtBorderPost"
    PTI19_15_ALIAS_2 = "pti19_15_Alias_2"
    PROBLEMS_AT_CUSTOMS_POST = "problemsAtCustomsPost"
    PTI19_15_ALIAS_3 = "pti19_15_Alias_3"
    SPEED_RESTRICTIONS = "speedRestrictions"
    PTI19_255_ALIAS_1 = "pti19_255_Alias_1"
    LOGISTIC_PROBLEMS = "logisticProblems"
    PTI19_255_ALIAS_2 = "pti19_255_Alias_2"
    PROBLEMS_ON_LOCAL_ROAD = "problemsOnLocalRoad"
