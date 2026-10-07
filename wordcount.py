"""wordcount(phrase): how many words a phrase has (a word is a run of letters or digits)."""
import re


def wordcount(phrase: str) -> int:
    return len(re.findall(r"[A-Za-z0-9]+", phrase))
