from enum import Enum

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


class AnfrageProtokollLevel(Enum):
    OFF = "OFF"
    SUMMARY = "SUMMARY"
    INFO = "INFO"
    DEBUG = "DEBUG"
