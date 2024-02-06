
from nova.vertriebs_service_port_type_soapv14_kaufe_leistungen_input import VertriebsServicePortTypeSoapv14KaufeLeistungenInput
from nova.vertriebs_service_port_type_soapv14_kaufe_leistungen_output import VertriebsServicePortTypeSoapv14KaufeLeistungenOutput

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


class VertriebsServicePortTypeSoapv14KaufeLeistungen:
    style = "document"
    location = "http://nova.voev.ch/novaan/vertrieb/public/v14/VertriebsService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://nova.voev.ch/services/v14/vertrieb/kaufeLeistungen"
    input = VertriebsServicePortTypeSoapv14KaufeLeistungenInput
    output = VertriebsServicePortTypeSoapv14KaufeLeistungenOutput
