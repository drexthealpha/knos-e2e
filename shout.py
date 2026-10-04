"""shout(text): the text in capitals, with one exclamation mark at the end."""


def shout(text: str) -> str:
    """'hello' gives 'HELLO!'; a text that already ends with '!' gets no second one."""
    up = text.upper()
    return up if up.endswith("!") else up + "!"
