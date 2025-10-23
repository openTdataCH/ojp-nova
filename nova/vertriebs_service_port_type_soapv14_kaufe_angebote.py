
from nova.vertriebs_service_port_type_soapv14_kaufe_angebote_input import VertriebsServicePortTypeSoapv14KaufeAngeboteInput
from nova.vertriebs_service_port_type_soapv14_kaufe_angebote_output import VertriebsServicePortTypeSoapv14KaufeAngeboteOutput

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


class VertriebsServicePortTypeSoapv14KaufeAngebote:
    style = "document"
    location = "http://nova.voev.ch/novaan/vertrieb/public/v14/VertriebsService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://nova.voev.ch/services/v14/vertrieb/kaufeAngebote"
    input = VertriebsServicePortTypeSoapv14KaufeAngeboteInput
    output = VertriebsServicePortTypeSoapv14KaufeAngeboteOutput
