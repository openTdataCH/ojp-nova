
from nova.vertriebs_service_port_type_soapv14_leistung_sperren_input import VertriebsServicePortTypeSoapv14LeistungSperrenInput
from nova.vertriebs_service_port_type_soapv14_leistung_sperren_output import VertriebsServicePortTypeSoapv14LeistungSperrenOutput

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


class VertriebsServicePortTypeSoapv14LeistungSperren:
    style = "document"
    location = "http://nova.voev.ch/novaan/vertrieb/public/v14/VertriebsService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://nova.voev.ch/services/v14/vertrieb/leistungSperren"
    input = VertriebsServicePortTypeSoapv14LeistungSperrenInput
    output = VertriebsServicePortTypeSoapv14LeistungSperrenOutput
