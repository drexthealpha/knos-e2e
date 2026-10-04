from palindrome import is_palindrome


def test_case_and_spaces_are_ignored():
    assert is_palindrome("Never odd or even")


def test_not_a_palindrome():
    assert not is_palindrome("knos")
