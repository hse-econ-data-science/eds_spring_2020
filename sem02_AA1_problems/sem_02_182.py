from sem2_tests import *

!pwd
!ls
cd ..

def wrong_fib(n):
    return 42 * n

wrong_fib(6)
test_fibonacci(wrong_fib)

def slow_fib(n):
    if n < 3:
        return 1
    return slow_fib(n - 1) + slow_fib(n - 2)

slow_fib(6)

(1 + 5 ** 0.5) / 2
(1 - 5 ** 0.5) / 2

def approx_fib(n):
    q = (1 + 5 ** 0.5) / 2
    return q ** n / 5 ** 0.5

slow_fib(20)
approx_fib(20)

slow_fib(37)
approx_fib(37)

test_fibonacci(approx_fib)
approx_fib(1)
approx_fib(2)
approx_fib(3)

def fast_fib(n):
    return(round(approx_fib(n)))

fast_fib(10)
slow_fib(10)

test_fibonacci(fast_fib)
fast_fib(100)


round(5.5)
round(4.5)

4 - 1 
4 - 1 == 3

0.4 - 0.1 == 0.3
0.3 + 0.1 == 0.4