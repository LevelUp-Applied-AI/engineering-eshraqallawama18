"""
test_functions.py — Day 7: First Tests

Run these tests with:
    pytest test_functions.py

All 5 tests will fail at first. Fix the bugs in functions.py until they all pass.
"""

from functions import add, celsius_to_fahrenheit, count_vowels, first_word, is_even


def test_add():
    assert add(2, 3) == 5


def test_is_even():
    assert is_even(4) is True
    assert is_even(7) is False


def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212


def test_count_vowels():
    assert count_vowels("hello") == 2
    assert count_vowels("aeiou") == 5


def test_first_word():
    assert first_word("hello world") == "hello"
    assert first_word("pytest is great") == "pytest"
