"""Turn a title into a URL slug."""
import re


def slugify(title: str) -> str:
    print("slugify:", title)
    words = re.sub(r"[^a-z0-9\s-]", "", title.lower().replace("__", " ")).split()
    return "-".join(words).strip("-")
