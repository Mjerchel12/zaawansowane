import pytest
from countvowels import (
    count_vowels
)
# ---------- count_vowels ----------
@pytest.mark.parametrize(
    "text, expected",
    [
        ("Python", 2),      # y, o
        ("AEIOUY", 6),
        ("bcd", 0),
        ("", 0),
        ("Próba żółwia", 5),  # ó, a, ó, i, a
    ],
)
def test_count_vowels(text, expected):
    assert count_vowels(text) == expected