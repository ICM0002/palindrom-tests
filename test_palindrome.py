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

def test_count_palindromes():
    assert count_palindromes("madam racecar level") == 3
    assert count_palindromes("hello world") == 0
    assert count_palindromes("A toyota's a toyota") == 1

def test_mixed_case_palindromes():
    assert count_palindromes("Racecar Madam Level") == 3

def test_sentence_with_punctuation():
    assert count_palindromes("Wow! Dad and Mom are here.") == 2
