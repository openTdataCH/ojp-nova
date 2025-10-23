
from nova.vertriebs_service_port_type_soapv14_bestaetige_produktion_input import VertriebsServicePortTypeSoapv14BestaetigeProduktionInput
from nova.vertriebs_service_port_type_soapv14_bestaetige_produktion_output import VertriebsServicePortTypeSoapv14BestaetigeProduktionOutput

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


class VertriebsServicePortTypeSoapv14BestaetigeProduktion:
    style = "document"
    location = "http://nova.voev.ch/novaan/vertrieb/public/v14/VertriebsService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://nova.voev.ch/services/v14/vertrieb/bestaetigeProduktion"
    input = VertriebsServicePortTypeSoapv14BestaetigeProduktionInput
    output = VertriebsServicePortTypeSoapv14BestaetigeProduktionOutput
