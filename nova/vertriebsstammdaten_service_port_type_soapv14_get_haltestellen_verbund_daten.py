
from nova.vertriebsstammdaten_service_port_type_soapv14_get_haltestellen_verbund_daten_input import VertriebsstammdatenServicePortTypeSoapv14GetHaltestellenVerbundDatenInput
from nova.vertriebsstammdaten_service_port_type_soapv14_get_haltestellen_verbund_daten_output import VertriebsstammdatenServicePortTypeSoapv14GetHaltestellenVerbundDatenOutput

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


class VertriebsstammdatenServicePortTypeSoapv14GetHaltestellenVerbundDaten:
    style = "document"
    location = "http://nova.voev.ch/novaan/vertrieb/public/v14/VertriebsstammdatenService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten/getHaltestellenVerbundDaten"
    input = VertriebsstammdatenServicePortTypeSoapv14GetHaltestellenVerbundDatenInput
    output = VertriebsstammdatenServicePortTypeSoapv14GetHaltestellenVerbundDatenOutput
