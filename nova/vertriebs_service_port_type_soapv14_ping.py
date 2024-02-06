
from nova.vertriebs_service_port_type_soapv14_ping_input import VertriebsServicePortTypeSoapv14PingInput
from nova.vertriebs_service_port_type_soapv14_ping_output import VertriebsServicePortTypeSoapv14PingOutput

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


class VertriebsServicePortTypeSoapv14Ping:
    style = "document"
    location = "http://nova.voev.ch/novaan/vertrieb/public/v14/VertriebsService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://nova.voev.ch/services/v14/vertrieb/ping"
    input = VertriebsServicePortTypeSoapv14PingInput
    output = VertriebsServicePortTypeSoapv14PingOutput
