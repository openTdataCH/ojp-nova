
from ojp import Ojp, Ojpresponse, ServiceDelivery, ServiceDeliveryStructure, OtherError
from xsdata.models.datatype import XmlDateTime

import datetime

from ojp2 import OperatorRef


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
    operator_ref=operator_ref.value
    return process_operating_ref(operator_ref)

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

def sloid2didok(sloid)->int:
    # TODO this is a hack for the timetable change 2024/2025 must be done correctly in map_ojp_to_ojp.py by replacing the stoppoints with the correct didoks
    #if a didok code, just return it
    my_dict ={
    }
    #dict from https://confluence.sbb.ch/pages/viewpage.action?pageId=2608861819
    #"8507082": "8504108",
    #"8503088": "8503000",
    #"8519342": "8504014",
    #"8014488": "8503467",
    #"8014482": "8503466",
    #"8014483": "8503465",
    #"8014484": "8503464",
    #"8014485": "853463",
    #"8014487": "8503462",
    if type(sloid)!=str:
        #must be a StopPointRef or StopPlaceRef TODO:Why is this different in OJP 1 and 2
        sloid=sloid.value
    try:
        didok=int(sloid)
        didok=int(my_dict.get(str(didok),str(didok))) # replaces if it is in the table or gets the value back
        return didok
    except:
        #remove left part of sloid
        sloid=sloid.replace('ch:1:sloid:','')
        if ':' in sloid:
            sloid = sloid[:sloid.find(':')]
        #remove the right part of sloid, if it exist
        #if bigger than 100000 -> no add
        sloid=int(my_dict.get(str(sloid),str(sloid))) # replaces if it is in the table or gets the value back
        if int(sloid)>100000:
            return int(sloid)
        return 8500000+int(sloid)

# raising an error and sending it back. Does not add values from err_str
class OJPError(Exception) :

    # Constructor or Initializer
    def __init__(self, value):
        self.value = value

    # __str__ is to print() the value
    def __str__(self):
        return (repr(self.value))