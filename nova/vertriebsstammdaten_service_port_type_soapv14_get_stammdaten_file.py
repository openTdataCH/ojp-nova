
from nova.vertriebsstammdaten_service_port_type_soapv14_get_stammdaten_file_input import VertriebsstammdatenServicePortTypeSoapv14GetStammdatenFileInput
from nova.vertriebsstammdaten_service_port_type_soapv14_get_stammdaten_file_output import VertriebsstammdatenServicePortTypeSoapv14GetStammdatenFileOutput

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


class VertriebsstammdatenServicePortTypeSoapv14GetStammdatenFile:
    style = "document"
    location = "http://nova.voev.ch/novaan/vertrieb/public/v14/VertriebsstammdatenService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten/getStammdatenFile"
    input = VertriebsstammdatenServicePortTypeSoapv14GetStammdatenFileInput
    output = VertriebsstammdatenServicePortTypeSoapv14GetStammdatenFileOutput
