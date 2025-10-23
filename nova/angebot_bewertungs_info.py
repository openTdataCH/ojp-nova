from dataclasses import dataclass, field
from typing import List, Optional
from nova.komfort import Komfort
from nova.raeumliche_flexibilitaet import RaeumlicheFlexibilitaet
from nova.strecken_sperre import StreckenSperre
from nova.zeitliche_flexibilitaet import ZeitlicheFlexibilitaet

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class AngebotBewertungsInfo:
    """Liefert (nicht normative) Informationen, die Vermittlern eine Bewertung
    eines Angebots ermöglichen.

    Alle Felder einer AngebotBewertungsInfo sind optional. Ein Feld ist
    IMMER gesetzt, wenn die entsprechende Bewertungsdimension für das
    vorliegende Produkt relevant ist (z.B. alle Felder bei 125er und den
    meisten anderen Billett-Produkten). Ist die Dimension nicht relevant
    (z.B. raeumlicheFlexibilitaet beim Produkt Elvia-Reiseversicherung),
    so wird das Feld nicht gesetzt.
    """
    zeitliche_flexibilitaet: Optional[ZeitlicheFlexibilitaet] = field(
        default=None,
        metadata={
            "name": "zeitlicheFlexibilitaet",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    strecken_sperre: List[StreckenSperre] = field(
        default_factory=list,
        metadata={
            "name": "streckenSperre",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    raeumliche_flexibilitaet: Optional[RaeumlicheFlexibilitaet] = field(
        default=None,
        metadata={
            "name": "raeumlicheFlexibilitaet",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    komfort: Optional[Komfort] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    reisenden_beziehung: Optional[str] = field(
        default=None,
        metadata={
            "name": "reisendenBeziehung",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 50,
        }
    )
    teil_angebot: Optional[bool] = field(
        default=None,
        metadata={
            "name": "teilAngebot",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
