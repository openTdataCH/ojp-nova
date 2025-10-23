
from nova.vertriebs_service_port_type_soapv14_storniere_leistung_input import VertriebsServicePortTypeSoapv14StorniereLeistungInput
from nova.vertriebs_service_port_type_soapv14_storniere_leistung_output import VertriebsServicePortTypeSoapv14StorniereLeistungOutput

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


class VertriebsServicePortTypeSoapv14StorniereLeistung:
    style = "document"
    location = "http://nova.voev.ch/novaan/vertrieb/public/v14/VertriebsService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://nova.voev.ch/services/v14/vertrieb/storniereLeistung"
    input = VertriebsServicePortTypeSoapv14StorniereLeistungInput
    output = VertriebsServicePortTypeSoapv14StorniereLeistungOutput
