from sem3_tests import *



a = [5, 7, 7, 2, 4, 6, 2]
a

b = set(a)
b

'крокодил' in a
'крокодил' in b

neznayu = (4, 5, [6, 7, -2])

neznayu[2] += [12, 35]

# problem 1
stones = 'aBdctrfaaB'
jewels = 'BRaty'

num_jewels = 0
for stone in stones:
    print(stone)
    print(stone in jewels)
    num_jewels += stone in jewels

num_jewels

True + True + True + False
5 + 6
'a' + 'sdfsd'
[5, 6] + [4, 7, 8]

def count_jewels(jewels, stones):
    '''
    Count the number of jewels in stones that I have

    Args:
        jewels: string of jewels, each letter is a jewel
        stones: string of stones, each letter is a stone
    '''
    jewels_set = set(jewels)
    num_jewels = 0
    for stone in stones:
        num_jewels += stone in jewels_set
    return num_jewels

count_jewels('ab', 'abababcdcdabcdab')

from sem3_tests import *
test_num_jewels_in_stones(count_jewels)

def mnepovezet(jewels, stones):
    return 3

mnepovezet('aaa', 'bb')
test_num_jewels_in_stones(mnepovezet)


# problem 2
# cumulative sum
def cum_sum(vector):
    cum_sum = []
    sum = 0
    for chislo in vector:
        sum += chislo
        cum_sum.append(sum)
    return cum_sum

cum_sum([5, 4, 3, 2, 1])

len([5, 6, 3, 2])
range(len([5, 6, 3, 2]))

def moving_average(vector, win_width):
    cum_vector = cum_sum(vector)
    average_vector = []
    for i in range(len(vector)):
        actual_win_width = min(i + 1, win_width)
        if i - actual_win_width == -1:
            diff = cum_vector[i]
        else:
            diff = cum_vector[i] - cum_vector[i - actual_win_width]
        average_vector.append(diff * 1.0 / actual_win_width)
    return average_vector

cum_sum([4, 5, 6, 7])
moving_average([4, 5, 6, 7], 3)
test_simple_moving_avarage(moving_average)