from dataclasses import dataclass, field
from typing import Optional
from nova.preis import Preis
from nova.rabatt_klasse import RabattKlasse

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class RabattInfoType:
    rabatt_preis: Optional[Preis] = field(
        default=None,
        metadata={
            "name": "rabattPreis",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    rabatt_klasse: Optional[RabattKlasse] = field(
        default=None,
        metadata={
            "name": "rabattKlasse",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    in_verkaufs_preis_eingerechnet: Optional[bool] = field(
        default=None,
        metadata={
            "name": "inVerkaufsPreisEingerechnet",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    rabatt_stufe_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "rabattStufeCode",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_length": 0,
            "max_length": 32,
        }
    )
