from dataclasses import dataclass, field
from typing import List, Optional
from ojp.natural_language_place_name_structure import NaturalLanguagePlaceNameStructure
from ojp.natural_language_string_structure import NaturalLanguageStringStructure
from ojp.passage_between_trains_structure import PassageBetweenTrainsStructure
from ojp.train import Train
from ojp.via_name_structure import ViaNameStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class TrainInCompoundTrainStructure:
    """Type for a TRAIN IN COMPOUND TRAIN.

    (since SIRI 2.1)

    :ivar train_in_compound_train_code: Identifier for TRAIN IN COMPOUND
        TRAIN.
    :ivar order: Specifies the order of the TRAIN within the COMPOUND
        TRAIN.
    :ivar label: Specifies how the TRAIN is labeled within the context
        of the COMPOUND TRAIN. This advertised label or number, e.g. the
        individual TRAIN NUMBER, can be used for seat reservations and
        passenger orientation.
    :ivar description: Description of TRAIN IN COMPOUND TRAIN.
    :ivar train_ref:
    :ivar train:
    :ivar origin_ref:
    :ivar origin_name: Name of the origin of the journey.  (Unbounded
        since SIRI 2.0)
    :ivar origin_short_name: Short name of the origin of the journey;
        used to help identify the VEHICLE JOURNEY on arrival boards. If
        absent, same as Origin Name.
    :ivar destination_display_at_origin: DIRECTION name shown for jurney
        at the origin. (since SIRI 2.0)
    :ivar via: Names of VIA points, used to help identify the LINE, for
        example, Luton to Luton via Sutton. Currently 3 in VDV. Should
        only be included if the detail level was requested.
    :ivar destination_ref: Reference to a DESTINATION.
    :ivar destination_name: Description of the destination stop (vehicle
        signage), Can be overwritten for a journey, and then also
        section by section by the entry in an individual CALl.
        (Unbounded since SIRI 2.0)
    :ivar destination_short_name: Short name of the DESTINATION.of the
        journey; used to help identify the VEHICLE JOURNEY on arrival
        boards. If absent, same as DestinationName.  (Unbounded since
        SIRI 2.0)
    :ivar origin_display_at_destination: Origin name shown for jourey at
        the destination (since SIRI 2.0)
    :ivar reversed_orientation: Whether orientation of TRAIN within
        COMPOUND TRAIN is reversed or not. Default is 'false', i.e.,
        they have the same orientation (usually forward in the direction
        of travel).
    :ivar passages: Specifies whether a passage from/to an adjacent
        TRAIN is possible for passengers.
    """
    train_in_compound_train_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrainInCompoundTrainCode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "name": "Order",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    label: Optional[NaturalLanguageStringStructure] = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    description: Optional[NaturalLanguageStringStructure] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    train_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrainRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    train: Optional[Train] = field(
        default=None,
        metadata={
            "name": "Train",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    origin_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "OriginRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    origin_name: List[NaturalLanguagePlaceNameStructure] = field(
        default_factory=list,
        metadata={
            "name": "OriginName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    origin_short_name: List[NaturalLanguagePlaceNameStructure] = field(
        default_factory=list,
        metadata={
            "name": "OriginShortName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    destination_display_at_origin: List[NaturalLanguagePlaceNameStructure] = field(
        default_factory=list,
        metadata={
            "name": "DestinationDisplayAtOrigin",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    via: List[ViaNameStructure] = field(
        default_factory=list,
        metadata={
            "name": "Via",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    destination_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DestinationRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    destination_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "DestinationName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    destination_short_name: List[NaturalLanguagePlaceNameStructure] = field(
        default_factory=list,
        metadata={
            "name": "DestinationShortName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    origin_display_at_destination: List[NaturalLanguagePlaceNameStructure] = field(
        default_factory=list,
        metadata={
            "name": "OriginDisplayAtDestination",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    reversed_orientation: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReversedOrientation",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    passages: Optional["TrainInCompoundTrainStructure.Passages"] = field(
        default=None,
        metadata={
            "name": "Passages",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )

    @dataclass
    class Passages:
        passage_between_trains: List[PassageBetweenTrainsStructure] = field(
            default_factory=list,
            metadata={
                "name": "PassageBetweenTrains",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
                "max_occurs": 2,
            }
        )
