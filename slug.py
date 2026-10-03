"""Turn a title into a URL slug."""


def slugify(title: str) -> str:
    return "-".join(title.lower().split()).strip("-")
