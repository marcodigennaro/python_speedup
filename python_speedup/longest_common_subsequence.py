import numpy as np


def lcs(a, b):
    """
    Calculate the length of the longest common subsequence between two sequences.

    Parameters:
    string_a (str): The first sequence.
    string_b (str): The second sequence.

    Returns:
    int: The length of the longest common subsequence between 'a' and 'b'.

    Example:
    >>> a = "ABCBDAB"
    >>> b = "BDCABC"
    >>> print(lcs(a, b))
    4
    """
    # Create a 2D array 'dp' with dimensions (len(a)+1) x (len(b)+1)
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

    # Fill the dp table with an optimal sub-problem relation
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                # If characters match, increment the value from the top-left diagonal
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # If not a match, take the maximum value from the left or above cell
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # The bottom-right cell will have the length of the longest common subsequence
    return dp[-1][-1]


def lcs_numpy(a, b):
    """
    Calculate the length of the longest common subsequence between two sequences using NumPy for enhanced performance.

    Parameters:
    a (str): The first sequence.
    b (str): The second sequence.

    Returns:
    int: The length of the longest common subsequence.

    Example:
    >>> lcs("ABCBDAB", "BDCABC")
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

    # The bottom-right cell contains the length of the LCS
    return dp[-1, -1]


