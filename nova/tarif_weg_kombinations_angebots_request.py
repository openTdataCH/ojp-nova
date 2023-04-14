from dataclasses import dataclass, field
from typing import List, Optional
from nova.vertriebs_request import VertriebsRequest

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class TarifWegKombinationsAngebotsRequest(VertriebsRequest):
    """Erzeugt ein streckenbasiertes Abo-Angebot dessen Geltungsbereich zwei
    unterschiedliche TarifWege abdeckt (Angebot mit zwei Strecken-Wegangaben).

    Tarifiert werden alle Wege aus den angefragten Angeboten.

    :ivar angebots_id: @Deprecated will be removed in NOVA 15. Beide
        Angebote müssen Abonnemente sein. Mind. 1 Angebot muss auf einem
        Produkt basieren das die Tarifierung mehrerer TarifWege erlaubt
        (Produktinfo.maxAnzahlTarifWege &gt; 1). Der Nutzungszeitraum
        der angefragten Angebote muss identisch sein. Jedes angefragte
        Angebot darf max. 1 TarifWeg abdecken.
    :ivar kombinierte_angebote:
    """
    angebots_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "angebotsId",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "max_occurs": 2,
            "length": 37,
            "pattern": r"_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
        }
    )
    kombinierte_angebote: List["TarifWegKombinationsAngebotsRequest.KombinierteAngebote"] = field(
        default_factory=list,
        metadata={
            "name": "kombinierteAngebote",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )

    @dataclass
    class KombinierteAngebote:
        angebots_id: List[str] = field(
            default_factory=list,
            metadata={
                "name": "angebotsId",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "min_occurs": 2,
                "max_occurs": 2,
                "length": 37,
                "pattern": r"_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
            }
        )
        angebotskombination: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "min_length": 0,
                "max_length": 50,
            }
        )
