from shout import shout


def test_shout():
    assert shout("hello") == "HELLO!"


def test_no_second_mark():
    assert shout("hi!") == "HI!"
