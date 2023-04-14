from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate, XmlDateTime
from nova.rabatt_anfrage_type import RabattAnfrageType

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class ErneuerungsRequest:
    """
    :ivar bestehende_leistungs_id:
    :ivar externe_leistungs_referenz_id:
    :ivar original_leistung_produkt_nummer:
    :ivar original_leistung_gueltig_bis:
    :ivar vertrags_partner_tkid:
    :ivar reisender_tkid:
    :ivar vertrags_nummer:
    :ivar original_leistung_klasse:
    :ivar original_leistungs_erster_lv:
    :ivar rabatt_request:
    :ivar gueltig_ab:
    :ivar ersatz_leistungs_kauf: Attribut zur Steuerung des
        Ersatzleistungskaufs. Wird für interne Zwecke benötigt.
    """
    bestehende_leistungs_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "bestehendeLeistungsId",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_inclusive": 0,
        }
    )
    externe_leistungs_referenz_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "externeLeistungsReferenzId",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 50,
        }
    )
    original_leistung_produkt_nummer: Optional[int] = field(
        default=None,
        metadata={
            "name": "originalLeistungProduktNummer",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_inclusive": 0,
        }
    )
    original_leistung_gueltig_bis: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "originalLeistungGueltigBis",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    vertrags_partner_tkid: Optional[str] = field(
        default=None,
        metadata={
            "name": "vertragsPartnerTkid",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "length": 36,
            "pattern": r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
        }
    )
    reisender_tkid: Optional[str] = field(
        default=None,
        metadata={
            "name": "reisenderTkid",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "length": 36,
            "pattern": r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
        }
    )
    vertrags_nummer: Optional[str] = field(
        default=None,
        metadata={
            "name": "vertragsNummer",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 10,
        }
    )
    original_leistung_klasse: Optional[int] = field(
        default=None,
        metadata={
            "name": "originalLeistungKlasse",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    original_leistungs_erster_lv: Optional[int] = field(
        default=None,
        metadata={
            "name": "originalLeistungsErsterLV",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "max_inclusive": 99999,
        }
    )
    rabatt_request: Optional[RabattAnfrageType] = field(
        default=None,
        metadata={
            "name": "rabattRequest",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    gueltig_ab: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "gueltigAb",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    ersatz_leistungs_kauf: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ersatzLeistungsKauf",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
