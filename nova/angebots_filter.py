from dataclasses import dataclass

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertriebsbase"


@dataclass
class AngebotsFilter:
    """Mittels Angebotsfilter werden die möglichen Angebote auf eine bestimmte
    Menge eingeschränkt und gefiltert.

    Die Klasse Angebotsfilter selbst ist abstrakt und wird in der Form
    von angegebenen ProduktNummern und/oder ProdukteListeFiltern
    konkretisiert.
    """
