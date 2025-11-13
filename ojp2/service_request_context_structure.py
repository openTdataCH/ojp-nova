from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDuration

from ojp2.data_name_spaces_structure import DataNameSpacesStructure
from ojp2.delivery_method_enumeration import DeliveryMethodEnumeration
from ojp2.empty_type import EmptyType
from ojp2.predictors_enumeration import PredictorsEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ServiceRequestContextStructure:
    """Configurable context for requests.

    Intended Primarily as a documentation mechanism.

    :ivar check_status_address: Address to which CheckStatus requests
        are to be sent.
    :ivar subscribe_address: Address to which subscription requests are
        to be sent.
    :ivar manage_subscription_address: Address to which subscription
        requests are to be sent. If absent, same as SubscribeAddress.
    :ivar get_data_address: Address to which requests are to return
        data.
    :ivar status_response_address: Address to which CheckStatus
        responses and heartbeats are to be sent. If absent, same as
        SubscriberAddress.
    :ivar subscriber_address: Address to which subscription responses
        are to be sent.
    :ivar notify_address: Address to which notifcations requests are to
        be sent. If absent, same as SubscriberAddress.
    :ivar consumer_address: Address to which data is to be sent. If
        absent, same as NotifyAddress.
    :ivar data_name_spaces: Default names pace used to scope data
        identifiers.
    :ivar language: Preferred languages in which to return text values.
    :ivar wgs_decimal_degrees: Geospatial coordinates are given as Wgs
        84 Latiude and longitude, decimial degrees of arc.
    :ivar gml_coordinate_format: Name of GML Coordinate format used for
        Geospatial points in responses.
    :ivar distance_units: Units for Distance Type. Default is metres.
        (since SIRI 2.0)
    :ivar velocity_units: Units for Distance Type. Default is metres per
        second. (since SIRI 2.0)
    :ivar data_horizon: Maximum data horizon for requests.
    :ivar request_timeout: Timeout for requests. [Should this be
        separate for each type?]
    :ivar delivery_method: Whether Delivery is fetched or retrieved.
    :ivar multipart_despatch: Whether multi-part delivery is allowed,
        i.e. the breaking up of updates into more than one delivery
        messages with a MoreData flag,
    :ivar confirm_delivery: Whether Consumers should issue an
        acknowledgement on successful receipt of a delivery. Default is
        ' false'.
    :ivar maximimum_number_of_subscriptions: Maximum Number of
        subscriptions that can be sustained by the subscriber. If absent
        no limit.
    :ivar allowed_predictors: Who may make a prediction.
    :ivar prediction_function: Name of prediction method used.
    """

    check_status_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "CheckStatusAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    subscribe_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubscribeAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    manage_subscription_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "ManageSubscriptionAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    get_data_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "GetDataAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    status_response_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "StatusResponseAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    subscriber_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubscriberAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    notify_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "NotifyAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    consumer_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConsumerAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    data_name_spaces: Optional[DataNameSpacesStructure] = field(
        default=None,
        metadata={
            "name": "DataNameSpaces",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    language: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Language",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    wgs_decimal_degrees: Optional[EmptyType] = field(
        default=None,
        metadata={
            "name": "WgsDecimalDegrees",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    gml_coordinate_format: Optional[str] = field(
        default=None,
        metadata={
            "name": "GmlCoordinateFormat",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    distance_units: Optional[str] = field(
        default=None,
        metadata={
            "name": "DistanceUnits",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    velocity_units: Optional[str] = field(
        default=None,
        metadata={
            "name": "VelocityUnits",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    data_horizon: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "DataHorizon",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    request_timeout: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "RequestTimeout",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    delivery_method: Optional[DeliveryMethodEnumeration] = field(
        default=None,
        metadata={
            "name": "DeliveryMethod",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    multipart_despatch: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MultipartDespatch",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    confirm_delivery: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ConfirmDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    maximimum_number_of_subscriptions: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximimumNumberOfSubscriptions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    allowed_predictors: Optional[PredictorsEnumeration] = field(
        default=None,
        metadata={
            "name": "AllowedPredictors",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    prediction_function: Optional[str] = field(
        default=None,
        metadata={
            "name": "PredictionFunction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
