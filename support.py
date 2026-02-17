from typing import Dict

from ojp import Ojp, Ojpresponse, ServiceDelivery, ServiceDeliveryStructure, OtherError
from xsdata.models.datatype import XmlDateTime

import datetime
import logging

from ojp2 import OperatorRef

logger = logging.getLogger(__name__)

# err_str = "" #global error string

# define an error response immediatly and make sure the program can send it back (ignores all warnings that were before).
def error_response(error_text:str) -> Ojp:
    return Ojp(ojpresponse=
        Ojpresponse(service_delivery=
                    ServiceDelivery(response_timestamp=XmlDateTime.from_datetime(datetime.datetime.utcnow()),
                                    producer_ref="OJP2NOVA",
                                    error_condition=ServiceDeliveryStructure.ErrorCondition(other_error=OtherError(error_text)))))

# storing warnings to be sent with the answer
#def add_error(error_text:str):
#    global err_str
#    err_str=err_str+error_text
#    return

# include accumulated warnings into the response. Status not affected (so should be warnings)
# def add_error_response(sd:ServiceDeliveryStructure):
#   global err_str
# if err_str=="":
#     return sd
# sd.ErrorCondition(other_error=OtherError(err_str))
# return sd

def process_operating_ref_ojp2(operator_ref:OperatorRef) ->str:
    operator_ref_str=operator_ref.value
    return process_operating_ref(operator_ref_str)

def process_operating_ref(operator_ref:str) ->str:
    #operator_ref = operator_ref.value
    # Remove the 'ojp:' prefix if it exists
    if operator_ref.startswith("ojp:"):
        operator_ref = operator_ref[4:]

    # Check if the remaining string is a digit
    if operator_ref.isdigit():
        # Fill with zeros from the left to make it 6 characters long
        return operator_ref.zfill(6)
    else:
        # Return the original string if it's not an int or not 6 characters long
        return operator_ref

def sloid2didok(sloid:str)->int:
    # We make sure that whatever we get is a didok in the end.
    # It might be a didok, when we return it as integer
    # It might be a sloid, then we transform it into a didok (as integer)
    # With the sloid it is important that we go from the Quay level to the StopPlace level
    # An important part is that we transform to the commercial stops.
    # For this the dict is used
    # The list here is derived from https://confluence.sbb.ch/pages/viewpage.action?pageId=2608861819
    my_dict: Dict[str,str] ={
        "8507082": "8504108",
        "8503088": "8503000",
        "8519342": "8504014",
        "8014488": "8503467",
        "8014482": "8503466",
        "8014483": "8503465",
        "8014484": "8503464",
        "8014485": "8503463",
        "8014487": "8503462",
    }

    try:
        # sloids are not integer, but didok are. So we first try to convert to id. If this works, we assume, it is a didok code
        didok=int(sloid)
        didok=int(my_dict.get(str(didok),str(didok))) # replaces if it is in the table or gets the value back
        return didok
    except:
        #remove left part of sloid
        sloid=sloid.replace('ch:1:sloid:','')
        #remove the right part of sloid, if it exist
        if ':' in sloid:
            tmp = sloid[:sloid.find(':')]

        # if bigger than 100000 -> no add. This is used for the 11-14 prefixes that are used for sloid that are used for local public transport
        # outside Switzerland
        if int(tmp)>100000:
            return int(tmp)
        tmp= 8500000+int(tmp)
        tmp=my_dict.get(str(tmp),str(tmp)) # replaces if it is in the table or gets the value back
        return tmp



# raising an error and sending it back. Does not add values from err_str
class OJPError(Exception) :

    # Constructor or Initializer
    def __init__(self, value:str) -> None:
        self.value = value
        logger.error(value)

    # __str__ is to print() the value
    def __str__(self)->str:
        return (repr(self.value))