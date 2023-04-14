from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class EquipmentReasonEnumeration(Enum):
    """
    Values for Equipment incident reason types TPEG Pti18_3/TPEG Pti_21.

    :cvar PTI21_0:
    :cvar UNKNOWN: TPEG Pti21_0 unknown.
    :cvar PTI21_1:
    :cvar POINTS_PROBLEM: TPEG Pti21_1 points problem.
    :cvar PTI21_2:
    :cvar POINTS_FAILURE: TPEG Pti21_2 points failure.
    :cvar PTI21_3:
    :cvar SIGNAL_PROBLEM: TPEG Pti21_3 signal problem.
    :cvar PTI21_3_ALIAS_1:
    :cvar TRAIN_WARNING_SYSTEM_PROBLEM: Train warning system eg
        TPWSAlias to TPEG Pti21_3 signal problem.
    :cvar PTI21_3_ALIAS_2:
    :cvar TRACK_CIRCUIT_PROBLEM: Track circuit alias to TPEG Pti21_3
        signal problem.
    :cvar PTI21_4:
    :cvar SIGNAL_FAILURE: TPEG Pti21_4 signal failure.
    :cvar PTI21_4_ALIAS_1:
    :cvar SIGNAL_AND_SWITCH_FAILURE: TPEG Pti21_4 signal failure.
    :cvar PTI21_5:
    :cvar DERAILMENT: TPEG Pti21_5 derailment.
    :cvar PTI21_6:
    :cvar ENGINE_FAILURE: TPEG Pti21_6 engine failure.
    :cvar PTI21_6_ALIAS_1:
    :cvar TRACTION_FAILURE: traction failure alais to TPEG Pti21_6
        engine failure.
    :cvar PTI21_7:
    :cvar BREAK_DOWN: TPEG Pti21_7 break down.
    :cvar PTI21_8:
    :cvar TECHNICAL_PROBLEM: TPEG Pti21_8 technical problem.
    :cvar PTI21_8_ALIAS_1:
    :cvar BROKEN_RAIL: Broken rail - alias to TPEG Pti21_8 technical
        problem.
    :cvar PTI21_8_ALIAS_2:
    :cvar POOR_RAIL_CONDITIONS: poor rail conditions - alias to TPEG
        Pti21_8 technical problem.
    :cvar PTI21_8_ALIAS_3:
    :cvar WHEEL_IMPACT_LOAD: Wheel Impact Load detectedi by trackside
        equipment alias to TPEG Pti21_8 technical problem.
    :cvar PTI21_8_ALIAS_4:
    :cvar LACK_OF_OPERATIONAL_STOCK: late lack of operational stock -
        alias to TPEG Pti21_8 technical problem.
    :cvar PTI21_8_ALIAS_5:
    :cvar DEFECTIVE_FIRE_ALARM_EQUIPMENT: defective fire alarm equipment
        - alias to TPEG Pti21_8 technical problem.
    :cvar PTI21_8_ALIAS_6:
    :cvar DEFECTIVE_PLATFORM_EDGE_DOORS: defective PEDs (platform edge
        doors) - alias to TPEG Pti21_8 technical problem.
    :cvar PTI21_8_ALIAS_7:
    :cvar DEFECTIVE_CCTV: defective CCTV - alias to TPEG Pti21_8
        technical problem.
    :cvar PTI21_8_ALIAS_8:
    :cvar DEFECTIVE_PUBLIC_ANNOUNCEMENT_SYSTEM: defective PA - alias to
        TPEG Pti21_8 technical problem.
    :cvar PTI21_8_ALIAS_9:
    :cvar TICKETING_SYSTEM_NOT_AVAILABLE: ticketing facility unavailable
        - alias to TPEG Pti21_8 technical problem.
    :cvar PTI21_8_ALIAS_10:
    :cvar LEVE_CROSSING_FAILURE: ticketing facility unavailable - alias
        to TPEG Pti21_8 technical problem.
    :cvar PTI21_9:
    :cvar REPAIR_WORK: TPEG Pti21_9 repair work.
    :cvar PTI21_10:
    :cvar CONSTRUCTION_WORK: TPEG Pti21_10 construction work.
    :cvar PTI21_11:
    :cvar MAINTENANCE_WORK: TPEG Pti21_11 maintenance work.
    :cvar PTI21_11_ALIAS_1:
    :cvar EMERGENCY_ENGINEERING_WORK: emergency engineering work - alias
        to TPEG Pti21_11 maintenance work.
    :cvar PTI21_11_ALIAS_2:
    :cvar LATE_FINISH_TO_ENGINEERING_WORK: late finish to engineering
        work - alias to TPEG Pti21_11 maintenance work.
    :cvar PTI21_12:
    :cvar POWER_PROBLEM: TPEG Pti21_12 power problem.
    :cvar PTI21_12_ALIAS_1:
    :cvar OVEHEAD_WIRE_FAILURE: TPEG Pti21_12 power problem.
    :cvar PTI21_13:
    :cvar FUEL_PROBLEM: TPEG Pti21_13 fuel problem.
    :cvar PTI21_14:
    :cvar SWING_BRIDGE_FAILURE: TPEG Pti21_14 swing bridge failure.
    :cvar PTI21_15:
    :cvar ESCALATOR_FAILURE: TPEG Pti21_15 escalator failure.
    :cvar PTI21_16:
    :cvar LIFT_FAILURE: TPEG Pti21_16 lift failure.
    :cvar PTI21_17:
    :cvar GANGWAY_PROBLEM: TPEG Pti21_17 gangway problem.
    :cvar PTI21_18:
    :cvar CLOSED_FOR_MAINTENANCE: TPEG Pti21_18 closed for maintenance.
    :cvar PTI21_19:
    :cvar FUEL_SHORTAGE: TPEG Pti21_19 fuel shortage.
    :cvar PTI21_20:
    :cvar DEICING_WORK: TPEG Pti21_20 de-icing work.
    :cvar PTI21_21:
    :cvar WHEEL_PROBLEM: TPEG Pti21_21 wheel problem.
    :cvar PTI21_21_ALIAS_1:
    :cvar SLIPPERY_TRACK: TPEG Pti21_21 wheel problem.
    :cvar PTI21_22:
    :cvar LUGGAGE_CAROUSEL_PROBLEM: TPEG Pti21_22 luggage carousel
        problem.
    :cvar PTI21_255:
    :cvar UNDEFINED_EQUIPMENT_PROBLEM: TPEG Pti21_255 undefined
        equipment problem.
    """
    PTI21_0 = "pti21_0"
    UNKNOWN = "unknown"
    PTI21_1 = "pti21_1"
    POINTS_PROBLEM = "pointsProblem"
    PTI21_2 = "pti21_2"
    POINTS_FAILURE = "pointsFailure"
    PTI21_3 = "pti21_3"
    SIGNAL_PROBLEM = "signalProblem"
    PTI21_3_ALIAS_1 = "pti21_3_Alias_1"
    TRAIN_WARNING_SYSTEM_PROBLEM = "trainWarningSystemProblem"
    PTI21_3_ALIAS_2 = "pti21_3_Alias_2"
    TRACK_CIRCUIT_PROBLEM = "trackCircuitProblem"
    PTI21_4 = "pti21_4"
    SIGNAL_FAILURE = "signalFailure"
    PTI21_4_ALIAS_1 = "pti21_4_Alias_1"
    SIGNAL_AND_SWITCH_FAILURE = "signalAndSwitchFailure"
    PTI21_5 = "pti21_5"
    DERAILMENT = "derailment"
    PTI21_6 = "pti21_6"
    ENGINE_FAILURE = "engineFailure"
    PTI21_6_ALIAS_1 = "pti21_6_Alias_1"
    TRACTION_FAILURE = "tractionFailure"
    PTI21_7 = "pti21_7"
    BREAK_DOWN = "breakDown"
    PTI21_8 = "pti21_8"
    TECHNICAL_PROBLEM = "technicalProblem"
    PTI21_8_ALIAS_1 = "pti21_8_Alias_1"
    BROKEN_RAIL = "brokenRail"
    PTI21_8_ALIAS_2 = "pti21_8_Alias_2"
    POOR_RAIL_CONDITIONS = "poorRailConditions"
    PTI21_8_ALIAS_3 = "pti21_8_Alias_3"
    WHEEL_IMPACT_LOAD = "wheelImpactLoad"
    PTI21_8_ALIAS_4 = "pti21_8_Alias_4"
    LACK_OF_OPERATIONAL_STOCK = "lackOfOperationalStock"
    PTI21_8_ALIAS_5 = "pti21_8_Alias_5"
    DEFECTIVE_FIRE_ALARM_EQUIPMENT = "defectiveFireAlarmEquipment"
    PTI21_8_ALIAS_6 = "pti21_8_Alias_6"
    DEFECTIVE_PLATFORM_EDGE_DOORS = "defectivePlatformEdgeDoors"
    PTI21_8_ALIAS_7 = "pti21_8_Alias_7"
    DEFECTIVE_CCTV = "defectiveCctv"
    PTI21_8_ALIAS_8 = "pti21_8_Alias_8"
    DEFECTIVE_PUBLIC_ANNOUNCEMENT_SYSTEM = "defectivePublicAnnouncementSystem"
    PTI21_8_ALIAS_9 = "pti21_8_Alias_9"
    TICKETING_SYSTEM_NOT_AVAILABLE = "ticketingSystemNotAvailable"
    PTI21_8_ALIAS_10 = "pti21_8_Alias_10"
    LEVE_CROSSING_FAILURE = "leveCrossingFailure"
    PTI21_9 = "pti21_9"
    REPAIR_WORK = "repairWork"
    PTI21_10 = "pti21_10"
    CONSTRUCTION_WORK = "constructionWork"
    PTI21_11 = "pti21_11"
    MAINTENANCE_WORK = "maintenanceWork"
    PTI21_11_ALIAS_1 = "pti21_11_Alias_1"
    EMERGENCY_ENGINEERING_WORK = "emergencyEngineeringWork"
    PTI21_11_ALIAS_2 = "pti21_11_Alias_2"
    LATE_FINISH_TO_ENGINEERING_WORK = "lateFinishToEngineeringWork"
    PTI21_12 = "pti21_12"
    POWER_PROBLEM = "powerProblem"
    PTI21_12_ALIAS_1 = "pti21_12_Alias_1"
    OVEHEAD_WIRE_FAILURE = "oveheadWireFailure"
    PTI21_13 = "pti21_13"
    FUEL_PROBLEM = "fuelProblem"
    PTI21_14 = "pti21_14"
    SWING_BRIDGE_FAILURE = "swingBridgeFailure"
    PTI21_15 = "pti21_15"
    ESCALATOR_FAILURE = "escalatorFailure"
    PTI21_16 = "pti21_16"
    LIFT_FAILURE = "liftFailure"
    PTI21_17 = "pti21_17"
    GANGWAY_PROBLEM = "gangwayProblem"
    PTI21_18 = "pti21_18"
    CLOSED_FOR_MAINTENANCE = "closedForMaintenance"
    PTI21_19 = "pti21_19"
    FUEL_SHORTAGE = "fuelShortage"
    PTI21_20 = "pti21_20"
    DEICING_WORK = "deicingWork"
    PTI21_21 = "pti21_21"
    WHEEL_PROBLEM = "wheelProblem"
    PTI21_21_ALIAS_1 = "pti21_21_Alias_1"
    SLIPPERY_TRACK = "slipperyTrack"
    PTI21_22 = "pti21_22"
    LUGGAGE_CAROUSEL_PROBLEM = "luggageCarouselProblem"
    PTI21_255 = "pti21_255"
    UNDEFINED_EQUIPMENT_PROBLEM = "undefinedEquipmentProblem"
