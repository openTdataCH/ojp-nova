from dataclasses import dataclass, field
from typing import List, Optional
from nova.datums_zeitraum import DatumsZeitraum
from nova.fahr_ausweis_art import FahrAusweisArt
from nova.leistungs_fach_schluessel import LeistungsFachSchluessel
from nova.leistungs_suche_feld import LeistungsSucheFeld
from nova.paging_parameter import PagingParameter
from nova.vertriebs_request import VertriebsRequest
from nova.zeitraum import Zeitraum

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class LeistungsSuchRequest(VertriebsRequest):
    """
    Das Objekt LeistungsSuchanfrage dient als Container für notwendige
    Informationen zur LeistungsSuchanfrage.

    :ivar leistungs_schluessel: Suche über ein oder mehrere Leistungs-
        Fachschlüssel
    :ivar leistungs_feld: @Deprecated Will be removed in NOVA 15. Suche
        in einem oder mehreren Leistungs-Feldern. Werden mehrere Felder
        angegeben, so werden diese UND-verknüpft.
    :ivar leistung:
    :ivar paging_parameter: Durch das Hinzufügen der Paging-Parameter
        trefferOffset und maxTreffer können die Ergebnisse der
        LeistungsSuche paginiert werden.
    :ivar inklusive_kontroll_status: Legt fest, ob der Kontrollstatus
        der Leistung ermittelt werden soll. Dies ist nur für
        elektronisch kontrollierte Leistungen möglich. Nur true setzen,
        falls wirklich benötigt. Default=false
    :ivar inklusive_offeriert_leistungen:
    :ivar inklusive_begleitperson_leistungen:
    """
    leistungs_schluessel: List[LeistungsFachSchluessel] = field(
        default_factory=list,
        metadata={
            "name": "leistungsSchluessel",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    leistungs_feld: List[LeistungsSucheFeld] = field(
        default_factory=list,
        metadata={
            "name": "leistungsFeld",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    leistung: Optional["LeistungsSuchRequest.Leistung"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    paging_parameter: Optional[PagingParameter] = field(
        default=None,
        metadata={
            "name": "pagingParameter",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    inklusive_kontroll_status: Optional[bool] = field(
        default=None,
        metadata={
            "name": "inklusiveKontrollStatus",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    inklusive_offeriert_leistungen: Optional[bool] = field(
        default=None,
        metadata={
            "name": "inklusiveOfferiertLeistungen",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    inklusive_begleitperson_leistungen: Optional[bool] = field(
        default=None,
        metadata={
            "name": "inklusiveBegleitpersonLeistungen",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )

    @dataclass
    class Leistung:
        """
        :ivar tkid:
        :ivar fahr_ausweis_art:
        :ivar traeger_medium_code:
        :ivar nutzungs_zeitraum: @Deprecated Will be removed in NOVA 15,
            please use gueltigkeitsZeitraum instead. / Schränkt die
            zurückgelieferten Leistungen auf diejenigen ein, deren
            Intervall [ersterNutzungsGeltungstag,
            letzterNutzungsGeltungstag] sich mit dem Intervall [von,
            bis] um mindestens 1 Tag überschneidet. Dieser Filter wird
            auf Leistungen, deren NutzungsInfo keinen
            erster/letzterNutzungsGeltungstag angibt, nicht angewendet
            (d.h. die Leistungen werden zurückgeliefert). UND-verknüpft
            mit erstellungszeitraum.
        :ivar gueltigkeits_zeitraum: Restricts the returned Leistungen
            to those whose intervals [ersterNutzungsGeltungstag,
            letzterNutzungsGeltungstag] and/or [entwertungsZeitraumVon,
            entwertungsZeitraumBis] overlap the given interval [von,
            bis]. AND-combined with erstellungszeitraum.
        :ivar erstellungs_zeitraum: Schränkt die zurückgelieferten
            Leistungen auf diejenigen ein, deren Erstellungszeitpunkt
            (Klang 2) sich mit dem Intervall [von, bis] überschneidet.
            UND-verknüpft mit nutzungsZeitraum.
        """
        tkid: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "required": True,
                "length": 36,
                "pattern": r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
            }
        )
        fahr_ausweis_art: Optional[FahrAusweisArt] = field(
            default=None,
            metadata={
                "name": "fahrAusweisArt",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )
        traeger_medium_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "traegerMediumCode",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "min_length": 0,
                "max_length": 50,
            }
        )
        nutzungs_zeitraum: Optional[DatumsZeitraum] = field(
            default=None,
            metadata={
                "name": "nutzungsZeitraum",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )
        gueltigkeits_zeitraum: Optional[Zeitraum] = field(
            default=None,
            metadata={
                "name": "gueltigkeitsZeitraum",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )
        erstellungs_zeitraum: Optional[Zeitraum] = field(
            default=None,
            metadata={
                "name": "erstellungsZeitraum",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )
