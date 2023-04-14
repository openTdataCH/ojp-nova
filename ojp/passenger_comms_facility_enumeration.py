from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class PassengerCommsFacilityEnumeration(Enum):
    """
    Values for PassengerComms Facility: TPEG pti_table 23.
    """
    UNKNOWN = "unknown"
    FACCOMMS_1 = "faccomms_1"
    PASSENGER_WIFI = "passengerWifi"
    PTI23_21 = "pti23_21"
    TELEPHONE = "telephone"
    PTI23_14 = "pti23_14"
    AUDIO_SERVICES = "audioServices"
    PTI23_15 = "pti23_15"
    VIDEO_SERVICES = "videoServices"
    PTI23_25 = "pti23_25"
    BUSINESS_SERVICES = "businessServices"
    INTERNET = "internet"
    POSTOFFICE = "postoffice"
    LETTERBOX = "letterbox"
