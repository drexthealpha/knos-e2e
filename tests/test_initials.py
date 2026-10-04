from initials import initials


def test_first_letters_upper_cased():
    assert initials("ada lovelace") == "AL"


def test_blank_name_has_no_initials():
    assert initials("") == ""
