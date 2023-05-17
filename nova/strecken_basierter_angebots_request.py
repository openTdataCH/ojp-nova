from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlTime
from nova.angebots_request import AngebotsRequest
from nova.fahrplan_verbindung import FahrplanVerbindung
from nova.weg_suche import WegSuche
from nova.zonen_buendel_request import ZonenBuendelRequest

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class StreckenBasierterAngebotsRequest(AngebotsRequest):
    """Die Klasse repräsentiert streckenbasierte Angebotsanfragen.

    Streckenbasierte Angebotsanfragen beschreiben den Reisewunsch eines
    Kunden.
    """
    weg_suche: Optional[WegSuche] = field(
        default=None,
        metadata={
            "name": "wegSuche",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    hin_fahrt_verbindung: Optional[FahrplanVerbindung] = field(
        default=None,
        metadata={
            "name": "hinFahrtVerbindung",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    rueck_fahrt: Optional["StreckenBasierterAngebotsRequest.RueckFahrt"] = field(
        default=None,
        metadata={
            "name": "rueckFahrt",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    zonen_buendel_request: List[ZonenBuendelRequest] = field(
        default_factory=list,
        metadata={
            "name": "zonenBuendelRequest",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )

    @dataclass
    class RueckFahrt:
        """
        :ivar verbindung:
        :ivar zeit_angabe:
        :ivar retour_angebote_zusaetzlich_anbieten: Diese Option
            erstellt keine zusätzlichen Angebote und berücksichtigt
            keine Rückwege, sondern dient zur intelligenteren Filterung
            von Angeboten, die nur auf der Basis von einem
            HinfahrtVerbindung erstellt werden. Retour-Angebote, deren
            NutzungsGeltungsdauer nicht 2x Zeit der Verbindung +
            Pufferzeit für einen potentiellen Aufenthaltsdauer abdeckt,
            werden herausgefiltert.
        """
        verbindung: Optional[FahrplanVerbindung] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )
        zeit_angabe: Optional["StreckenBasierterAngebotsRequest.RueckFahrt.ZeitAngabe"] = field(
            default=None,
            metadata={
                "name": "zeitAngabe",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )
        retour_angebote_zusaetzlich_anbieten: Optional["StreckenBasierterAngebotsRequest.RueckFahrt.RetourAngeboteZusaetzlichAnbieten"] = field(
            default=None,
            metadata={
                "name": "retourAngeboteZusaetzlichAnbieten",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )

        @dataclass
        class ZeitAngabe:
            """
            :ivar datum_rueck_fahrt: Datum der Rückfahrt für
                FahrplanVerbindungsanfragen ohne Angabe einer
                Rückfahrtverbindung und für Weganfragen.
            :ivar zeitpunkt_rueck_fahrt: Zeitpunkt der Rückfahrt für
                FahrplanVerbindungsanfragen ohne Angabe einer
                Rückfahrtverbindung und für Weganfragen.
            """
            datum_rueck_fahrt: Optional[XmlDate] = field(
                default=None,
                metadata={
                    "name": "datumRueckFahrt",
                    "type": "Attribute",
                    "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                }
            )
            zeitpunkt_rueck_fahrt: Optional[XmlTime] = field(
                default=None,
                metadata={
                    "name": "zeitpunktRueckFahrt",
                    "type": "Attribute",
                    "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                }
            )

        @dataclass
        class RetourAngeboteZusaetzlichAnbieten:
            """
            :ivar value:
            :ivar pufferzeit_aufenthaltsdauer_minuten: Nova-Benutzer
                können den Wert der Pufferzeit (in Minuten) einstellen,
                um die Filterung von Retourenangeboten anzupassen (falls
                leer, wird der Defaultwert (180 Minuten) angewendet.).
            """
            value: Optional[bool] = field(
                default=None,
                metadata={
                    "required": True,
                }
            )
            pufferzeit_aufenthaltsdauer_minuten: Optional[int] = field(
                default=None,
                metadata={
                    "name": "pufferzeitAufenthaltsdauerMinuten",
                    "type": "Attribute",
                    "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                    "max_inclusive": 9999,
                }
            )
