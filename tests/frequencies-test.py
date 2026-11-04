import pytest
from frequencies import (
    word_frequencies
)

# ---------- word_frequencies ----------
def test_word_frequencies_basic():
    assert word_frequencies("To be or not to be") == {
        "to": 2,
        "be": 2,
        "or": 1,
        "not": 1,
    }


def test_word_frequencies_punctuation():
    assert word_frequencies("Hello, hello!") == {"hello": 2}


def test_word_frequencies_empty():
    assert word_frequencies("") == {}

def test_word_frequencies_python():
    assert word_frequencies("Python Python python") == {"python": 3}

def test_word_frequencies_alamakota():
    assert word_frequencies("Ala ma kota, a kot ma Alę") == {"ala": 1, "ma": 2, "kota": 1, "a": 1, "kot": 1, "alę": 1}
