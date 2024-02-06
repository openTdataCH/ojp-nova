from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDate
from nova.dauer import Dauer
from nova.zeit_einheit_code import ZeitEinheitCode

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class ProduktErstattungsBedingung:
    """
    :ivar erstattungs_bedingung_ref: Referenziert Erstattungsbedingung
        in stammdatenErstattungsBedingungen.
    :ivar ersatz_erstattungs_gruende:
    :ivar kuendigungs_bedingungen:
    :ivar gueltig_ab:
    :ivar gueltig_bis:
    :ivar nur_einzeln_erstattbar:
    """
    erstattungs_bedingung_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "erstattungsBedingungRef",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
        }
    )
    ersatz_erstattungs_gruende: Optional["ProduktErstattungsBedingung.ErsatzErstattungsGruende"] = field(
        default=None,
        metadata={
            "name": "ersatzErstattungsGruende",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    kuendigungs_bedingungen: Optional["ProduktErstattungsBedingung.KuendigungsBedingungen"] = field(
        default=None,
        metadata={
            "name": "kuendigungsBedingungen",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    gueltig_ab: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "gueltigAb",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
        }
    )
    gueltig_bis: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "gueltigBis",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
        }
    )
    nur_einzeln_erstattbar: Optional[bool] = field(
        default=None,
        metadata={
            "name": "nurEinzelnErstattbar",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
        }
    )

    @dataclass
    class ErsatzErstattungsGruende:
        moeglicher_erstattungs_grund: List[str] = field(
            default_factory=list,
            metadata={
                "name": "moeglicherErstattungsGrund",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
                "min_length": 0,
                "max_length": 50,
            }
        )

    @dataclass
    class KuendigungsBedingungen:
        kuendigung_auf_ende: Optional[ZeitEinheitCode] = field(
            default=None,
            metadata={
                "name": "kuendigungAufEnde",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            }
        )
        kuendigungs_frist: Optional[Dauer] = field(
            default=None,
            metadata={
                "name": "kuendigungsFrist",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            }
        )
        mindest_vertrags_dauer: Optional[Dauer] = field(
            default=None,
            metadata={
                "name": "mindestVertragsDauer",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            }
        )
