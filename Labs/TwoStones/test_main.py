"""Module to test important functions in main.py
"""

import main

# test function must start with test_ prefix for pytest to recognize it


def test_odd_even():
    """Function to test odd_even function"""
    number = 99999
    expected = "odd"
    ans = main.odd_even(number)
    assert (main.odd_even(number) == ans), f"Expected: {expected}, but got: {ans}"


def test_odd_even2():
    assert (main.odd_even(200) == "even"), f"Expected: even, but got: {main.odd_even(200)}"

def test_odd_even3():
    assert (main.odd_even(0) == "even"), f"Expected: even, but got: {main.odd_even(0)}"

def test_odd_even4():
    assert (main.odd_even(69) == "odd"), f"Expected: odd, but got: {main.odd_even(69)}"

test_odd_even()
test_odd_even2()
test_odd_even3()
test_odd_even4()

def test_answer():
    assert (main.answer(50) == "Bob"), f"Expected: Bob, but got: Alice"

def test_answer2():
    assert (main.answer(51) == "Alice"), f"Expected: Alice, but got: Bob"

def test_answer3():
    assert (main.answer(1) == "Alice"), f"Expected: Alice, but got: Bob"

test_answer()
test_answer2()
test_answer3()

# FIXME 5: Write 3rd test case #FIXED#
# FIXME 6: Write 4th test case #FIXED#


# FIXME 7: Write 3 test functions to test answer function #FIXED#
