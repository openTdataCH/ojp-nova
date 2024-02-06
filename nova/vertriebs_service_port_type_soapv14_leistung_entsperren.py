
from nova.vertriebs_service_port_type_soapv14_leistung_entsperren_input import VertriebsServicePortTypeSoapv14LeistungEntsperrenInput
from nova.vertriebs_service_port_type_soapv14_leistung_entsperren_output import VertriebsServicePortTypeSoapv14LeistungEntsperrenOutput

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


class VertriebsServicePortTypeSoapv14LeistungEntsperren:
    style = "document"
    location = "http://nova.voev.ch/novaan/vertrieb/public/v14/VertriebsService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://nova.voev.ch/services/v14/vertrieb/leistungEntsperren"
    input = VertriebsServicePortTypeSoapv14LeistungEntsperrenInput
    output = VertriebsServicePortTypeSoapv14LeistungEntsperrenOutput
