import bisect


def isPossible(A):
    if all(a == 1 for a in A):
        return True
    total = sum(A)
    A.sort()
    while True:
        a = A.pop()
        if a == 1:
            return True
        total -= a
        a -= total
        total += a
        if a < 0:
            return False
        bisect.insort(A, a)


print(isPossible([1, 1,  2]))
