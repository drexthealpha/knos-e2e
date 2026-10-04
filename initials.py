"""The initials of a name."""


def initials(name: str) -> str:
    return "".join(word[0].upper() for word in name.split())
