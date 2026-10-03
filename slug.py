"""Turn a title into a URL slug."""
import re


def slugify(title: str) -> str:
    return "-".join(re.findall(r"[a-z0-9]+", title.lower()))
