from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class AudienceEnumeration(Enum):
    """
    Values for Audience.
    """
    PUBLIC = "public"
    EMERGENCY_SERVICES = "emergencyServices"
    STAFF = "staff"
    STATION_STAFF = "stationStaff"
    MANAGEMENT = "management"
    INFO_SERVICES = "infoServices"
