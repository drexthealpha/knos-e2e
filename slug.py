"""Turn a title into a URL slug."""


def slugify(title: str) -> str:
    slug = "-".join(title.lower().split()).strip("-")
    print(f"{title!r} -> {slug!r}")
    return slug
