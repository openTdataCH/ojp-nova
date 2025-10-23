from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlDateTime
from nova.angebot_verkaufs_parameter_type import AngebotVerkaufsParameterType
from nova.preis import Preis
from nova.rabatt_info_type import RabattInfoType
from nova.tarif_stufe import TarifStufe

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class AbstractAngebot:
    """
    Superklasse für Angebote und SAVAngebote.

    :ivar meldungen_refs:
    :ivar verkaufs_parameter:
    :ivar verkaufs_preis:
    :ivar tarif_stufe: Gesetzt bei Verbund-Fahrausweisen. i.d.R. 1
        Taristufe. Ausnahme: Bei gewissen Fahrausweisen die in Zonen
        unterschiedlicher Verbunde gültig sind wird pro Verbund eine
        eigene Tarifstufe ausgewiesen.
    :ivar rabatt_info:
    :ivar info_text_id:
    :ivar angebotskombination:
    :ivar angebots_id: ID, die ein Angebot eindeutig identifiziert. Die
        ID ist im 2. Klang zur Identifikation des Angebots zu verwenden.
        Ausnahme: Bei ErneuerungsInfoAngebotAntwort werden die Angebote
        nicht persisitiert und können daher im 2. Klang nicht verwendet
        werden.
    :ivar generation_stich_datum: Datum/Zeit des angewendeten
        Preisberechnungszeitpunkt und damit der DatenRelease-Zeitscheibe
        (Verkaufs- o. Reisezeitpunkt)
    :ivar produkt_nummer:
    :ivar vorhalte_zeitpunkt_bis: Zeitpunkt bis zu dem das Angebot
        gespeichert wird und von Operationen die auf Angeboten operieren
        (wie z.B. offeriereLeistungen, kaufeAngebote,
        liefereBelegeFuerAngebot etc.) verarbeitet werden kann.
    """
    meldungen_refs: List[str] = field(
        default_factory=list,
        metadata={
            "name": "meldungenRefs",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "tokens": True,
        }
    )
    verkaufs_parameter: List[AngebotVerkaufsParameterType] = field(
        default_factory=list,
        metadata={
            "name": "verkaufsParameter",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    verkaufs_preis: Optional[Preis] = field(
        default=None,
        metadata={
            "name": "verkaufsPreis",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    tarif_stufe: List[TarifStufe] = field(
        default_factory=list,
        metadata={
            "name": "tarifStufe",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    rabatt_info: List[RabattInfoType] = field(
        default_factory=list,
        metadata={
            "name": "rabattInfo",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    info_text_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "infoTextId",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 200,
        }
    )
    angebotskombination: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 50,
        }
    )
    angebots_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "angebotsId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "length": 37,
            "pattern": r"_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
        }
    )
    generation_stich_datum: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "generationStichDatum",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    produkt_nummer: Optional[int] = field(
        default=None,
        metadata={
            "name": "produktNummer",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_inclusive": 0,
        }
    )
    vorhalte_zeitpunkt_bis: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "vorhalteZeitpunktBis",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
