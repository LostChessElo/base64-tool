from codecs import encode
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
    layers: list[PeelLayer] = []
    current_data = data
    current_bytes = data.encode("utf-8")

    for depth in range(max_depth):
        detection = detect_best(current_data)

        if detection is None:
            break
        if detection.confidence < threshold:
            break
        if detection.decoded is None:
            break


        scores = (tuple(score_all_formats(current_data).items()) if verbose else ())

        decoded_bytes = detection.decoded
        print(decoded_bytes)
        layer = PeelLayer(
            depth=depth + 1,
            format=detection.format,
            confidence=detection.confidence,
            encoded_preview=truncate(current_data),
            decoded_preview=safe_bytes_preview(decoded_bytes),
            all_scores=scores,
        )
        layers.append(layer)
        current_bytes = decoded_bytes

        try:
            current_data = decoded_bytes.decode("utf-8")
        except (UnicodeDecodeError, ValueError):
            break


    return PeelResult(
        layers=tuple(layers),
        final_output=current_bytes,
        success=len(layers) > 0
    )