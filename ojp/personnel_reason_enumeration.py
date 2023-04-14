from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class PersonnelReasonEnumeration(Enum):
    """
    Values for Personnel incident reason types TPEG Pti18_2/TPEG Pti_20.

    :cvar PTI20_0:
    :cvar UNKNOWN: TPEG Pti20_0 unknown.
    :cvar PTI20_1:
    :cvar STAFF_SICKNESS: TPEG Pti20_1 staff sickness.
    :cvar PTI20_1_ALIAS_1:
    :cvar STAFF_INJURY: staff injury alias to TPEG Pti20_1 staff
        sickness.
    :cvar PTI20_1_ALIAS_2:
    :cvar CONTRACTOR_STAFF_INJURY: contractor staff injury alias to TPEG
        Pti20_1 staff sickness.
    :cvar PTI20_2:
    :cvar STAFF_ABSENCE: TPEG Pti20_2 staff absence.
    :cvar PTI20_3:
    :cvar STAFF_IN_WRONG_PLACE: TPEG Pti20_3 staff in wrong place.
    :cvar PTI20_4:
    :cvar STAFF_SHORTAGE: TPEG Pti20_4 staff shortage.
    :cvar PTI20_5:
    :cvar INDUSTRIAL_ACTION: TPEG Pti20_5 industrial action.
    :cvar PTI20_5_ALIAS_1:
    :cvar UNOFFICIAL_INDUSTRIAL_ACTION: Unofffical action - alias to
        TPEG Pti20_5 industrial action.
    :cvar PTI20_6:
    :cvar WORK_TO_RULE: TPEG Pti20_6 work to rule.
    :cvar PTI20_255:
    :cvar UNDEFINED_PERSONNEL_PROBLEM: TPEG Pti20_255 undefined
        personnel problem.
    """
    PTI20_0 = "pti20_0"
    UNKNOWN = "unknown"
    PTI20_1 = "pti20_1"
    STAFF_SICKNESS = "staffSickness"
    PTI20_1_ALIAS_1 = "pti20_1_Alias_1"
    STAFF_INJURY = "staffInjury"
    PTI20_1_ALIAS_2 = "pti20_1_Alias_2"
    CONTRACTOR_STAFF_INJURY = "contractorStaffInjury"
    PTI20_2 = "pti20_2"
    STAFF_ABSENCE = "staffAbsence"
    PTI20_3 = "pti20_3"
    STAFF_IN_WRONG_PLACE = "staffInWrongPlace"
    PTI20_4 = "pti20_4"
    STAFF_SHORTAGE = "staffShortage"
    PTI20_5 = "pti20_5"
    INDUSTRIAL_ACTION = "industrialAction"
    PTI20_5_ALIAS_1 = "pti20_5_Alias_1"
    UNOFFICIAL_INDUSTRIAL_ACTION = "unofficialIndustrialAction"
    PTI20_6 = "pti20_6"
    WORK_TO_RULE = "workToRule"
    PTI20_255 = "pti20_255"
    UNDEFINED_PERSONNEL_PROBLEM = "undefinedPersonnelProblem"
