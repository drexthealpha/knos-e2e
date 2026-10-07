from wordcount import wordcount


def test_wordcount():
    assert wordcount("one, two-three  4") == 4
    assert wordcount("") == 0
