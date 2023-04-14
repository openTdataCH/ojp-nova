from dataclasses import dataclass, field
from typing import Optional
from nova.abstract_rabatt_type import AbstractRabattType

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class B2BrabattType(AbstractRabattType):
    class Meta:
        name = "B2BRabattType"

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
