from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDate
from nova.b2_brabatt_stufe_code_liste import B2BrabattStufeCodeListe
from nova.ermaessigungs_karten import ErmaessigungsKarten
from nova.erstattungs_grund_typen import ErstattungsGrundTypen
from nova.fahr_art_typen import FahrArtTypen
from nova.geschlechter import Geschlechter
from nova.klassen_typen import KlassenTypen
from nova.reisenden_beziehungen import ReisendenBeziehungen
from nova.reisenden_typen import ReisendenTypen
from nova.traeger_medium_typen import TraegerMediumTypen
from nova.verkehrs_mittel_typen import VerkehrsMittelTypen
from nova.vertrags_kuendigungs_gruende import VertragsKuendigungsGruende
from nova.zahlungs_arten import ZahlungsArten
from nova.zahlungs_attribute import ZahlungsAttribute

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class StammdatenPaket:
    """
    :ivar fahr_art_typen:
    :ivar klassen_typen:
    :ivar produkt_info_refs: { Produktinfo.id }
    :ivar traeger_medium_typen:
    :ivar verkehrs_mittel_typen:
    :ivar zahlungs_arten:
    :ivar zahlungs_attribute:
    :ivar zonen_ref: { Zonen.id }
    :ivar erstattungs_gruende:
    :ivar geschlecht:
    :ivar reisenden_typen:
    :ivar haltestellen_ref: { Haltestellen.id }
    :ivar zonen_plaene_ref: { Zonenplaene.id }
    :ivar reisenden_beziehungen:
    :ivar ermaessigungs_karten:
    :ivar zonen_tarife_ref: { Zonentarife.id }
    :ivar kunden_segmente_refs: Enthält die möglichen KundenSegmente,
        für die in der Angebotsantwort (Klang 1) nur der Code geliefert
        wird.
    :ivar b2b_rabatt_stufe_codes: Enthält die möglichen
        B2B-RabattstufeCodes für Angebotsanfragen im Geschäftsfeld B2B
    :ivar vertrags_kuendigungs_gruende:
    :ivar gueltig_ab:
    :ivar gueltig_bis:
    """
    fahr_art_typen: Optional[FahrArtTypen] = field(
        default=None,
        metadata={
            "name": "fahrArtTypen",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
        }
    )
    klassen_typen: Optional[KlassenTypen] = field(
        default=None,
        metadata={
            "name": "klassenTypen",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
        }
    )
    produkt_info_refs: List[str] = field(
        default_factory=list,
        metadata={
            "name": "produktInfoRefs",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "tokens": True,
        }
    )
    traeger_medium_typen: Optional[TraegerMediumTypen] = field(
        default=None,
        metadata={
            "name": "traegerMediumTypen",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
        }
    )
    verkehrs_mittel_typen: Optional[VerkehrsMittelTypen] = field(
        default=None,
        metadata={
            "name": "verkehrsMittelTypen",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
        }
    )
    zahlungs_arten: Optional[ZahlungsArten] = field(
        default=None,
        metadata={
            "name": "zahlungsArten",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
        }
    )
    zahlungs_attribute: Optional[ZahlungsAttribute] = field(
        default=None,
        metadata={
            "name": "zahlungsAttribute",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
        }
    )
    zonen_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "zonenRef",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    erstattungs_gruende: Optional[ErstattungsGrundTypen] = field(
        default=None,
        metadata={
            "name": "erstattungsGruende",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
        }
    )
    geschlecht: Optional[Geschlechter] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
        }
    )
    reisenden_typen: Optional[ReisendenTypen] = field(
        default=None,
        metadata={
            "name": "reisendenTypen",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
        }
    )
    haltestellen_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "haltestellenRef",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    zonen_plaene_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "zonenPlaeneRef",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    reisenden_beziehungen: Optional[ReisendenBeziehungen] = field(
        default=None,
        metadata={
            "name": "reisendenBeziehungen",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
        }
    )
    ermaessigungs_karten: Optional[ErmaessigungsKarten] = field(
        default=None,
        metadata={
            "name": "ermaessigungsKarten",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
        }
    )
    zonen_tarife_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "zonenTarifeRef",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    kunden_segmente_refs: List[str] = field(
        default_factory=list,
        metadata={
            "name": "kundenSegmenteRefs",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
            "tokens": True,
        }
    )
    b2b_rabatt_stufe_codes: Optional[B2BrabattStufeCodeListe] = field(
        default=None,
        metadata={
            "name": "b2bRabattStufeCodes",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    vertrags_kuendigungs_gruende: Optional[VertragsKuendigungsGruende] = field(
        default=None,
        metadata={
            "name": "vertragsKuendigungsGruende",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
        }
    )
    gueltig_ab: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "gueltigAb",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
        }
    )
    gueltig_bis: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "gueltigBis",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
        }
    )
