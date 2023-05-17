from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://nova.voev.ch/services/v14/base"


@dataclass
class CorrelationKontext:
    correlation_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "correlationId",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "required": True,
            "length": 36,
            "pattern": r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
        }
    )
    geschaefts_prozess_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "geschaeftsProzessId",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "length": 36,
            "pattern": r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
        }
    )
