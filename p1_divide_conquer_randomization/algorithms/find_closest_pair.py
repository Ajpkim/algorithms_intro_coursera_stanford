import math

from random import randint

# Implementation of a divide and conquer algorithm to find the closest pair of
# points in a array of 2d points


def find_closest_pair(points):
    """
    Sorts points and then recursively computes the closest pair of points in
    the given array with calls to closest_pair() and closest_split_pair().

    Args:
        points: array of 2 dimensional points

    Returns:
        tuple of closest 2 points in given array
    """

    Px = dimensional_merge_sort(points, 0)  # sort by x values
    Py = dimensional_merge_sort(points, 1)  # sort by y values

    d, p, q = closest_pair(Px, Py)

    return (d, p, q)


def closest_pair(Px, Py):
    """
    function that recursively computes the closest pair of points within the
    given sorted arrays

    args:
        Px and Py are two sorted variations of same collection of 2d points

    returns:
        tuple of 2 points with smallest euclidean distance between them
    """
    if len(Px) < 4:
        return closest_pair_brute_force(Px)

    Qx = Px[:int(len(Px)/2)]
    Qy = [y for y in Py if y in Qx]

    Rx = Px[int(len(Px)/2):]
    Ry = [y for y in Py if y in Rx]

    dl, p1, q1 = closest_pair(Qx, Qy)

    dr, p2, q2 = closest_pair(Rx, Ry)

    d = min(dl, dr)
    ds, p3, q3 = closest_split_pair(Px, Py, d)

    min_distance = min(dl, dr, ds)

    if min_distance == (dl):
        return dl, p1, q1
    elif min_distance == (dr):
        return dr, p2, q2
    else:
        return ds, p3, q3


def closest_split_pair(Px, Py, d):
    """
    finds best split pair that is closer together than distance d

    args:
        Px, Py are sorted arrays of 2d points
        d is euclidean distance of closest points found in recursive calls

    returns:
        min closest split pair if distance is less than d
    """

    x_bar = Px[int(len(Px)/2)][0]  # largest x value of original leftside group

    strip_begin = x_bar - d
    strip_end = x_bar + d
    Sy = [y for y in Py if strip_begin < float(y[0]) < strip_end]
    best = d

    p, q = (0, 0), (0, 0)  # if no pairs found will return (0,0),(0,0)

    for i in range(len(Sy) - 1):
        for j in range((i + 1), min(i + 8, len(Sy))):

            ptest, qtest = Sy[i], Sy[j]
            dist = calc_euclidean_dist(Sy[i], Sy[j])

            if dist < best:
                best = dist
                p, q = Sy[i], Sy[j]

    return best, p, q


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
