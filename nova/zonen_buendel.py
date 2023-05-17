from dataclasses import dataclass, field
from typing import List, Optional
from nova.befahrungs_typ import BefahrungsTyp
from nova.localized_string import LocalizedString
from nova.weg_position import WegPosition
from nova.zone import Zone

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class ZonenBuendel:
    """Ein Zonenbündel beinhaltet Zonen, die gemeinsam (im Bündel) angeboten werden
    (z.B.

    die Libero Zonen 100+101 [Kern- und Ringzone Bern])

    :ivar zone:
    :ivar additive_zone:
    :ivar bezeichnung: Die Bezeichnung von Zonbenbündeln wird u.a. für
        Modul-Abo Zonen oder City-Zonen gesetzt (z.B. City-Zone Bern).
        Für Verbundtickets üblicherweise nicht gesetzt.
    :ivar weg_position:
    :ivar pflicht_zonen_buendel: Kennzeichnet, ob es sich bei den im
        Zonenbündel enthaltenen Zonen um Pflichtzonen handelt, die
        zwingender Bestandteil des Angebots sind.
    :ivar alle_zonen: Kennzeichnet, ob der Geltungsbereich "ALLE ZONEN"
        des TarifOwners umfasst. Default ist false. Wenn true, werden
        keine (additiven) Zonen geliefert.
    :ivar tarif_owner:
    :ivar befahrungs_typ:
    :ivar nova_zonen_tarif_code:
    """
    zone: List[Zone] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    additive_zone: List[Zone] = field(
        default_factory=list,
        metadata={
            "name": "additiveZone",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    bezeichnung: Optional[LocalizedString] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    weg_position: Optional[WegPosition] = field(
        default=None,
        metadata={
            "name": "wegPosition",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    pflicht_zonen_buendel: Optional[bool] = field(
        default=None,
        metadata={
            "name": "pflichtZonenBuendel",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    alle_zonen: Optional[bool] = field(
        default=None,
        metadata={
            "name": "alleZonen",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    tarif_owner: Optional[int] = field(
        default=None,
        metadata={
            "name": "tarifOwner",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "max_inclusive": 99999,
        }
    )
    befahrungs_typ: Optional[BefahrungsTyp] = field(
        default=None,
        metadata={
            "name": "befahrungsTyp",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    nova_zonen_tarif_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "novaZonenTarifCode",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 255,
        }
    )
