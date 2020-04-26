import math


def karatsuba(x, y):
    # handle negatives
    # x, y = abs(x), abs(y)

    # recursive base case
    if x < 10 and y < 10:
        return x * y

    else:
        n = max(len(str(x)), len(str(y)))
        m = int(math.ceil(float(n) / 2))  # (n // 2)

        x1 = x // (10**m)
        x2 = x % (10**m)
        y1 = y // (10**m)
        y2 = y % (10**m)

        s1 = karatsuba(x1, y1)
        s2 = karatsuba(x2, y2)
        s3 = karatsuba((x1 + x2), (y1 + y2))  # Err (x1 + x2) * (y1 + y2)
        s4 = s3 - s2 - s1

        result = (s1 * (10**(m*2)) + s4 * (10**m) + s2)

    # if (x < 0 and y > 0) or (y < 0 and x > 0):
    #     return (-1 * result)
    #
    # else:
        return result


x = -505876
y = 100376

print("test: x={}, y={}".format(x, y))
print("expected:", x * y)
print("result:", karatsuba(x, y))
print("test:", ((x*y) == karatsuba(x, y)))
