from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "http://nova.voev.ch/services/v14/base"


@dataclass
class MwstAnteil:
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
    mwst_satz: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "mwstSatz",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "required": True,
            "total_digits": 4,
            "fraction_digits": 2,
        }
    )
