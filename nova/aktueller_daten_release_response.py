from dataclasses import dataclass
from nova.vertriebs_stammdaten_response import VertriebsStammdatenResponse

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class AktuellerDatenReleaseResponse(VertriebsStammdatenResponse):
    pass
