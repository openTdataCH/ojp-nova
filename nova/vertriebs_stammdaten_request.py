from dataclasses import dataclass, field
from typing import Optional
from nova.correlation_kontext import CorrelationKontext
from nova.time_shift import TimeShift

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class VertriebsStammdatenRequest:
    """Basistyp für alle Anfragen im VertriebsstammdatenService.

    Die Angaben leistungsVermittler, kanal und (optional) timeShift
    werden ausschliesslich zur Ermittlung des zu verwendenden
    DatenReleases bei der Bearbeitung der Anfrage benötigt.

    :ivar correlation_kontext:
    :ivar time_shift:
    :ivar leistungs_vermittler: Der Partner-Code des anfragenden
        Leistungsvermittlers.
    :ivar kanal_code: Der Kanal-Code des anfragenden
        Leistungsvermittlers
    """
    correlation_kontext: Optional[CorrelationKontext] = field(
        default=None,
        metadata={
            "name": "correlationKontext",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
        }
    )
    time_shift: Optional[TimeShift] = field(
        default=None,
        metadata={
            "name": "timeShift",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    leistungs_vermittler: Optional[int] = field(
        default=None,
        metadata={
            "name": "leistungsVermittler",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
            "max_inclusive": 99999,
        }
    )
    kanal_code: Optional[int] = field(
        default=None,
        metadata={
            "name": "kanalCode",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
            "max_inclusive": 9999,
        }
    )
