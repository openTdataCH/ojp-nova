from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertriebsbase"


@dataclass
class B2BrabattStufeCodeListe:
    """
    Liste von möglichen B2B-RabattstufeCodes.
    """
    class Meta:
        name = "B2BRabattStufeCodeListe"

    b2b_rabatt_stufe_code: List[str] = field(
        default_factory=list,
        metadata={
            "name": "b2bRabattStufeCode",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "min_occurs": 1,
            "min_length": 0,
            "max_length": 32,
        }
    )
