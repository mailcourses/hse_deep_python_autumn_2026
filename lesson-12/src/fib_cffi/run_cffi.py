import cffi


def run_fib():
    ffi = cffi.FFI()
    lib = ffi.dlopen("../fib_ctypes/libfibutils.so")

    ffi.cdef("int fib_c_rec(int n);")

    res = lib.fib_c_rec(41);
    print(f"{res=}")


def run_compile():
    ffi = cffi.FFI()

    ffi.cdef("int mult(int a, int b, int c);")

    ffi.set_source(
        "libarithm",
        """
        int mult(int a, int b, int c)
        {
            return a * b * c;
        }
        """
    )
    ffi.compile()


def run_import():
    import libarithm

    print(f"{libarithm.lib.mult(3, 4, 5)=}")


if __name__ == "__main__":
    run_fib()

    run_compile()
    run_import()

