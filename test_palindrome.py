from palindrome import palindrome
from count_palindromes import count_palindromes

def test_single_word_palindrome():
    assert palindrome("racecar") is True
    assert palindrome("madam") is True
    assert palindrome("level") is True
    assert palindrome("hello") is False
    assert palindrome("world") is False

def test_case_insensitivity():
    assert palindrome("Racecar") is True
    assert palindrome("MadAm") is True

def test_empty_string():
    assert palindrome("") is True
