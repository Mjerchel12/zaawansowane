import pytest
from prime import (
    is_prime
)


# ---------- is_prime ----------
@pytest.mark.parametrize(
    "n, expected",
    [
        (2, True),
        (3, True),
        (4, False),
        (1, False),
        (0, False),
        (5, True),
        (97, True),
    ],
)
def test_is_prime(n, expected):
    assert is_prime(n) == expected