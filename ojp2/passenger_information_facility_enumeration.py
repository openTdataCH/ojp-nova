from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class PassengerInformationFacilityEnumeration(Enum):
    """
    Values for Passenger Information Facility.
    """

    UNKNOWN = "unknown"
    NEXT_STOP_INDICATOR = "nextStopIndicator"
    STOP_ANNOUNCEMENTS = "stopAnnouncements"
    PASSENGER_INFORMATION_DISPLAY = "passengerInformationDisplay"
    AUDIO_INFORMATION = "audioInformation"
    VISUAL_INFORMATION = "visualInformation"
    TACTILE_PLATFORM_EDGES = "tactilePlatformEdges"
    TACTILE_INFORMATION = "tactileInformation"
    WALKING_GUIDANCE = "walkingGuidance"
    JOURNEY_PLANNING = "journeyPlanning"
    LOST_FOUND = "lostFound"
    INFORMATION_DESK = "informationDesk"
    INTERACTIVE_KIOSK_DISPLAY = "interactiveKiosk-Display"
    PRINTED_PUBLIC_NOTICE = "printedPublicNotice"
