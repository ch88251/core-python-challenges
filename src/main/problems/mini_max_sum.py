"""
Given five positive integers, find the minimum and maximum values that can
be calculated by summing exactly four of the five integers. Then print the
respective minimum and maximum values as a single line of two space-separated
long integers.
Example:
    arr = [1,3,5,7,9]
    The minimum sum is 1+3+5+7=16, The maximum sum is 3+5+7+9=24
    Output: 16 24
"""
import math
import os
import random
import re
import sys


def mini_max_sum(arr):
    """
    Finds the minimum and maximum values that can be calculated by summing
    exactly four of the five integers in the given array.

    :param arr:
    :return: two integers separated by a single space, where the first
             integer is the min sum and the second integer is the max sum.
    """
    sums = []
    for num in arr:
        sums.append(sum(arr)-num)
    print(f'{min(sums)} {max(sums)}')
    return sums


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    mini_max_sum(arr)