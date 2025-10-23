from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate, XmlTime

__NAMESPACE__ = "http://nova.voev.ch/services/v14/base"


@dataclass
class TimeShift:
    """Ein TimeShift kann optional einer VertriebsAnfrage mitgegeben werden, um den
    Anfragezeitpunkt künstlich zu verschieben. Ein TimeShift besteht aus:

    - einer optionalen Anfragezeit, welche festgelegt werden kann
    - einem optionalen AnfrageDatumShift, welches das Anfragedatum entweder fix, oder per Delta festlegen kann
    Eines der beiden optionalen Attribute muss jeweils gesetzt sein, es dürfen nicht beide gleichzeitig leer sein.
    """
    anfrage_datum_shift: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "anfrageDatumShift",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
        }
    )
    anfrage_zeit: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "anfrageZeit",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
        }
    )
