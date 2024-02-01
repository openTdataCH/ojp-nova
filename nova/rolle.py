from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "http://nova.voev.ch/services/v14/geschaeftspartner"


@dataclass
class Rolle:
    """Eine Rolle beschreibt die Position, die ein Partner in einer
    Geschäftsbeziehung einnimmt.

    Aufgrund der Rolle wird unter anderem das Konfidenzprofil bestimmt,
    dem ein Partner mit dieser Rolle entsprechen muss.
    """
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "required": True,
            "min_length": 0,
            "max_length": 64,
        }
    )
    gueltig_bis: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "gueltigBis",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
        }
    )
