from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class MiscellaneousSubReasonEnumeration(Enum):
    """
    Values for Miscellaneous incident sub reason types.

    :cvar UNKNOWN: TPEG Pti_19_0 unknown
    :cvar PREVIOUS_DISTURBANCES: 19:0_1 Previous disturbances - alias to
        TPEG Pti_19_0 unknown
    :cvar INCIDENT: TPEG Pti_19_1 incident.
    :cvar SAFETY_VIOLATION: 19:1_1 Near Miss - alias to TPEG Pti_19_1
        incident.
    :cvar NEAR_MISS: 19:1_2 Near Miss - alias to TPEG Pti_19_1 incident.
    :cvar SIGNAL_PASSED_AT_DANGER: 19:1_3 Signal passed at danger -
        alias to TPEG Pti_19_1 incident.
    :cvar STATION_OVERRUN: 19:1_4 Station overrun - alias to TPEG
        Pti_19_1 incident.
    :cvar TRAIN_DOOR: 19:1_5  trainDoor- alias to TPEG Pti_19_1
        incident.
    :cvar BOMB_EXPLOSION: TPEG Pti_19_2 bomb explosion.
    :cvar SECURITY_ALERT: TPEG Pti_19_3 security alert.
    :cvar EMERGENCY_SERVICES_CALL: 19:1_6 Unspecified emergency service
        visit. Alias to pti19
    :cvar POLICE_REQUEST: 19:3_1 Request of the police Alias to TPEG
        Pti_19_3 security alert.
    :cvar FIRE_BRIGADE_SAFETY_CHECKS: 19:3_2 Fire brigade safety
        checksAlias to TPEG Pti_19_3 security alert.
    :cvar UNATTENDED_BAG: 19:3_3 An unattended bag TPEG Pti_19_3
        security alert.
    :cvar TELEPHONED_THREAT: 19:3_4 Telephoned threat TPEG Pti_19_3
        security alert.
    :cvar SUSPECT_VEHICLE: 19:3_5 telephoned threat TPEG Pti_19_3
        security alert.
    :cvar CIVIL_EMERGENCY: 19:3_6 Civil Emergency Pti_19_3 security
        alert
    :cvar AIR_RAID: 19:3_7 Air Raid Pti_19_3 security alert
    :cvar SABOTAGE: 19:3_8 Sabotage Pti_19_3 security alert
    :cvar BOMB_ALERT: 19:3_9 Bomb alert Pti_19_3 security alert
    :cvar ATTACK: 19:3_10 Attack Pti_19_3 security alert
    :cvar EVACUATION: 19:3_11 EvacuationPti_19_3 security alert
    :cvar TERRORIST_INCIDENT: 19:3_12 terrorist Incident Pti_19_3
        security alert
    :cvar GUNFIRE_ON_ROADWAY:
    :cvar EXPLOSION: 19:3_14 Explosion Pti_19_3 security alert
    :cvar EXPLOSION_HAZARD: 19:3_15 explosion Hazard Pti_19_3 security
        alert
    :cvar SECURITY_INCIDENT: 19:3_16 security Incident Pti_19_3 security
        alert
    :cvar FIRE_BRIGADE_ORDER: 19:3_17 terrorist Incident Pti_19_3
        security alert
    :cvar POLICE_ACTIVITY: 19:3_18 terrorist Incident Pti_19_3 security
        alert
    :cvar FIRE: TPEG Pti_19_4 fire
    :cvar LINESIDE_FIRE: linesideFire alias to TPEG Pti_19_4 fire.
    :cvar VANDALISM: TPEG Pti_19_5 vandalism
    :cvar PASSENGER_ACTION: 19:5_1 passengerActionAlias to pti19_5
        vandalism
    :cvar STAFF_ASSAULT: 19:5_2 Assault on staft.Alias to pti19_5
        vandalism
    :cvar RAILWAY_CRIME: 19:5_3 Railway Crime Alias to pti19_5 vandalism
    :cvar THEFT: 19:5_4 theft to pti19_5 vandalism
    :cvar ALTERCATION: 19:1_7Railway Crime Alias to pti19_1 incident
    :cvar ILL_VEHICLE_OCCUPANTS: 19:1_8 Railway Crime Alias to pti19_1
        incident
    :cvar ACCIDENT: PEG Pti_19_6 accident
    :cvar FATALITY: 19:6_1 fatality alias to TPEG Pti_19_6 accident.
    :cvar PERSON_UNDER_TRAIN: 19:6_2 a person under a train - alias to
        TPEG Pti_19_6 accident.
    :cvar PERSON_HIT_BY_TRAIN: 19:6_3 a person hit by a train - alias to
        TPEG Pti_19_6 accident.
    :cvar PERSON_ILL_ON_VEHICLE: 19:6_4 person ill On Vehicle -Alias to
        pti19_6 accident.
    :cvar EMERGENCY_SERVICES: 19:6_5 emergencyServices - alias to TPEG
        Pti_19_6 accident.
    :cvar COLLISION: 19:6_6 Collision - Alias to pti19_6 accident.
    :cvar OVERCROWDED: TPEG Pti_19_07 overcrowded
    :cvar INSUFFICIENT_DEMAND: TPEG Pti_19_08 insufficientDemand
    :cvar LIGHTING_FAILURE: TPEG Pti_19_09 lightingFailure
    :cvar LEADER_BOARD_FAILURE: TPEG Pti_19_10 leaderBoardFailure
    :cvar SERVICE_INDICATOR_FAILURE: TPEG Pti_19_11
        serviceIndicatorFailure
    :cvar SERVICE_FAILURE: TPEG Pti_19_12 serviceFailure
    :cvar OPERATOR_CEASED_TRADING: TPEG Pti_19_13 operatorCeasedTrading
    :cvar OPERATOR_SUSPENDED: TPEG Pti_19_14 operatorSuspended
    :cvar CONGESTION: TPEG Pti_19_15 congestion
    :cvar ROUTE_BLOCKAGE: TPEG Pti_19_16 routeBlockage
    :cvar PERSON_ON_THE_LINE: TPEG Pti_19_17 personOnTheLine
    :cvar VEHICLE_ON_THE_LINE: TPEG Pti_19_18 vehicleOnTheLine
    :cvar OBJECT_ON_THE_LINE: TPEG Pti_19_19 objectOnTheLine
    :cvar FALLEN_TREE_ON_THE_LINE: 19:19_1 fallen tree on line- alias to
        TPEG Pti_19_19 object on the line.
    :cvar VEGETATION: 19:19_2 Vegetation - alias to TPEG Pti_19_19
        object on the line.
    :cvar TRAIN_STRUCK_ANIMAL: 19:19_3 Train struck animal alias to TPEG
        Pti_19_19 object on the line.
    :cvar TRAIN_STRUCK_OBJECT: 19:19_4 Train struck object alias to TPEG
        Pti_19_19 object on the line.
    :cvar LEVEL_CROSSING_INCIDENT: 19:18_1 Level Crossing Incident -
        alias to TPEG Pti_19_18 VEHICLE on the line.
    :cvar ANIMAL_ON_THE_LINE: TPEG Pti_19_20 animal on the line.
    :cvar ROUTE_DIVERSION: TPEG Pti_19_21 route diversion.
    :cvar ROAD_CLOSED: TPEG Pti_19_22 road closed.
    :cvar ROADWORKS: TPEG Pti_19_23 roadworks.
    :cvar SEWERAGE_MAINTENANCE: 19:23_1 sewerageMaintenance - alias to
        TPEG Pti_19_23 roadworks..
    :cvar ROAD_MAINTENANCE: 19:23_2 roadMaintenance - alias to TPEG
        Pti_19_23 roadworks..
    :cvar ASPHALTING: 19:23_3 asphalting - alias to TPEG Pti_19_23
        roadworks..
    :cvar PAVING: 19:23_4 paving - alias to TPEG Pti_19_23 roadworks..
    :cvar SPECIAL_EVENT: TPEG Pti_19_24 special event.
    :cvar MARCH: 19:24_1 march - alias to TPEG Pti_19_24 specialEvent
    :cvar PROCESSION: 19:24_2 procession - alias to TPEG Pti_19_24
        specialEvent
    :cvar DEMONSTRATION: 19:24_3 demonstration - alias to TPEG Pti_19_24
        specialEvent
    :cvar PUBLIC_DISTURBANCE: 19:24_4 publicDisturbance - alias to TPEG
        Pti_19_24 specialEvent
    :cvar FILTER_BLOCKADE: 19:24_5 filterBlockade - alias to TPEG
        Pti_19_24 specialEvent
    :cvar SIGHTSEERS_OBSTRUCTING_ACCESS: 19:24_6
        sightseersObstructingAccess - alias to TPEG Pti_19_24
        specialEvent
    :cvar HOLIDAY: 19:24_7 sightseersObstructingAccess - alias to TPEG
        Pti_19_24 specialEvent
    :cvar BRIDGE_STRIKE: TPEG Pti_19_25 bridge strike.
    :cvar VIADUCT_FAILURE: 19:25_1 viaductFailure - alias to TPEG
        Pti_19_24 bridgeStrike
    :cvar OVERHEAD_OBSTRUCTION: TPEG Pti_19_26 overhead obstruction.
    :cvar UNDEFINED_PROBLEM: TPEG Pti_19_255 undefined problem.
    :cvar PROBLEMS_AT_BORDER_POST: 19:15_1 problemsAtBorderPost - alias
        to TPEG Pti_19_15 congestion.
    :cvar PROBLEMS_AT_CUSTOMS_POST: 19:15_2 problemsAtCustomsPost alias
        to TPEG Pti_19_15 congestion.
    :cvar PROBLEMS_ON_LOCAL_ROAD: 19:15_3 problemsOnLocalRoad alias to
        TPEG Pti_19_15 congestion.
    :cvar SPEED_RESTRICTIONS: 19:255_1 speedRestrictions alias to TPEG
        Pti_19_15 unknown
    :cvar LOGISTIC_PROBLEMS: 19:255_2 logisticProblems alias to TPEG
        Pti_19_15 unknown
    """
    UNKNOWN = "unknown"
    PREVIOUS_DISTURBANCES = "previousDisturbances"
    INCIDENT = "incident"
    SAFETY_VIOLATION = "safetyViolation"
    NEAR_MISS = "nearMiss"
    SIGNAL_PASSED_AT_DANGER = "signalPassedAtDanger"
    STATION_OVERRUN = "stationOverrun"
    TRAIN_DOOR = "trainDoor"
    BOMB_EXPLOSION = "bombExplosion"
    SECURITY_ALERT = "securityAlert"
    EMERGENCY_SERVICES_CALL = "emergencyServicesCall"
    POLICE_REQUEST = "policeRequest"
    FIRE_BRIGADE_SAFETY_CHECKS = "fireBrigadeSafetyChecks"
    UNATTENDED_BAG = "unattendedBag"
    TELEPHONED_THREAT = "telephonedThreat"
    SUSPECT_VEHICLE = "suspectVehicle"
    CIVIL_EMERGENCY = "civilEmergency"
    AIR_RAID = "airRaid"
    SABOTAGE = "sabotage"
    BOMB_ALERT = "bombALert"
    ATTACK = "attack"
    EVACUATION = "evacuation"
    TERRORIST_INCIDENT = "terroristIncident"
    GUNFIRE_ON_ROADWAY = "gunfireOnRoadway"
    EXPLOSION = "explosion"
    EXPLOSION_HAZARD = "explosionHazard"
    SECURITY_INCIDENT = "securityIncident"
    FIRE_BRIGADE_ORDER = "fireBrigadeOrder"
    POLICE_ACTIVITY = "policeActivity"
    FIRE = "fire"
    LINESIDE_FIRE = "linesideFire"
    VANDALISM = "vandalism"
    PASSENGER_ACTION = "passengerAction"
    STAFF_ASSAULT = "staffAssault"
    RAILWAY_CRIME = "railwayCrime"
    THEFT = "theft"
    ALTERCATION = "altercation"
    ILL_VEHICLE_OCCUPANTS = "illVehicleOccupants"
    ACCIDENT = "accident"
    FATALITY = "fatality"
    PERSON_UNDER_TRAIN = "personUnderTrain"
    PERSON_HIT_BY_TRAIN = "personHitByTrain"
    PERSON_ILL_ON_VEHICLE = "personIllOnVehicle"
    EMERGENCY_SERVICES = "emergencyServices"
    COLLISION = "collision"
    OVERCROWDED = "overcrowded"
    INSUFFICIENT_DEMAND = "insufficientDemand"
    LIGHTING_FAILURE = "lightingFailure"
    LEADER_BOARD_FAILURE = "leaderBoardFailure"
    SERVICE_INDICATOR_FAILURE = "serviceIndicatorFailure"
    SERVICE_FAILURE = "serviceFailure"
    OPERATOR_CEASED_TRADING = "operatorCeasedTrading"
    OPERATOR_SUSPENDED = "operatorSuspended"
    CONGESTION = "congestion"
    ROUTE_BLOCKAGE = "routeBlockage"
    PERSON_ON_THE_LINE = "personOnTheLine"
    VEHICLE_ON_THE_LINE = "vehicleOnTheLine"
    OBJECT_ON_THE_LINE = "objectOnTheLine"
    FALLEN_TREE_ON_THE_LINE = "fallenTreeOnTheLine"
    VEGETATION = "vegetation"
    TRAIN_STRUCK_ANIMAL = "trainStruckAnimal"
    TRAIN_STRUCK_OBJECT = "trainStruckObject"
    LEVEL_CROSSING_INCIDENT = "levelCrossingIncident"
    ANIMAL_ON_THE_LINE = "animalOnTheLine"
    ROUTE_DIVERSION = "routeDiversion"
    ROAD_CLOSED = "roadClosed"
    ROADWORKS = "roadworks"
    SEWERAGE_MAINTENANCE = "sewerageMaintenance"
    ROAD_MAINTENANCE = "roadMaintenance"
    ASPHALTING = "asphalting"
    PAVING = "paving"
    SPECIAL_EVENT = "specialEvent"
    MARCH = "march"
    PROCESSION = "procession"
    DEMONSTRATION = "demonstration"
    PUBLIC_DISTURBANCE = "publicDisturbance"
    FILTER_BLOCKADE = "filterBlockade"
    SIGHTSEERS_OBSTRUCTING_ACCESS = "sightseersObstructingAccess"
    HOLIDAY = "holiday"
    BRIDGE_STRIKE = "bridgeStrike"
    VIADUCT_FAILURE = "viaductFailure"
    OVERHEAD_OBSTRUCTION = "overheadObstruction"
    UNDEFINED_PROBLEM = "undefinedProblem"
    PROBLEMS_AT_BORDER_POST = "problemsAtBorderPost"
    PROBLEMS_AT_CUSTOMS_POST = "problemsAtCustomsPost"
    PROBLEMS_ON_LOCAL_ROAD = "problemsOnLocalRoad"
    SPEED_RESTRICTIONS = "speedRestrictions"
    LOGISTIC_PROBLEMS = "logisticProblems"
