import numpy as np
from typing import Union, Sequence


def lcs(a: Sequence[Union[str, np.dtype]], b: Sequence[Union[str, np.dtype]]) -> int:
    """
    Calculate the length of the longest common subsequence between two sequences.
    The sequences can be either lists of characters or NumPy arrays of characters.

    Parameters:
    a (Sequence[Union[str, np.dtype]]): The first sequence.
    b (Sequence[Union[str, np.dtype]]): The second sequence.

    Returns:
    int: The length of the longest common subsequence.

    Example:
    >>> lcs(np.array(list("ABCBDAB")), np.array(list("BDCABC")))
    4
    """
    # Initialize a 2D NumPy array with dimensions (len(a)+1) x (len(b)+1), filled with zeros
    dp = np.zeros((len(a) + 1, len(b) + 1), dtype=int)

    # Fill the dp array
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return int(dp[-1, -1])
