from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlDateTime
from nova.leistung_verkaufs_parameter_type import LeistungVerkaufsParameterType
from nova.leistungs_status import LeistungsStatus
from nova.leistungs_typ import LeistungsTyp
from nova.preis import Preis
from nova.rabatt_info_type import RabattInfoType
from nova.savaktion import Savaktion
from nova.savprotokoll_eintrag import SavprotokollEintrag
from nova.tarif_stufe import TarifStufe
from nova.verkaeufer_information import VerkaeuferInformation
from nova.zahlungs_information import ZahlungsInformation

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class AbstractLeistung:
    """
    Superklasse für Leistungen und SAVLeistungen.

    :ivar leistungs_typ:
    :ivar verkaufs_parameter:
    :ivar zahlungs_information:
    :ivar verkaufs_preis:
    :ivar tarif_stufe: Gesetzt bei Verbund-Fahrausweisen. i.d.R. 1
        Taristufe. Ausnahme: Bei gewissen Fahrausweisen die in Zonen
        unterschiedlicher Verbunde gültig sind wird pro Verbund eine
        eigene Tarifstufe ausgewiesen.
    :ivar rabatt_info:
    :ivar verkaeufer_information: Angaben zur Stelle, die diese Leistung
        verkauft hat.
    :ivar sav_protokoll: Liste aller SAV-Aktionen (Erstattungen,
        Annullationen), die für diese Leistung durchgeführt wurden.
    :ivar leistungs_id:
    :ivar erneuerungs_id: UUID der Leistung, die in der URL im
        ErneurungsInfoService verwendet wird
    :ivar leistungs_paket_id:
    :ivar externe_leistungs_referenz_id:
    :ivar leistungs_referenz:
    :ivar leistungs_status:
    :ivar offerte_gueltig_bis:
    :ivar externe_reisenden_referenz_id:
    :ivar verkaufs_zeitpunkt:
    :ivar erstellungs_zeitpunkt: Gibt an, wann diese Leistung in NOVAAN
        angelegt wurde (Klang 2).
    :ivar produkt_nummer:
    :ivar generation_stich_datum: Datum/Zeit des angewendeten
        Preisberechnungszeitpunkt und damit der DatenRelease-Zeitscheibe
        (Verkaufs- o. Reisezeitpunkt)
    :ivar daten_release_id:
    """
    leistungs_typ: Optional[LeistungsTyp] = field(
        default=None,
        metadata={
            "name": "leistungsTyp",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    verkaufs_parameter: List[LeistungVerkaufsParameterType] = field(
        default_factory=list,
        metadata={
            "name": "verkaufsParameter",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    zahlungs_information: List[ZahlungsInformation] = field(
        default_factory=list,
        metadata={
            "name": "zahlungsInformation",
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
    verkaeufer_information: Optional[VerkaeuferInformation] = field(
        default=None,
        metadata={
            "name": "verkaeuferInformation",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    sav_protokoll: Optional["AbstractLeistung.SavProtokoll"] = field(
        default=None,
        metadata={
            "name": "savProtokoll",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    leistungs_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "leistungsId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_inclusive": 0,
        }
    )
    erneuerungs_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "erneuerungsId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "length": 36,
            "pattern": r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
        }
    )
    leistungs_paket_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "leistungsPaketId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 1,
            "max_length": 37,
        }
    )
    externe_leistungs_referenz_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "externeLeistungsReferenzId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 50,
        }
    )
    leistungs_referenz: Optional[str] = field(
        default=None,
        metadata={
            "name": "leistungsReferenz",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    leistungs_status: Optional[LeistungsStatus] = field(
        default=None,
        metadata={
            "name": "leistungsStatus",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    offerte_gueltig_bis: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "offerteGueltigBis",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    externe_reisenden_referenz_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "externeReisendenReferenzId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 50,
        }
    )
    verkaufs_zeitpunkt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "verkaufsZeitpunkt",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    erstellungs_zeitpunkt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "erstellungsZeitpunkt",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
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
    generation_stich_datum: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "generationStichDatum",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    daten_release_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "datenReleaseId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_length": 0,
            "max_length": 100,
        }
    )

    @dataclass
    class SavProtokoll:
        """
        :ivar sav_aktion: @Deprecated will be removed with NOVA 15.
            Please use savProtokollEintrag instead.
        :ivar sav_protokoll_eintrag:
        """
        sav_aktion: List[Savaktion] = field(
            default_factory=list,
            metadata={
                "name": "savAktion",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )
        sav_protokoll_eintrag: List[SavprotokollEintrag] = field(
            default_factory=list,
            metadata={
                "name": "savProtokollEintrag",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )
