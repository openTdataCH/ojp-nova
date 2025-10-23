from enum import Enum

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


class TransaktionsVerhalten(Enum):
    COMMIT_ON_ERROR = "COMMIT_ON_ERROR"
    ROLLBACK_ON_ERROR = "ROLLBACK_ON_ERROR"
