from dataclasses import dataclass, field
from typing import Optional
from nova.ausweisbarer_zeitraum import AusweisbarerZeitraum
from nova.dauer import Dauer
from nova.zeitraum import Zeitraum

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class GueltigkeitsZeitraum:
    """Kombination des tarifierbaren und ausweisbaren Zeitraums.

    AusweisbarerZeitraum darf lediglich zu Ausgabezwecken (Druck / Screenanzeige) verwendet werden. In der Business-Logik (z.B. beim Vergleich von Gültigkeitszeiträumen) muss der tarifierbareZeitraum verwendet werden! Beispiel: DV-Einzelbillett 125 - tarifarischer Nutzungszeitraum = 24.08.2016, 00:00:00 Uhr – 25.08.2016 05:00:00 Uhr (29 Stunden, bis 5 Uhr am Folgetag) - ausgewiesener Nutzungszeitraum = 24.08.2016 – 24.08.2016 (1 Tag, ohne Zeitangabe)
    """
    tarifierbarer_zeitraum: Optional[Zeitraum] = field(
        default=None,
        metadata={
            "name": "tarifierbarerZeitraum",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    ausweisbarer_zeitraum: Optional[AusweisbarerZeitraum] = field(
        default=None,
        metadata={
            "name": "ausweisbarerZeitraum",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    reisezeit_toleranz: Optional[Dauer] = field(
        default=None,
        metadata={
            "name": "reisezeitToleranz",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
