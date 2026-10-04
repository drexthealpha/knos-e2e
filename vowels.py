"""Count the vowels of a text."""


def count_vowels(text: str) -> int:
    return sum(1 for ch in text.lower() if ch in "aeiou")
