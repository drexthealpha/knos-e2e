"""Turn a title into a URL slug."""


def slugify(title: str) -> str:
    slug = "-".join(title.lower().split()).strip("-")
    print("slugify:", title, "->", slug)
    return slug
