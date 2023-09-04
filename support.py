
from ojp import Ojp, Ojpresponse, ServiceDelivery, ServiceDeliveryStructure, OtherError
from xsdata.models.datatype import XmlDateTime

import datetime

err_str = "" #global error string

# define an error response immediatly and make sure the program can send it back (ignores all warnings that were before).
def error_response(error_text:str):
    return Ojp(ojpresponse=
        Ojpresponse(service_delivery=
                    ServiceDelivery(response_timestamp=XmlDateTime.from_datetime(datetime.datetime.utcnow()),
                                    producer_ref="OJP2NOVA",
                                    error_condition=ServiceDeliveryStructure.ErrorCondition(other_error=OtherError(error_text)))))

# storing warnings to be sent with the answer
def add_error(error_text:str):
    global err_str
    err_str=err_str+error_text
    return

# include accumulated warnings into the response. Status not affected (so should be warnings)
def add_error_response(sd:ServiceDeliveryStructure):
  global err_str
  if err_str=="":
      return sd
  sd.ErrorCondition(other_error=OtherError(err_str))
  return sd


# raising an error and sending it back. Does not add values from err_str
class OJPError(Exception):

    # Constructor or Initializer
    def __init__(self, value):
        self.value = value

    # __str__ is to print() the value
    def __str__(self):
        return (repr(self.value))