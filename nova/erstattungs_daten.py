from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate
from nova.erstattungs_grund_typ_1 import ErstattungsGrundTyp1
from nova.erstattungs_typ import ErstattungsTyp
from nova.geld_betrag import GeldBetrag
from nova.preis import Preis

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class ErstattungsDaten:
    """
    Enthält Erstattungsangaben für eine OriginalLeistung.

    :ivar erstattungs_betrag:
    :ivar preis_benutzter_teil: @Deprecated replaced with benutzterTeil
        element. Will be removed in NOVA 15.
    :ivar benutzter_teil:
    :ivar erstattungs_grund:
    :ivar letzter_nutzungs_geltungs_tag:
    :ivar erstattungs_typ:
    :ivar entschaedigung_datum:
    """
    erstattungs_betrag: Optional[Preis] = field(
        default=None,
        metadata={
            "name": "erstattungsBetrag",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    preis_benutzter_teil: Optional[GeldBetrag] = field(
        default=None,
        metadata={
            "name": "preisBenutzterTeil",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    benutzter_teil: Optional[Preis] = field(
        default=None,
        metadata={
            "name": "benutzterTeil",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    erstattungs_grund: Optional[ErstattungsGrundTyp1] = field(
        default=None,
        metadata={
            "name": "erstattungsGrund",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    letzter_nutzungs_geltungs_tag: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "letzterNutzungsGeltungsTag",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    erstattungs_typ: Optional[ErstattungsTyp] = field(
        default=None,
        metadata={
            "name": "erstattungsTyp",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    entschaedigung_datum: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "entschaedigungDatum",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
