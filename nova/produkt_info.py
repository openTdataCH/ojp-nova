from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDate
from nova.erneuerungs_art import ErneuerungsArt
from nova.generischer_einfluss_faktor import GenerischerEinflussFaktor
from nova.gueltigkeits_einschraenkung import GueltigkeitsEinschraenkung
from nova.haltestellen_einschraenkung import HaltestellenEinschraenkung
from nova.localized_string import LocalizedString
from nova.moegliche_parkplatz import MoeglicheParkplatz
from nova.parameter_kombination import ParameterKombination
from nova.parkplatz import Parkplatz
from nova.produkt_erstattungs_bedingung import ProduktErstattungsBedingung
from nova.rollen_name_list_type import RollenNameListType
from nova.standort_type import StandortType
from nova.verkaufs_ablauf import VerkaufsAblauf
from nova.vorverkaufs_frist_traeger_medium import VorverkaufsFristTraegerMedium
from nova.weg_einschraenkung import WegEinschraenkung
from nova.zonen_einschraenkung import ZonenEinschraenkung

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class ProduktInfo:
    """
    Die Klasse ProduktInfo identifiziert ein Produkt und enthält allgemeine
    Informatioinen(Info-Texte, Konditionen) zu diesem.

    :ivar verkaufs_ablauf:
    :ivar produkt_bezeichnung:
    :ivar moegliche_erstattungs_bedingung:
    :ivar zonen_tarif_ref:
    :ivar gueltigkeits_einschraenkung:
    :ivar moegliche_parameter_kombination:
    :ivar vorverkaufs_frist_traeger_medium: Gibt die Vorverkaufsfrist je
        Traegermedium an
    :ivar moeglicher_standort: @Deprecated will be removed in NOVA 15.
        Gibt die Standorte (als DidokCode und bezeichnung) an, an denen
        dieses Produkt verkauft werden kann.
    :ivar moeglicher_parkplatz: @Deprecated Will be removed in NOVA 15.
        Use "moeglicheParkplaetze" instead.
    :ivar moegliche_parkplaetze: Gibt die Parkplätze (als ParkplatzCode
        und Bezeichnung) an, an denen dieses Produkt verkauft werden
        kann
    :ivar generischer_einfluss_faktor:
    :ivar berechtigendes_basis_produkt:
    :ivar berechtigendes_verknuepfungs_produkt:
    :ivar ausschliessendes_verknuepfungs_produkt:
    :ivar weg_einschraenkung: @Deprecated will be removed in NOVA 15
    :ivar haltestellen_einschraenkung:
    :ivar zonen_einschraenkung:
    :ivar erforderliche_rollen: Element contains the names of all roles
        that are required by a customer to be able to buy this kind of
        product. If the list contains more than one role name then the
        customer has to have at least one of the mentioned roles. This
        element replaces the deprecated attribute "benoetigeRolle" from
        ProduktInfo.
    :ivar id: id wird durch Stammdatenpaket referenziert.
    :ivar produkt_nummer:
    :ivar interne_produkt_bezeichnung:
    :ivar verkaufbar_ab:
    :ivar verkaufbar_bis:
    :ivar gueltig_von:
    :ivar gueltig_bis:
    :ivar tarif_owner_code: Partnercode des dem Produkt zugeordneten
        Tarifowners.
    :ivar ist_undatiertes_produkt:
    :ivar erfordert_kunde:
    :ivar erfordert_vertrag:
    :ivar benoetigte_rolle: @Deprecated Will be removed in NOVA 15. Use
        "erforderlicheRollen" instead. Gibt die zum Kauf dieses Produkts
        erforderliche Rolle an.
    :ivar ist_zuschlags_produkt: Gibt an, ob es sich beim Produkt um ein
        Zuschlagsprodukt (z.B. Nachtzusschlag) handelt.
    :ivar erneuerungs_typ:
    :ivar druck_beleg_fuer_gratis_angebote: Gibt an, ob bei Gratis-
        Angeboten ein Druckbeleg ausgegeben werden muss oder nicht.
    :ivar nutzung_moeglich_von:
    :ivar nutzung_moeglich_bis:
    :ivar max_anzahl_tarif_wege:
    :ivar freie_preis_eingabe:
    :ivar ist_gruppen_produkt:
    :ivar ist_abo_produkt:
    """
    verkaufs_ablauf: List[VerkaufsAblauf] = field(
        default_factory=list,
        metadata={
            "name": "verkaufsAblauf",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    produkt_bezeichnung: Optional[LocalizedString] = field(
        default=None,
        metadata={
            "name": "produktBezeichnung",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    moegliche_erstattungs_bedingung: List[ProduktErstattungsBedingung] = field(
        default_factory=list,
        metadata={
            "name": "moeglicheErstattungsBedingung",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    zonen_tarif_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "zonenTarifRef",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    gueltigkeits_einschraenkung: List[GueltigkeitsEinschraenkung] = field(
        default_factory=list,
        metadata={
            "name": "gueltigkeitsEinschraenkung",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    moegliche_parameter_kombination: List[ParameterKombination] = field(
        default_factory=list,
        metadata={
            "name": "moeglicheParameterKombination",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    vorverkaufs_frist_traeger_medium: List[VorverkaufsFristTraegerMedium] = field(
        default_factory=list,
        metadata={
            "name": "vorverkaufsFristTraegerMedium",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    moeglicher_standort: List[StandortType] = field(
        default_factory=list,
        metadata={
            "name": "moeglicherStandort",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    moeglicher_parkplatz: List[Parkplatz] = field(
        default_factory=list,
        metadata={
            "name": "moeglicherParkplatz",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    moegliche_parkplaetze: List[MoeglicheParkplatz] = field(
        default_factory=list,
        metadata={
            "name": "moeglicheParkplaetze",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    generischer_einfluss_faktor: List[GenerischerEinflussFaktor] = field(
        default_factory=list,
        metadata={
            "name": "generischerEinflussFaktor",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    berechtigendes_basis_produkt: List[int] = field(
        default_factory=list,
        metadata={
            "name": "berechtigendesBasisProdukt",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "min_inclusive": 0,
        }
    )
    berechtigendes_verknuepfungs_produkt: List[int] = field(
        default_factory=list,
        metadata={
            "name": "berechtigendesVerknuepfungsProdukt",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "min_inclusive": 0,
        }
    )
    ausschliessendes_verknuepfungs_produkt: List[int] = field(
        default_factory=list,
        metadata={
            "name": "ausschliessendesVerknuepfungsProdukt",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "min_inclusive": 0,
        }
    )
    weg_einschraenkung: Optional[WegEinschraenkung] = field(
        default=None,
        metadata={
            "name": "wegEinschraenkung",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    haltestellen_einschraenkung: Optional[HaltestellenEinschraenkung] = field(
        default=None,
        metadata={
            "name": "haltestellenEinschraenkung",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    zonen_einschraenkung: List[ZonenEinschraenkung] = field(
        default_factory=list,
        metadata={
            "name": "zonenEinschraenkung",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    erforderliche_rollen: Optional[RollenNameListType] = field(
        default=None,
        metadata={
            "name": "erforderlicheRollen",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
        }
    )
    produkt_nummer: Optional[int] = field(
        default=None,
        metadata={
            "name": "produktNummer",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
            "min_inclusive": 0,
        }
    )
    interne_produkt_bezeichnung: Optional[str] = field(
        default=None,
        metadata={
            "name": "interneProduktBezeichnung",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "min_length": 0,
            "max_length": 255,
        }
    )
    verkaufbar_ab: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "verkaufbarAb",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    verkaufbar_bis: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "verkaufbarBis",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    gueltig_von: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "gueltigVon",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    gueltig_bis: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "gueltigBis",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    tarif_owner_code: Optional[int] = field(
        default=None,
        metadata={
            "name": "tarifOwnerCode",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "max_inclusive": 99999,
        }
    )
    ist_undatiertes_produkt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "istUndatiertesProdukt",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    erfordert_kunde: Optional[bool] = field(
        default=None,
        metadata={
            "name": "erfordertKunde",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    erfordert_vertrag: Optional[bool] = field(
        default=None,
        metadata={
            "name": "erfordertVertrag",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    benoetigte_rolle: Optional[str] = field(
        default=None,
        metadata={
            "name": "benoetigteRolle",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "min_length": 0,
            "max_length": 64,
        }
    )
    ist_zuschlags_produkt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "istZuschlagsProdukt",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    erneuerungs_typ: Optional[ErneuerungsArt] = field(
        default=None,
        metadata={
            "name": "erneuerungsTyp",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    druck_beleg_fuer_gratis_angebote: Optional[bool] = field(
        default=None,
        metadata={
            "name": "druckBelegFuerGratisAngebote",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    nutzung_moeglich_von: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "nutzungMoeglichVon",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    nutzung_moeglich_bis: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "nutzungMoeglichBis",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    max_anzahl_tarif_wege: Optional[int] = field(
        default=None,
        metadata={
            "name": "maxAnzahlTarifWege",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "min_inclusive": 1,
            "max_inclusive": 2,
        }
    )
    freie_preis_eingabe: Optional[bool] = field(
        default=None,
        metadata={
            "name": "freiePreisEingabe",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    ist_gruppen_produkt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "istGruppenProdukt",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    ist_abo_produkt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "istAboProdukt",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
