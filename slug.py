"""Turn a title into a URL slug."""


def slugify(title: str) -> str:
    return title.strip().replace(" ", "-")
