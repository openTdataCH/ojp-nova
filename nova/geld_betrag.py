from dataclasses import dataclass, field
from typing import Optional
from nova.currency import Currency

__NAMESPACE__ = "http://nova.voev.ch/services/v14/base"


@dataclass
class GeldBetrag:
    """
    Der GeldBetrag wird definiert durch einen Betrag und eine Währung.

    :ivar betrag: beziffert den GeldBetrag
    :ivar waehrung:
    """
    betrag: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "required": True,
            "total_digits": 12,
            "fraction_digits": 2,
            "pattern": r"-?[0-9]{1,10}(\.[0-9]{0,2})?",
        }
    )
    waehrung: Optional[Currency] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "required": True,
        }
    )
