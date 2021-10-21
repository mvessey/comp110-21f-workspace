"""Practice with dictionaries."""

__author__ = "730409403"


def invert(norm_dict: dict[str, str]) -> dict[str, str]:
    inverted_dict = {}
    for key, value in norm_dict.items():
        if value in inverted_dict.keys():
            raise KeyError("Two keys of same value cannot exist.")
        else:
            inverted_dict[value] = []
            inverted_dict[value].append(key)
    return inverted_dict


def favorite_color(colors: dict[str, str]) -> str:
    the_favorite_color = {}
    for key, value in colors.items():
        the_favorite_color.setdefault(value, set()).add(key)
    favorite_color = [key for key, values in the_favorite_color.items() if len(values) > 1]
    return str(favorite_color)


def count(list_values: list[str]) -> dict[str, int]:
    initial_dictionary = {}
    for item in list_values:
        if (item in initial_dictionary):
            initial_dictionary[item] += 1
        else:
            initial_dictionary[item] = 1
    return initial_dictionary