from dataclasses import dataclass

from ojp2.passenger_information_action_structure import (
    PassengerInformationActionStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class PassengerInformationAction(PassengerInformationActionStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
