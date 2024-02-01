from dataclasses import dataclass, field
from typing import List, Optional
from nova.auspraegung_verkaufs_parameter_type import AuspraegungVerkaufsParameterType
from nova.fahr_art_typ_code import FahrArtTypCode
from nova.klassen_typ_code import KlassenTypCode
from nova.nachweis_kategorie import NachweisKategorie

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class ParameterKombination:
    generischer_einfluss_faktor: List["ParameterKombination.GenerischerEinflussFaktor"] = field(
        default_factory=list,
        metadata={
            "name": "generischerEinflussFaktor",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    verkaufs_parameter: List[AuspraegungVerkaufsParameterType] = field(
        default_factory=list,
        metadata={
            "name": "verkaufsParameter",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    klasse: Optional[KlassenTypCode] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    traeger_medium_typ: Optional[str] = field(
        default=None,
        metadata={
            "name": "traegerMediumTyp",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "min_length": 0,
            "max_length": 50,
        }
    )
    fahr_art: Optional[FahrArtTypCode] = field(
        default=None,
        metadata={
            "name": "fahrArt",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    kunden_segment_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "kundenSegmentCode",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "min_length": 0,
            "max_length": 50,
        }
    )
    erforderlicher_nachweis: Optional[NachweisKategorie] = field(
        default=None,
        metadata={
            "name": "erforderlicherNachweis",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )

    @dataclass
    class GenerischerEinflussFaktor:
        id_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "idRef",
                "type": "Attribute",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
                "required": True,
            }
        )
        wert_id_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "wertIdRef",
                "type": "Attribute",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
                "required": True,
            }
        )
