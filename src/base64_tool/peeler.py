from dataclasses import dataclass

from base64_tool.constants import (
    CONFIDENCE_THRESHOLD,
    PEEL_MAX_DEPTH,
    EncodingFormat,
)
from base64_tool.detectors import detect_best, score_all_formats
from base64_tool.util import safe_bytes_preview, truncate

@dataclass(frozen=True, slots=True)
class PeelLayer:
    depth: int
    format: EncodingFormat
    confidence: float
    encoded_preview: str
    decoded_preview: str
    all_scores: tuple[tuple[EncodingFormat, float], ...] = ()

@dataclass(frozen=True, slots=True)
class PeelResult:
    layers: tuple[PeelLayer, ...]
    final_output: bytes
    success: bool


def peel(data: str, *, max_depth: int = PEEL_MAX_DEPTH, threshold: float = CONFIDENCE_THRESHOLD, verbose: bool = False) -> PeelResult:
    pass
