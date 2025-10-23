
from nova.vertriebsstammdaten_service_port_type_soapv14_get_produkt_taxonomien_input import VertriebsstammdatenServicePortTypeSoapv14GetProduktTaxonomienInput
from nova.vertriebsstammdaten_service_port_type_soapv14_get_produkt_taxonomien_output import VertriebsstammdatenServicePortTypeSoapv14GetProduktTaxonomienOutput

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


class VertriebsstammdatenServicePortTypeSoapv14GetProduktTaxonomien:
    style = "document"
    location = "http://nova.voev.ch/novaan/vertrieb/public/v14/VertriebsstammdatenService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten/getProduktTaxonomien"
    input = VertriebsstammdatenServicePortTypeSoapv14GetProduktTaxonomienInput
    output = VertriebsstammdatenServicePortTypeSoapv14GetProduktTaxonomienOutput
