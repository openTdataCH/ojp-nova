from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class AuthorityOperationTypeEnum(Enum):
    ACCIDENT_INVESTIGATION_WORK = "accidentInvestigationWork"
    BOMB_SQUAD_IN_ACTION = "bombSquadInAction"
    CIVIL_EMERGENCY = "civilEmergency"
    CUSTOMS_OPERATION = "customsOperation"
    JURIDICAL_RECONSTRUCTION = "juridicalReconstruction"
    POLICE_CHECK_POINT = "policeCheckPoint"
    POLICE_INVESTIGATION = "policeInvestigation"
    ROAD_OPERATOR_CHECK_POINT = "roadOperatorCheckPoint"
    SURVEY = "survey"
    TRANSPORT_OF_VIP = "transportOfVip"
    UNDEFINED_AUTHORITY_ACTIVITY = "undefinedAuthorityActivity"
    VEHICLE_INSPECTION_CHECK_POINT = "vehicleInspectionCheckPoint"
    VEHICLE_WEIGHING = "vehicleWeighing"
    WEIGH_IN_MOTION = "weighInMotion"
    OTHER = "other"
