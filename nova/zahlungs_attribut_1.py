from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertriebsbase"


@dataclass
class ZahlungsAttribut1:
    """Beliebige Attribute, die ein LV zu einem Zahlvorgang abspeichern kann.

    Wird z.B: von B2B verwendet, um in gewissen Situationen die
    RechnungsStelle und die Kostenzuordnung zu übergeben.
    """
    class Meta:
        name = "ZahlungsAttribut"

    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
            "min_length": 0,
            "max_length": 50,
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
            "min_length": 0,
            "max_length": 200,
        }
    )
