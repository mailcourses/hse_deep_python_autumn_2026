
cpdef int fib_cyth_rec(int n):
    if n <= 2:
        return 1

    return fib_cyth_rec(n - 1) + fib_cyth_rec(n - 2)


def fib_cyth_iter(int n):
    a = 0
    b = 1
    cdef int i

    for i in range(n):
        a, b = b, a + b

    return a
