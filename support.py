from typing import Dict

from ojp import Ojp, Ojpresponse, ServiceDelivery, ServiceDeliveryStructure, OtherError
from xsdata.models.datatype import XmlDateTime

import datetime
import logging

from ojp2 import OperatorRef
from datetime import datetime, timedelta, timezone
import random
import re
from typing import Pattern

logger = logging.getLogger(__name__)


# err_str = "" #global error string

# define an error response immediatly and make sure the program can send it back (ignores all warnings that were before).
def error_response(error_text:str) -> Ojp:
    return Ojp(ojpresponse=
        Ojpresponse(service_delivery=
                    ServiceDelivery(response_timestamp=XmlDateTime.from_datetime(datetime.datetime.utcnow()),
                                    producer_ref="OJP2NOVA",
                                    error_condition=ServiceDeliveryStructure.ErrorCondition(other_error=OtherError(error_text)))))

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

def is_version_2_0(xml_string:str) -> bool:
    #simple test to see if the xml is OJP version 2.0 (or should be)
    # Split the string into lines
    lines = xml_string.splitlines()

    # Check if there are at least two lines
    if len(lines) < 2:
        return False
    #check the first line for the version (when the xml header was omitted)
    if 'version="2.0"' in lines[0]:
        return True
    # Check the second line for the version
    second_line = lines[1]
    if 'version="2.0"' in second_line:
        return True
    return False


def build_timestamp(days_in_future: int | None = None, start_time: str | None = None) -> str:
    if days_in_future is None and start_time is None:
        raise ValueError("Either days_in_future or start_time must be provided.")
    if days_in_future is not None:
        if not isinstance(days_in_future, int) or days_in_future < 0:
            raise ValueError("days_in_future must be a non-negative integer.")

    if start_time is not None:
        TIME_RE = re.compile(r'^(\d{2}):(\d{2}):(\d{2})$')
        m = TIME_RE.match(start_time)
        if not m:
            raise ValueError('start_time must be in "HH:MM:SS" format.')
        h, mnt, s = map(int, m.groups())
        if not (0 <= h <= 23 and 0 <= mnt <= 59 and 0 <= s <= 59):
            raise ValueError("start_time components out of range.")
        hours, minutes, seconds = h, mnt, s
    else:
        start_sec = 8 * 3600
        end_sec = 12 * 3600
        rand_sec = random.randint(start_sec, end_sec - 1)
        hours = rand_sec // 3600
        minutes = (rand_sec % 3600) // 60
        seconds = rand_sec % 60

    days = 0 if days_in_future is None else days_in_future

    now_utc = datetime.now(timezone.utc)
    target_date = (now_utc + timedelta(days=days)).replace(hour=hours, minute=minutes, second=seconds, microsecond=random.randrange(0,1000)*1000, tzinfo=timezone.utc)
    # isoformat with Z
    iso = target_date.isoformat(timespec='milliseconds')
    if iso.endswith('+00:00'):
        iso = iso[:-6] + 'Z'
    return iso


def insert_before_line_with_substring(text: str, pattern: str, insert: str) -> str:
    lines = text.splitlines(keepends=True)
    for i, line in enumerate(lines):
        if pattern in line:
            lines.insert(i, insert)
            return ''.join(lines)
    return text

def inject_departure_datetime(ojp_trip_request_xml : str, daysinthefuture : int,start_time : str) -> str:
     # TODO: shaky
     # build the date
     ts=build_timestamp(daysinthefuture,start_time)
     if is_version_2_0(ojp_trip_request_xml):
         #wrap the result
         ts="<DepArrTime>"+ts+"</DepArrTime>"
         return insert_before_line_with_substring(ojp_trip_request_xml,"</Origin>",ts)
     #wrap the result
     ts="<ojp:DepArrTime>"+ts+"</ojp:DepArrTime>"
     return insert_before_line_with_substring(ojp_trip_request_xml,"</ojp:Origin>",ts)

# raising an error and sending it back. Does not add values from err_str
class OJPError(Exception) :

    # Constructor or Initializer
    def __init__(self, value:str) -> None:
        self.value = value
        logger.error(value)

    # __str__ is to print() the value
    def __str__(self)->str:
        return (repr(self.value))


