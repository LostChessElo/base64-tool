from src.base64_tool.util import (
    is_printable_text,
    safe_bytes_preview,
    truncate,
)

def test_truncate_short_string_unchanged():
    assert truncate("hello") == "hello"

def test_truncate_exact_length_unchanged():
    assert truncate("a" * 72) == "a" * 72

def test_truncate_long_string():
    assert truncate("a" * 100) == "a" * 72 + "..."

def test_truncate_custom_length():
    assert truncate("hello world", length=5) == "hello..."


def test_safe_bytes_preview_valid_utf8():
    assert safe_bytes_preview(b"hello") == "hello"

def test_safe_bytes_preview_truncates():
    assert safe_bytes_preview(b"a" * 100) == "a" * 72 + "..."

def test_safe_bytes_preview_invalid_utf8_falls_back_to_hex():
    data = bytes([0xFF, 0xFE])
    assert safe_bytes_preview(data) == data.hex()


def test_is_printable_text_normal_text():
    assert is_printable_text(b"hello world") is True

def test_is_printable_text_with_newlines_and_tabs():
    assert is_printable_text(b"line1\nline2\ttabbed") is True

def test_is_printable_text_invalid_utf8():
    assert is_printable_text(bytes([0xFF, 0xFE])) is False

def test_is_printable_text_empty():
    assert is_printable_text(b"") is False

def test_is_printable_text_mostly_binary():
    # only ~10% printable, well below 0.8
    data = bytes(range(256))
    assert is_printable_text(data) is False

def test_is_printable_text_custom_threshold():
    data = b"hello\x01\x02\x03\x04"
    assert is_printable_text(data, threshold=0.5) is True
    assert is_printable_text(data, threshold=0.8) is False
