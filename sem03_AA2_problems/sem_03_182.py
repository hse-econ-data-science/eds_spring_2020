# quick test
1 + 3

# set vs list

5 in [6, 7, 9, 13]

my_list = [6, 2, 5, 9]

my_list

my_set = set(my_list)

5 in my_list
5 in my_set

set([5, 5, 6, 5])

# Problem 1. Jewels and Stones

S = 'abcdefff'
J = 'bedf'

True + True + False

set_jewels = set(J)
set_jewels

num_gems = 0
for kamen in S:
    # print(kamen)
    # print(kamen in set_jewels)
    num_gems += (kamen in set_jewels) 

num_gems

def count_jewels(J, S):
    '''
    Function counts number of jewels in stones.

    Args:
        J: string of jewel letters
        S: string of stone letters
    '''
    set_jewels = set(J)
    num_gems = 0
    for kamen in S:
        num_gems += (kamen in set_jewels) 
    return num_gems

count_jewels('bd', 'abbddeeccCCCDDD')

from sem3_tests import *

test_num_jewels_in_stones(count_jewels)

def obmanka(J, S):
    return 3


obmanka('aaaa', 'sdfdf')


test_num_jewels_in_stones(obmanka)


vector = [5, 6, -2, 3, 7]
cum_sum = 0
cum_vector = []
for chislo in vector:
    cum_sum += chislo
    cum_vector.append(cum_sum)

cum_vector

def cum_sum(vector):
    '''
    Calculates cumulative sum of numbers in vector

    Args:
        vector: list of numbers
    '''
    cum_sum = 0
    cum_vector = []
    for chislo in vector:
        cum_sum += chislo
        cum_vector.append(cum_sum)
    return cum_vector

cum_sum([4, 5, 6, -6])


