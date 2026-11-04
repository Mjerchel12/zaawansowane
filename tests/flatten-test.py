import pytest
from flatten import (
    flatten_list
)

# ---------- flatten_list ----------
@pytest.mark.parametrize(
    "nested, expected",
    [
        ([1, 2, 3], [1, 2, 3]),
        ([1, [2, 3], [4, [5]]], [1, 2, 3, 4, 5]),
        ([], []),
        ([[[1]]], [1]), 
        ([1, [2, [3, [4, ]]]], [1, 2, 3, 4]),
    ],
)
def test_flatten_list(nested, expected):
    assert flatten_list(nested) == expected
