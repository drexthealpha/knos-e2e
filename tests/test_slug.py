from slug import slugify


def test_spaces_become_hyphens():
    assert slugify("Hello World") == "hello-world"


def test_case_is_lowered():
    assert slugify("KNOS") == "knos"
