# ipython is needed for magic commands
!pwd 
!ls
cd ..

from sem2_tests import *

def wrong_fib(n):
    '''
    wrong fibonacci function
    '''
    return 2 * n

def slow_fib(n):
    '''
    slow fibonacci function
    '''
    if n < 3:
        return 1
    return slow_fib(n - 1) + slow_fib(n - 2)

# square root
56 ** 0.5

def app_fib(n):
    '''
    approximate fibonacci function
    two roots z^2 - z - 1 = 0
    |z_1| > 1, |z_2| < 1
    '''
    q5 = 5 ** 0.5
    return  ((1 + q5) / 2) ** n / q5

# fast fibonacci function
def fast_fib(n):
    '''
    fast fibonacci function
    '''
    return round(app_fib(n))


# float number surprises
round(5.5)
round(4.5)

4 - 1 == 3
0.4 - 0.1 == 0.3
3 + 1 == 4
0.3 + 0.1 == 0.4
