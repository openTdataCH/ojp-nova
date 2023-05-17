from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from nova.localized_string import LocalizedString
from nova.meldungs_typ import MeldungsTyp

__NAMESPACE__ = "http://nova.voev.ch/services/v14/base"


@dataclass
class Meldung:
    """
    Eine fachliche oder technische Meldung des Systems, die für Clients von
    Bedeutung sein kann.

    :ivar beschreibung:
    :ivar id: Technische ID zur Referenzierung innerhalb des XML-
        Dokuments. Wird nur gesetzt für Meldungen, die auch von anderer
        Stelle referenziert werden (Klang 1-4 Antworten).
    :ivar meldungs_code: Code, der eine Meldung eindeutig identifiziert.
    :ivar zeit_stempel:
    :ivar typ: TECHNISCHER_FEHLER bei technischen Fehlern (z.B.
        Nichtverfügbarkeit von Partnersystemen, alle anderen Typen
        kennzeichnen fachliche Meldungen.
    :ivar end_kunden_relevant: true, falls der Meldungstext für einen
        Endkunden relevant ist. Default=false.
    """
    beschreibung: Optional[LocalizedString] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "required": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
        }
    )
    meldungs_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "meldungsCode",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "required": True,
            "min_length": 0,
            "max_length": 50,
        }
    )
    zeit_stempel: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "zeitStempel",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "required": True,
        }
    )
    typ: Optional[MeldungsTyp] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "required": True,
        }
    )
    end_kunden_relevant: Optional[bool] = field(
        default=None,
        metadata={
            "name": "endKundenRelevant",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
        }
    )
