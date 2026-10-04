"""Whether a text reads the same backwards."""


def is_palindrome(text: str) -> bool:
    letters = "".join(text.lower().split())
    return letters == letters[::-1]
