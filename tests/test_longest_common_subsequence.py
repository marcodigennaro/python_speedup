import pytest
from python_speedup.longest_common_subsequence import lcs

# Fixture to provide different test cases
@pytest.fixture(params=[
    ("ABCBDAB", "BDCABC", 4),
    ("abc", "abc", 3),
    ("1234", "4321", 1),
    ("", "nonempty", 0),
    ("nonempty", "", 0),
    ("a", "b", 0),
    ("same", "same", 4)
])
def test_cases(request):
    return request.param


def test_lcs(test_cases):
    """
    Test the lcs function to ensure it correctly computes the length of the longest common subsequence.
    """
    a, b, expected = test_cases
    assert lcs(a, b) == expected, f"Failed for inputs {a} and {b}"


def test_lcs_type_error():
    """
    Test that the lcs function raises an error when the inputs are not of type str.
    """
    with pytest.raises(TypeError):
        lcs(123, 456)  # Non-string inputs


def test_lcs_empty_input():
    """
    Test the lcs function with empty strings to ensure it returns zero.
    """
    assert lcs("", "") == 0, "Failed for two empty strings"
