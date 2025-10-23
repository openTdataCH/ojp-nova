from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class UrlLinkTypeEnum(Enum):
    DOCUMENT_PDF = "documentPdf"
    HTML = "html"
    IMAGE = "image"
    RSS = "rss"
    VIDEO_STREAM = "videoStream"
    VOICE_STREAM = "voiceStream"
    OTHER = "other"
