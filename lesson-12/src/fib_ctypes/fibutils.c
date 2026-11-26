int fib_c_rec(int n)
{
    if (n <= 2)
        return 1;

    return fib_c_rec(n - 1) + fib_c_rec(n - 2);
}


int fib_c_iter(int n)
{
    int a = 0, b = 1;

    for (int i = 0; i < n; ++i)
    {
        int tmp = a;
        a = b;
        b = b + tmp;
    }

    return a;
}
