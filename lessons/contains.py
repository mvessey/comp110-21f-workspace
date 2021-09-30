"""Example of writing a function to process a list."""


def main() -> None:
    """entrypoint of program."""
    names: list[str] = ["Kris", "Kaki"]
    print(contains("Kevin", names))


def contains(needle: str, haystack: list[str]) -> bool:
    """Return true if needle is found in the haystack, False others"""
    i: int = 0
    while i < len(haystack):
        item: str = haystack[i]
        if item == needle:
            return True
        i += 1
    return False


if __name__ == "__main__":
    main()