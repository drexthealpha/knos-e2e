from slug import slugify


def test_spaces_become_hyphens():
    assert slugify("Hello World") == "hello-world"


def test_case_is_lowered():
    assert slugify("KNOS") == "knos"


def test_runs_of_spaces_become_one_hyphen():
    assert slugify("a   b") == "a-b"


def test_no_hyphen_at_either_end():
    assert slugify("-a b-") == "a-b"
