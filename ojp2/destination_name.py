from dataclasses import dataclass

from ojp2.natural_language_place_name_structure import (
    NaturalLanguagePlaceNameStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class DestinationName(NaturalLanguagePlaceNameStructure):
    """The name of the DESTINATION of the journey; used to help identify the
    VEHICLE to the public.

    Note when used in a CALL, this is the Dynamic Destination Display:
    since vehicles can change their destination during a journey, the
    destination included here should be what the VEHICLE will display
    when it reaches the stop.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
