from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class SituationSourceTypeEnumeration(Enum):
    """
    Values for Type of Source.
    """
    DIRECT_REPORT = "directReport"
    EMAIL = "email"
    PHONE = "phone"
    FAX = "fax"
    POST = "post"
    FEED = "feed"
    RADIO = "radio"
    TV = "tv"
    WEB = "web"
    PAGER = "pager"
    TEXT = "text"
    OTHER = "other"
