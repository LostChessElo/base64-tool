import base64 as b64
import binascii
from collections.abc import Callable
from urllib.parse import (
    quote,
    quote_plus,
    unquote,
    unquote_plus,
)
from base64_tool.constants import EncodingFormat


type EncoderFn = Callable[[bytes], str]
type DecoderFn = Callable[[str], bytes]

def encode_base64(data: bytes) -> str:
    pass

def encode_base64url(data: bytes) -> str:
    pass

def encode_base32(data: bytes) -> str:
    pass

def encode_hex(data: bytes) -> str:
    pass

def encode_url(data: bytes) -> str:
    pass

def decode_base64(data: str) -> bytes:
    pass

def decode_base64url(data: str) -> bytes:
    pass

def decode_base32(data: str) -> bytes:
    pass

def decode_url(data: str) -> bytes:
    pass

def decode_hex(data: str) -> bytes:
    pass

ENCODER_REGISTRY: dict[
    EncodingFormat,
    tuple[EncoderFn, DecoderFn],
] = {
    EncodingFormat.BASE64: (encode_base64, decode_base64),
    EncodingFormat.BASE64URL: (encode_base64url, decode_base64url),
    EncodingFormat.BASE32: (encode_base32, decode_base32),
    EncodingFormat.HEX: (encode_hex, decode_hex),
    EncodingFormat.URL: (
        lambda data: encode_url(data),
        lambda data: decode_url(data),
    ),
}
