import pytest # noqa
from palindrom import palindrom
from count_palindromes import count_palindromes

def test_single_word_palindrome():
    assert palindrom("racecar") is True
    assert palindrom("madam") is True
    assert palindrom("level") is True
    assert palindrom("hello") is False
    assert palindrom("world") is False

def test_case_insensitivity():
    assert palindrom("Racecar") is True
    assert palindrom("MadAm") is True

def test_empty_string():
    assert palindrom("") is True

def test_count_palindromes():
    assert count_palindromes("madam racecar level") == 3
    assert count_palindromes("hello world") == 0
    assert count_palindromes("A toyota's a toyota") == 1

def test_mixed_case_palindromes():
    assert count_palindromes("Racecar Madam Level") == 3

def test_sentence_with_punctuation():
    assert count_palindromes("Wow! Dad and Mom are here.") == 2