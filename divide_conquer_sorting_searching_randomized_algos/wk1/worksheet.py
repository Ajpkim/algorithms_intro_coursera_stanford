# import math
#
#
# def karatsuba(x, y):
#     if x < 10 and y < 10:
#         return x * y
#
#     n = max(len(str(x)), len(str(y)))
#     m = int(math.ceil(float(n) / 2))
#
#     # divide x into two half
#     xh = int(math.floor(x / 10 ** m))
#     xl = int(x % (10 ** m))
#
#     # divide y into two half
#     yh = int(math.floor(y / 10 ** m))
#     yl = int(y % (10 ** m))
#
#     # Karatsuba's algorithm.
#     s1 = karatsuba(xh, yh)
#     s2 = karatsuba(yl, xl)
#     s3 = karatsuba(xh + xl, yh + yl)
#     s4 = s3 - s2 - s1
#
#     return int(s1 * (10 ** (m*2)) + s4 * (10 ** m) + s2)
#
#
# x = 50
# y = -1003
#
# print("test: x={}, y={}".format(x, y))
# print("expected:", x * y)
# print("result:", karatsuba(x, y))
# print("test:", ((x*y) == karatsuba(x, y)))

print(-7 % 3)
print(7 % 3)
print(-6 % 3)
print(-7 % -3)
