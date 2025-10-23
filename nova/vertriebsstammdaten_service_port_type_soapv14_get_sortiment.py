
from nova.vertriebsstammdaten_service_port_type_soapv14_get_sortiment_input import VertriebsstammdatenServicePortTypeSoapv14GetSortimentInput
from nova.vertriebsstammdaten_service_port_type_soapv14_get_sortiment_output import VertriebsstammdatenServicePortTypeSoapv14GetSortimentOutput

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


class VertriebsstammdatenServicePortTypeSoapv14GetSortiment:
    style = "document"
    location = "http://nova.voev.ch/novaan/vertrieb/public/v14/VertriebsstammdatenService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten/getSortiment"
    input = VertriebsstammdatenServicePortTypeSoapv14GetSortimentInput
    output = VertriebsstammdatenServicePortTypeSoapv14GetSortimentOutput
