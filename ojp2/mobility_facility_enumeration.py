from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class MobilityFacilityEnumeration(Enum):
    """Values for Mobility Facility: TPEG pti_table 23."""

    PTI23_255_4 = "pti23_255_4"
    UNKNOWN = "unknown"
    PTI23_16 = "pti23_16"
    SUITABLE_FOR_WHEEL_CHAIRS = "suitableForWheelChairs"
    PTI23_16_1 = "pti23_16_1"
    LOW_FLOOR = "lowFloor"
    PTI23_16_2 = "pti23_16_2"
    BOARDING_ASSISTANCE = "boardingAssistance"
    PTI23_16_3 = "pti23_16_3"
    STEP_FREE_ACCESS = "stepFreeAccess"
    TACTILE_PATFORM_EDGES = "tactilePatformEdges"
    ONBOARD_ASSISTANCE = "onboardAssistance"
    UNACCOMPANIED_MINOR_ASSISTANCE = "unaccompaniedMinorAssistance"
    AUDIO_INFORMATION = "audioInformation"
    VISUAL_INFORMATION = "visualInformation"
    DISPLAYS_FOR_VISUALLY_IMPAIRED = "displaysForVisuallyImpaired"
    AUDIO_FOR_HEARING_IMPAIRED = "audioForHearingImpaired"
