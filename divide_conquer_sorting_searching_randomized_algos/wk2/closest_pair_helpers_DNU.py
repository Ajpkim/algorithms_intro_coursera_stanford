import math
from random import randint
from find_closest_pair import *


def dimensional_merge_sort(a, sort_criteria):
    """
    function that takes in array of 2d points and returns sorted array based on
    either x or y values.

    args:
        - a is an array of 2d points to be sorted
        - sort_criteria dictates which dimension to sort on, 0 for x, 1 for y

    returns:
        sorted array
    """

    if len(a) < 2:
        return a

    left = dimensional_merge_sort(a[:int(len(a)/2)], sort_criteria)
    right = dimensional_merge_sort(a[int(len(a)/2):], sort_criteria)

    return merge(left, right, sort_criteria)


def merge(left, right, sort_criteria):
    c = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index][sort_criteria] < right[right_index][sort_criteria]:
            c.append(left[left_index])
            left_index += 1
        else:
            c.append(right[right_index])
            right_index += 1

    if left_index == len(left):
        c.extend(right[right_index:])
    else:
        c.extend(left[left_index:])

    return c


def closest_pair_brute_force(Px):
    """
    function to calculate the closest pair with brute force. Will identify
    duplicate points as a closest pair

    args:
        Sorted array of 2d points

    returns:
        - 2 tuples representing the two closest points
    """
    best = float("inf")
    p1, q1 = (0, 0), (0, 0)

    for i in range(len(Px) - 1):
        for j in range(i+1, len(Px)):
            dist = calc_euclidean_dist(Px[i], Px[j])
            if dist < best:
                best = dist
                p1, q1 = Px[i], Px[j]

    return best, p1, q1


def calc_euclidean_dist(p1, p2):
    """Return int euclidean distance between two dimensional points p1, p2"""
    x_sqrd_diff = (abs(p1[0] - p2[0]))**2
    y_squrd_diff = (abs(p1[1] - p2[1]))**2

    return math.sqrt(x_sqrd_diff + y_squrd_diff)
