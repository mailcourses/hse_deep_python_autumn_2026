
def fib_native_rec(n: int) -> int:
    if n <= 2:
        return 1

    return fib_native_rec(n - 1) + fib_native_rec(n - 2)


def fib_native_iter(n: int) -> int:
    a, b = 0, 1

    for i in range(n):
        a, b = b, a + b

    return a


if __name__ == "__main__":
    for i in range(1, 11):
        print(f"{fib_native_rec(i)=}, {fib_native_iter(i)=}")
