from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class EquipmentSubReasonEnumeration(Enum):
    """
    Values for Equipment incident sub reason types.

    :cvar UNKNOWN: TPEG Pti21_0 unknown.
    :cvar POINTS_PROBLEM: TPEG Pti21_1 points problem.
    :cvar POINTS_FAILURE: TPEG Pti21_2 points failure.
    :cvar SIGNAL_PROBLEM: TPEG Pti21_3 signal problem.
    :cvar TRAIN_WARNING_SYSTEM_PROBLEM: Train warning system eg
        TPWSAlias to TPEG Pti21_3 signal problem.
    :cvar TRACK_CIRCUIT_PROBLEM: Track circuit alias to TPEG Pti21_3
        signal problem.
    :cvar SIGNAL_FAILURE: TPEG Pti21_4 signal failure.
    :cvar SIGNAL_AND_SWITCH_FAILURE: TPEG Pti21_4 signal failure.
    :cvar DERAILMENT: TPEG Pti21_5 derailment.
    :cvar ENGINE_FAILURE: TPEG Pti21_6 engine failure.
    :cvar TRACTION_FAILURE: traction failure alais to TPEG Pti21_6
        engine failure.
    :cvar BREAK_DOWN: TPEG Pti21_7 break down.
    :cvar TECHNICAL_PROBLEM: TPEG Pti21_8 technical problem.
    :cvar BROKEN_RAIL: Broken rail - alias to TPEG Pti21_8 technical
        problem.
    :cvar POOR_RAIL_CONDITIONS: poor rail conditions - alias to TPEG
        Pti21_8 technical problem.
    :cvar WHEEL_IMPACT_LOAD: Wheel Impact Load detectedi by trackside
        equipment alias to TPEG Pti21_8 technical problem.
    :cvar LACK_OF_OPERATIONAL_STOCK: late lack of operational stock -
        alias to TPEG Pti21_8 technical problem.
    :cvar DEFECTIVE_FIRE_ALARM_EQUIPMENT: defective fire alarm equipment
        - alias to TPEG Pti21_8 technical problem.
    :cvar DEFECTIVE_PLATFORM_EDGE_DOORS: defective PEDs (platform edge
        doors) - alias to TPEG Pti21_8 technical problem.
    :cvar DEFECTIVE_CCTV: defective CCTV - alias to TPEG Pti21_8
        technical problem.
    :cvar DEFECTIVE_PUBLIC_ANNOUNCEMENT_SYSTEM: defective PA - alias to
        TPEG Pti21_8 technical problem.
    :cvar TICKETING_SYSTEM_NOT_AVAILABLE: ticketing facility unavailable
        - alias to TPEG Pti21_8 technical problem.
    :cvar LEVE_CROSSING_FAILURE: ticketing facility unavailable - alias
        to TPEG Pti21_8 technical problem.
    :cvar REPAIR_WORK: TPEG Pti21_9 repair work.
    :cvar CONSTRUCTION_WORK: TPEG Pti21_10 construction work.
    :cvar MAINTENANCE_WORK: TPEG Pti21_11 maintenance work.
    :cvar EMERGENCY_ENGINEERING_WORK: emergency engineering work - alias
        to TPEG Pti21_11 maintenance work.
    :cvar LATE_FINISH_TO_ENGINEERING_WORK: late finish to engineering
        work - alias to TPEG Pti21_11 maintenance work.
    :cvar POWER_PROBLEM: TPEG Pti21_12 power problem.
    :cvar OVEHEAD_WIRE_FAILURE: TPEG Pti21_12 power problem.
    :cvar FUEL_PROBLEM: TPEG Pti21_13 fuel problem.
    :cvar SWING_BRIDGE_FAILURE: TPEG Pti21_14 swing bridge failure.
    :cvar ESCALATOR_FAILURE: TPEG Pti21_15 escalator failure.
    :cvar LIFT_FAILURE: TPEG Pti21_16 lift failure.
    :cvar GANGWAY_PROBLEM: TPEG Pti21_17 gangway problem.
    :cvar CLOSED_FOR_MAINTENANCE: TPEG Pti21_18 closed for maintenance.
    :cvar FUEL_SHORTAGE: TPEG Pti21_19 fuel shortage.
    :cvar DEICING_WORK: TPEG Pti21_20 de-icing work.
    :cvar WHEEL_PROBLEM: TPEG Pti21_21 wheel problem.
    :cvar SLIPPERY_TRACK: TPEG Pti21_21 wheel problem.
    :cvar LUGGAGE_CAROUSEL_PROBLEM: TPEG Pti21_22 luggage carousel
        problem.
    :cvar UNDEFINED_EQUIPMENT_PROBLEM: TPEG Pti21_255 undefined
        equipment problem.
    """
    UNKNOWN = "unknown"
    POINTS_PROBLEM = "pointsProblem"
    POINTS_FAILURE = "pointsFailure"
    SIGNAL_PROBLEM = "signalProblem"
    TRAIN_WARNING_SYSTEM_PROBLEM = "trainWarningSystemProblem"
    TRACK_CIRCUIT_PROBLEM = "trackCircuitProblem"
    SIGNAL_FAILURE = "signalFailure"
    SIGNAL_AND_SWITCH_FAILURE = "signalAndSwitchFailure"
    DERAILMENT = "derailment"
    ENGINE_FAILURE = "engineFailure"
    TRACTION_FAILURE = "tractionFailure"
    BREAK_DOWN = "breakDown"
    TECHNICAL_PROBLEM = "technicalProblem"
    BROKEN_RAIL = "brokenRail"
    POOR_RAIL_CONDITIONS = "poorRailConditions"
    WHEEL_IMPACT_LOAD = "wheelImpactLoad"
    LACK_OF_OPERATIONAL_STOCK = "lackOfOperationalStock"
    DEFECTIVE_FIRE_ALARM_EQUIPMENT = "defectiveFireAlarmEquipment"
    DEFECTIVE_PLATFORM_EDGE_DOORS = "defectivePlatformEdgeDoors"
    DEFECTIVE_CCTV = "defectiveCctv"
    DEFECTIVE_PUBLIC_ANNOUNCEMENT_SYSTEM = "defectivePublicAnnouncementSystem"
    TICKETING_SYSTEM_NOT_AVAILABLE = "ticketingSystemNotAvailable"
    LEVE_CROSSING_FAILURE = "leveCrossingFailure"
    REPAIR_WORK = "repairWork"
    CONSTRUCTION_WORK = "constructionWork"
    MAINTENANCE_WORK = "maintenanceWork"
    EMERGENCY_ENGINEERING_WORK = "emergencyEngineeringWork"
    LATE_FINISH_TO_ENGINEERING_WORK = "lateFinishToEngineeringWork"
    POWER_PROBLEM = "powerProblem"
    OVEHEAD_WIRE_FAILURE = "oveheadWireFailure"
    FUEL_PROBLEM = "fuelProblem"
    SWING_BRIDGE_FAILURE = "swingBridgeFailure"
    ESCALATOR_FAILURE = "escalatorFailure"
    LIFT_FAILURE = "liftFailure"
    GANGWAY_PROBLEM = "gangwayProblem"
    CLOSED_FOR_MAINTENANCE = "closedForMaintenance"
    FUEL_SHORTAGE = "fuelShortage"
    DEICING_WORK = "deicingWork"
    WHEEL_PROBLEM = "wheelProblem"
    SLIPPERY_TRACK = "slipperyTrack"
    LUGGAGE_CAROUSEL_PROBLEM = "luggageCarouselProblem"
    UNDEFINED_EQUIPMENT_PROBLEM = "undefinedEquipmentProblem"
