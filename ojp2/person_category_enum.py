from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class PersonCategoryEnum(Enum):
    ADULT = "adult"
    CHILD = "child"
    EMERGENCY_SERVICES_PERSON = "emergencyServicesPerson"
    FIREMAN = "fireman"
    INFANT = "infant"
    MEDICAL_STAFF = "medicalStaff"
    MEMBER_OF_THE_PUBLIC = "memberOfThePublic"
    POLICEMAN = "policeman"
    POLITICIAN = "politician"
    PUBLIC_TRANSPORT_PASSENGER = "publicTransportPassenger"
    SICK_PERSON = "sickPerson"
    TRAFFIC_OFFICER = "trafficOfficer"
    TRAFFIC_WARDEN = "trafficWarden"
    VERY_IMPORTANT_PERSON = "veryImportantPerson"
