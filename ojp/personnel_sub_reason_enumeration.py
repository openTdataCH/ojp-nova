from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class PersonnelSubReasonEnumeration(Enum):
    """
    Values for Personnel incident sub reason types.

    :cvar STAFF_SICKNESS:
    :cvar UNKNOWN: TPEG Pti20_0 unknown.
    :cvar STAFF_INJURY:
    :cvar CONTRACTOR_STAFF_INJURY: contractor staff injury alias to TPEG
        Pti20_1 staff sickness.
    :cvar STAFF_ABSENCE: TPEG Pti20_2 staff absence.
    :cvar STAFF_IN_WRONG_PLACE: TPEG Pti20_3 staff in wrong place.
    :cvar STAFF_SHORTAGE: TPEG Pti20_4 staff shortage.
    :cvar INDUSTRIAL_ACTION: TPEG Pti20_5 industrial action.
    :cvar UNOFFICIAL_INDUSTRIAL_ACTION:
    :cvar WORK_TO_RULE: TPEG Pti20_6 work to rule.
    :cvar UNDEFINED_PERSONNEL_PROBLEM: TPEG Pti20_255 undefined
        personnel problem.
    """
    STAFF_SICKNESS = "staffSickness"
    UNKNOWN = "unknown"
    STAFF_INJURY = "staffInjury"
    CONTRACTOR_STAFF_INJURY = "contractorStaffInjury"
    STAFF_ABSENCE = "staffAbsence"
    STAFF_IN_WRONG_PLACE = "staffInWrongPlace"
    STAFF_SHORTAGE = "staffShortage"
    INDUSTRIAL_ACTION = "industrialAction"
    UNOFFICIAL_INDUSTRIAL_ACTION = "unofficialIndustrialAction"
    WORK_TO_RULE = "workToRule"
    UNDEFINED_PERSONNEL_PROBLEM = "undefinedPersonnelProblem"
