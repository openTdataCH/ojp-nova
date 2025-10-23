from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from nova.pruef_status import PruefStatus

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class KontrollStatus:
    """
    :ivar kontroll_zeitpunkt: Datum und Zeit wann die Kontrolle
        durchgeführt wurde.
    :ivar tco_code: Partner-Code der kontrollierenden
        Transportunternehmung
    :ivar kurs_nummer: Kurs-Nummer des VerkehrsMittels, in welchem die
        Kontrolle stattgefunden hat (z.B. Zugnummer).
    :ivar kontroll_person: Kürzel der kontrollierenden Person.
    :ivar resultat_auto: Resultat von automatischer Kontrolle. Wird
        durch Kontrollgerät vorgeschlagen. Hinweis: kann durch
        Kontrollperson übersteuert werden (s. resultatManuell)
    :ivar resultat_manuell: Resultat von Kontrolle. Wird durch
        Kontrollperson gewählt.
    """
    kontroll_zeitpunkt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "kontrollZeitpunkt",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    tco_code: Optional[int] = field(
        default=None,
        metadata={
            "name": "tcoCode",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "max_inclusive": 99999,
        }
    )
    kurs_nummer: Optional[str] = field(
        default=None,
        metadata={
            "name": "kursNummer",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 200,
        }
    )
    kontroll_person: Optional[str] = field(
        default=None,
        metadata={
            "name": "kontrollPerson",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 200,
        }
    )
    resultat_auto: Optional[PruefStatus] = field(
        default=None,
        metadata={
            "name": "resultatAuto",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    resultat_manuell: Optional[PruefStatus] = field(
        default=None,
        metadata={
            "name": "resultatManuell",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
