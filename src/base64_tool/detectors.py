import re
from collections.abc import Callable
from dataclasses import dataclass

from base64_tool.constants import (
    BASE32_CHARSET,
    BASE64_CHARSET,
    BASE64URL_CHARSET,
    CONFIDENCE_THRESHOLD,
    EncodingFormat,
    HEX_CHARSET,
    HEX_SEPARATORS,
    MIN_INPUT_LENGTH,
    ScoreWeight as W,
)
from base64_tool.encoders import try_decode
from base64_tool.util import is_printable_text

@dataclass(frozen=True, slots=True)
class DetectionResult:
    format: EncodingFormat
    confidence: float
    decoded: bytes | None

def _score_base64(data: str) -> float:
    pass

def _score_base64url(data: str) -> float:
    pass

def _score_base32(data: str) -> float:
    pass

def _score_url(data: str) -> float:
    pass

def _score_hex(data: str) -> float:
    pass
