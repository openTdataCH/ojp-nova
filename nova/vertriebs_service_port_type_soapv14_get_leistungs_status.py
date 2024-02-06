
from nova.vertriebs_service_port_type_soapv14_get_leistungs_status_input import VertriebsServicePortTypeSoapv14GetLeistungsStatusInput
from nova.vertriebs_service_port_type_soapv14_get_leistungs_status_output import VertriebsServicePortTypeSoapv14GetLeistungsStatusOutput

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


class VertriebsServicePortTypeSoapv14GetLeistungsStatus:
    style = "document"
    location = "http://nova.voev.ch/novaan/vertrieb/public/v14/VertriebsService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://nova.voev.ch/services/v14/vertrieb/getLeistungsStatus"
    input = VertriebsServicePortTypeSoapv14GetLeistungsStatusInput
    output = VertriebsServicePortTypeSoapv14GetLeistungsStatusOutput
