
from nova.vertriebsstammdaten_service_port_type_soapv14_get_info_texte_input import VertriebsstammdatenServicePortTypeSoapv14GetInfoTexteInput
from nova.vertriebsstammdaten_service_port_type_soapv14_get_info_texte_output import VertriebsstammdatenServicePortTypeSoapv14GetInfoTexteOutput

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


class VertriebsstammdatenServicePortTypeSoapv14GetInfoTexte:
    style = "document"
    location = "http://nova.voev.ch/novaan/vertrieb/public/v14/VertriebsstammdatenService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten/getInfoTexte"
    input = VertriebsstammdatenServicePortTypeSoapv14GetInfoTexteInput
    output = VertriebsstammdatenServicePortTypeSoapv14GetInfoTexteOutput
