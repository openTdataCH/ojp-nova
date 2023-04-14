from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlTime
from nova.strecke import Strecke
from nova.verkehrs_mittel_typ_code import VerkehrsMittelTypCode

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class WegSuche(Strecke):
    """Die Klasse dient zur Formulierung von streckenbasierten Angebotsanfragen
    auf Basis eines Wegs.

    In diesem Fall führt die öV-Plattform selbst eine Wegsuche basierend
    auf dem übergebenen Weg durch.

    :ivar weg_suche_segment:
    :ivar folge_haltestelle: Mobile Verkaufsstellen können die noch
        abzufahrenden Haltestellen mitgeben.
    :ivar datum_hin_fahrt:
    :ivar zeitpunkt_hin_fahrt:
    :ivar nur_hin_fahrt_anbieten:
    :ivar zeit_spanne_weg_suche_minuten: Beschränkt die für eine
        Wegsuche verwendeten Fahrplanverbindungen auf den Zeitraum
        [zeitpunktHinFahrt, zeitpunktHinFahrt +
        zeitspanneWegsucheMinuten]. Darf nur gemeinsam mit
        zeitpunktHinFahrt angegeben werden und muss grösser 0 sein.
    """
    weg_suche_segment: List["WegSuche.WegSucheSegment"] = field(
        default_factory=list,
        metadata={
            "name": "wegSucheSegment",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_occurs": 1,
        }
    )
    folge_haltestelle: List[int] = field(
        default_factory=list,
        metadata={
            "name": "folgeHaltestelle",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_inclusive": 0,
        }
    )
    datum_hin_fahrt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "datumHinFahrt",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    zeitpunkt_hin_fahrt: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "zeitpunktHinFahrt",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    nur_hin_fahrt_anbieten: bool = field(
        default=False,
        metadata={
            "name": "nurHinFahrtAnbieten",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    zeit_spanne_weg_suche_minuten: Optional[int] = field(
        default=None,
        metadata={
            "name": "zeitSpanneWegSucheMinuten",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "max_inclusive": 9999,
        }
    )

    @dataclass
    class WegSucheSegment:
        verkehrs_mittel_typ: List[VerkehrsMittelTypCode] = field(
            default_factory=list,
            metadata={
                "name": "verkehrsMittelTyp",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )
        abgang: Optional[int] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "required": True,
                "min_inclusive": 0,
            }
        )
        bestimmung: Optional[int] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "required": True,
                "min_inclusive": 0,
            }
        )
