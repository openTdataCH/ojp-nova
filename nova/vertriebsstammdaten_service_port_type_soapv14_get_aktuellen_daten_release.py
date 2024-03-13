
from nova.vertriebsstammdaten_service_port_type_soapv14_get_aktuellen_daten_release_input import VertriebsstammdatenServicePortTypeSoapv14GetAktuellenDatenReleaseInput
from nova.vertriebsstammdaten_service_port_type_soapv14_get_aktuellen_daten_release_output import VertriebsstammdatenServicePortTypeSoapv14GetAktuellenDatenReleaseOutput

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


class VertriebsstammdatenServicePortTypeSoapv14GetAktuellenDatenRelease:
    style = "document"
    location = "http://nova.voev.ch/novaan/vertrieb/public/v14/VertriebsstammdatenService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten/getAktuellenDatenRelease"
    input = VertriebsstammdatenServicePortTypeSoapv14GetAktuellenDatenReleaseInput
    output = VertriebsstammdatenServicePortTypeSoapv14GetAktuellenDatenReleaseOutput
