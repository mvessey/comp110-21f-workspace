"""Unit tests for dictionary functions."""


from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730409403"


def test_invert_equal_value_key() -> None:
    """Testing if one value = key with inverse function."""
    assert invert({'a': 'a', 'b': 'b'}) == {'a': ['a'], 'b': ['b']}


def test_invert_long() -> None:
    """Testing if long dictionary correctly inverts."""
    assert invert({'a': 'z', 'b': 'y', 'c': 'x'}) == {'z': ['a'], 'y': ['b'], 'x': ['c']}


def test_invert_ending_value() -> None:
    """Testing endpoints."""
    assert invert({'Boron': 'Boron', 'Helium': 'Sodium'}) == {'Boron': ['Boron'], 'Sodium': ['Helium']}


def test_favorite_color_equal() -> None:
    """Favorite colors with one value occuring more."""
    assert favorite_color({"Mark": "yellow", "Elena": "Blue", "Greg": "Blue"}) == "['Blue']"


def test_favorite_color_one_value() -> None:
    """Testing favorite color with all one value."""
    assert favorite_color({"Mark": "Blue", "Elena": "Blue", "Greg": "Blue"}) == "['Blue']"


def test_favorite_color() -> None:
    """Testing favorite color with favorite color as the beginnig and end of the dictionary."""
    assert favorite_color({"Mark": "Blue", "Elena": "Orange", "Patricia": "Pink", "Greg": "Blue"}) == "['Blue']"


def test_count_all_occur_equally() -> None:
    """Testing when all string items occur equally in list."""
    assert count(["Bob", "Henry", "Andrew"]) == {'Bob': 1, 'Henry': 1, 'Andrew': 1}


def test_count_middle_occurs_most() -> None:
    """Testing count when middle of list has strings that occur the most."""
    assert count(["Ken", "Barbie", "Barbie", "Midge"]) == {'Ken': 1, 'Barbie': 2, 'Midge': 1}


def test_count_outer_items_greater() -> None:
    """Testing count when greater amount of same strings occurs on the endpoints of the list."""
    assert count(["Ken", "Barbie", "Midge", "Ken"]) == {'Barbie': 1, 'Midge': 1, 'Ken': 2}