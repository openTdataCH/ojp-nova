from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class MonitoringTypeEnumeration(Enum):
    """Allowed values for the types of monitoring: automatic or manual - describing the hardware transducer (video, GPS/Radio, in-road sensors, etc.) doesn't seeme useful for SIRi."""
    UNKNOWN = "unknown"
    MANUAL = "manual"
    AUTOMATIC = "automatic"
