
"""
CS 1001 - Lab Programming 4: Searching Algorithms

Complete implementations of four searching algorithms.
"""


def find(values: list[int], target: int) -> int | None:
    """Return the index of the first occurrence of target, or None if absent."""

    for i in range(len(values)):
        if values[i] == target:
            return i

    return None


def is_descending(values: list[float]) -> bool:
    """Return True if values are in strictly descending order."""

    for i in range(1, len(values)):
        if values[i] >= values[i - 1]:
            return False

    return True


def index_of_largest(values: list[int]) -> int | None:
    """Return the index of the largest value, or None for an empty list."""

    if len(values) == 0:
        return None

    largest_index = 0

    for i in range(1, len(values)):
        if values[i] > values[largest_index]:
            largest_index = i

    return largest_index


def largest_between(values: list[int], lower: int, upper: int) -> int | None:
    """Return the index of the largest value in the inclusive index range."""

    if len(values) == 0:
        return None

    # Adjust the boundaries to stay within the list.
    if lower < 0:
        lower = 0

    if upper >= len(values):
        upper = len(values) - 1

    # Check whether any valid indexes remain.
    if lower > upper or lower >= len(values) or upper < 0:
        return None

    largest_index = lower

    for i in range(lower + 1, upper + 1):
        if values[i] > values[largest_index]:
            largest_index = i

    return largest_index
