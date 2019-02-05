import logging

from .types import (
    TimeStampReq, MessageImprint, PKIFreeText, PKIStatus, PKIFailureInfo,
    PKIStatusInfo, TimeStampResp, Accuracy, AnotherName, GeneralName,
    TimeStampToken, TSTInfo,
)
from .constants import (
    id_kp_timeStamping, id_sha1, id_sha256, id_sha384,
    id_sha512, id_ct_TSTInfo, oid_to_hash,
)
from .api import (
    RemoteTimestamper, check_timestamp, get_hash_oid,
    TimestampingError, get_timestamp, make_timestamp_request,
    encode_timestamp_request, encode_timestamp_response,
    decode_timestamp_request, decode_timestamp_response,
)


logging.getLogger(__name__).addHandler(logging.NullHandler())

__all__ = (
    'VERSION',

    'TimeStampReq', 'MessageImprint', 'PKIFreeText', 'PKIStatus', 'PKIFailureInfo',
    'PKIStatusInfo', 'TimeStampResp', 'Accuracy', 'AnotherName', 'GeneralName',
    'TimeStampToken', 'TSTInfo',

    'id_kp_timeStamping', 'id_sha1', 'id_sha256', 'id_sha384',
    'id_sha512', 'id_ct_TSTInfo', 'oid_to_hash',

    'RemoteTimestamper', 'check_timestamp', 'get_hash_oid',
    'TimestampingError', 'get_timestamp', 'make_timestamp_request',
    'encode_timestamp_request', 'encode_timestamp_response',
    'decode_timestamp_request', 'decode_timestamp_response',
)

VERSION = '3.0-dev'
