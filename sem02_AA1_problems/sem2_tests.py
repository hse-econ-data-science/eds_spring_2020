def test_problem(func, test_data):
    for inputs, true_answer in test_data:
        answer = func(inputs)
        assert answer == true_answer, f'Expected {true_answer}, got {answer}. Input: {inputs}'
    print("OK!")


def test_fizz_buzz(fizz_buzz_func):
    FIZZ_BUZZ_TESTS_DATA = [
        (1, ["1"]),
        (2, ["1", "2"]),
        (15, ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]),
    ]
    test_problem(fizz_buzz_func, FIZZ_BUZZ_TESTS_DATA)


def test_fibonacci(fibonacci_func):
    FIBONACCI_TESTS_DATA = [
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (10, 55),
        (40, 102334155),
    ]
    test_problem(fibonacci_func, FIBONACCI_TESTS_DATA)


def test_find_duplicates(find_duplicates_func):
    FIND_DUPLICATES_TESTS_DATA = [
        ([1], []),
        ([1, 1], [1]),
        ([1, 1, 2, 2], [1, 2]),
    ]
    test_problem(find_duplicates_func, FIND_DUPLICATES_TESTS_DATA)


def test_word_frequency(count_word_frequency_func):
    WORD_FREQUENCY_TESTS_DATA = [
        ('game game  of of of thrones', [('of', 3), ('game', 2), ('thrones', 1)]),
    ]
    test_problem(count_word_frequency_func, WORD_FREQUENCY_TESTS_DATA)


def test_valid_palindrome(is_almost_palindrome_func):
    VALID_PALINDROME_TESTS_DATA = [
        ("aba", True),
        ("abca", True),
        ("abcd", False)
    ]
    test_problem(is_almost_palindrome_func, VALID_PALINDROME_TESTS_DATA)


def test_longest_substring(longest_substring_func):
    LONGEST_SUBSTRING_TESTS_DATA = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3)
    ]
    test_problem(longest_substring_func, LONGEST_SUBSTRING_TESTS_DATA)
