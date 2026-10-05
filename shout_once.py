def shout_once(text):
    """The text in capitals with exactly one "!" at the end."""
    return text.upper().rstrip("!") + "!"
