"""Unit tests for list utility functions."""

from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730409403"


def test_only_evens_empty() -> None:
    """Testing accuracy of function only_evens, with no list."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_just_evens() -> None:
    """Testing accuracy with only evens."""
    assert only_evens([2, 4, 6]) == [2, 4, 6]


def test_only_evens_all_odd() -> None:
    """Tesing only_evens with all odd integers."""
    assert only_evens([1, 3, 5]) == []


def test_sub_start_negative() -> None:
    """Testing sub when beginning_value is zero."""
    assert sub([1, 2, 3, 4], -5, 2) == [1, 2]


def test_sub_invalid_end_index() -> None:
    """Testing function sub when ending value is great than the length of list."""
    assert sub([1, 2, 3, 4], 1, 5) == [2, 3, 4]


def test_sub_negative_middle() -> None:
    """Testing function sub when index is within normal range."""
    assert sub([0, 1, 2, 3, 4], 1, 3) == [1, 2]


def test_concat_empty_list() -> None:
    """Testing concat function with one empty list."""
    assert concat([1, 3, 7], []) == [1, 3, 7]


def test_concat_small_lists() -> None:
    """Testing concat function with two small lists."""
    assert concat([1, 4], [8, 3]) == [1, 4, 8, 3]


def test_concat_identical_lists() -> None:
    """Testing concat function w two identical lists."""
    assert concat([1, 2, 3], [1, 2, 3]) == [1, 2, 3, 1, 2, 3]