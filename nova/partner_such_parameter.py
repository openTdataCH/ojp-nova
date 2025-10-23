from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDate
from nova.paging_parameter import PagingParameter
from nova.partner_type import PartnerType
from nova.zeitraum import Zeitraum

__NAMESPACE__ = "http://nova.voev.ch/services/v14/geschaeftspartner"


@dataclass
class PartnerSuchParameter:
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "min_length": 0,
            "max_length": 64,
        }
    )
    vorname: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "min_length": 0,
            "max_length": 64,
        }
    )
    organisation1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "min_length": 0,
            "max_length": 64,
        }
    )
    organisation2: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "min_length": 0,
            "max_length": 64,
        }
    )
    ckm: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "min_length": 0,
            "max_length": 13,
        }
    )
    tkid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "length": 36,
            "pattern": r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
        }
    )
    telefon_nummer: Optional[str] = field(
        default=None,
        metadata={
            "name": "telefonNummer",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "min_length": 0,
            "max_length": 200,
        }
    )
    mail: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "min_length": 0,
            "max_length": 200,
        }
    )
    land: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "min_length": 0,
            "max_length": 200,
        }
    )
    ort: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "min_length": 0,
            "max_length": 200,
        }
    )
    plz: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "min_length": 0,
            "max_length": 50,
        }
    )
    strasse_hnr: Optional[str] = field(
        default=None,
        metadata={
            "name": "strasseHnr",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "min_length": 0,
            "max_length": 200,
        }
    )
    geburts_datum: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "geburtsDatum",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
        }
    )
    grundkarten_nummer: Optional[str] = field(
        default=None,
        metadata={
            "name": "grundkartenNummer",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "min_length": 0,
            "max_length": 6,
        }
    )
    geburts_datum_zeitraum: Optional[Zeitraum] = field(
        default=None,
        metadata={
            "name": "geburtsDatumZeitraum",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
        }
    )
    abo_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "aboCode",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "min_length": 0,
            "max_length": 10,
        }
    )
    paging_parameter: Optional[PagingParameter] = field(
        default=None,
        metadata={
            "name": "pagingParameter",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
        }
    )
    partner_typ: Optional[PartnerType] = field(
        default=None,
        metadata={
            "name": "partnerTyp",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
        }
    )
    rolle: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "min_length": 0,
            "max_length": 64,
        }
    )
