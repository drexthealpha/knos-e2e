"""initials(name): the capital initials of a name."""
import re


def initials(name: str) -> str:
    """One capital per word, where a word is a run of ASCII letters: 'jean-luc picard' gives 'JLP'."""
    return "".join(w[0].upper() for w in re.findall(r"[A-Za-z]+", name))
