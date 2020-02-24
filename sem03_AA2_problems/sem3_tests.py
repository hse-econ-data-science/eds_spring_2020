import matplotlib
import matplotlib.pyplot as plt

import numpy as np


def test_problem(func, test_data):
    for inputs, true_answer in test_data:
        answer = func(*inputs)
        assert answer == true_answer, f'Expected {true_answer}, got {answer}. Input: {inputs}'
    print("OK!")


def test_num_jewels_in_stones(num_jewels_in_stones_func):
    NUM_JEWELS_IN_STONES_TESTS_DATA = [
        (("aA", "aAAbbbb"), 3),
    ]
    test_problem(num_jewels_in_stones_func, NUM_JEWELS_IN_STONES_TESTS_DATA)


def test_simple_moving_avarage(simple_moving_avarage_func):
    MOVING_AVARAGE_TESTS_DATA = [
        (([3, 9, 12, 15], 3), [3, 6, 8, 12]),
    ]
    test_problem(simple_moving_avarage_func, MOVING_AVARAGE_TESTS_DATA)


def visual_test_simple_moving_avarage(moving_average_func, window):
    N = 1000
    array = np.sqrt(np.linspace(0, 100, N)) + np.random.normal(0, 1, N)
    array = np.round(array, 2)
    plt.figure(figsize=(12, 3))
    plt.plot(array)
    plt.plot(moving_average_func(np.copy(array), window))
    plt.show()


def test_longest_substring(longest_substring_func):
    LONGEST_SUBSTRING_TESTS_DATA = [
        (["abcabcbb"], 3),
        (["bbbbb"], 1),
        (["pwwkew"], 3)
    ]
    test_problem(longest_substring_func, LONGEST_SUBSTRING_TESTS_DATA)


def test_two_sum(two_sum_func):
    TWO_SUM_TESTS_DATA = [
        ([[2, 7, 11, 15], 9], (0, 1)),
    ]
    test_problem(two_sum_func, TWO_SUM_TESTS_DATA)


def test_remove_repeated_spaces(remove_repeated_spaces_func):
    TWO_SPACES_TEST_DATA = [
        ([list("aa  a  a   a")], list("aa a a a")),
    ]
    test_problem(remove_repeated_spaces_func, TWO_SPACES_TEST_DATA)
