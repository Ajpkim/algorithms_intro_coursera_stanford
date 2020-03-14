import math


def kuratsuba(a, b):
    """
    takes two integers, a and b, and returns the product
    """
    # base case
    if a < 10 and b < 10:
        return a * b

    # recursive case
    else:
        n = max(len(str(a)), len(str(b)))
        m = math.ceil(float(n)/2)

        a1 = a // (10**m)
        a2 = a % (10**m)

        b1 = b // (10**m)
        b2 = b % (10**m)

        s1 = kuratsuba(a1, b1)
        s2 = kuratsuba(a2, b2)
        s3 = kuratsuba((a1 + a2), (b1 + b2))
        s4 = s3 - s2 - s1

        return ((s1*(10**(m*2))) + (s4*(10**m)) + (s2))


# TESTING
# Assignment givens
a = 3141592653589793238462643383279502884197169399375105820974944592
b = 2718281828459045235360287471352662497757247093699959574966967627

print("test:", ((a*b) == (kuratsuba(a, b))))
print("a={}, b={}".format(a, b))
print("expected:", (a*b))
print("result:", kuratsuba(a, b))
