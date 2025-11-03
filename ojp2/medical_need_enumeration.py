from enum import Enum

__NAMESPACE__ = "http://www.ifopt.org.uk/acsb"


class MedicalNeedEnumeration(Enum):
    """
    Enumeration of specific Medical USER NEEDs.
    """

    ALLERGIC = "allergic"
    HEART_CONDITION = "heartCondition"
    OTHER_MEDICAL_NEED = "otherMedicalNeed"
