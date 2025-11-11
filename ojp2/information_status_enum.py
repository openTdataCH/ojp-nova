from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class InformationStatusEnum(Enum):
    REAL = "real"
    SECURITY_EXERCISE = "securityExercise"
    TECHNICAL_EXERCISE = "technicalExercise"
    TEST = "test"
