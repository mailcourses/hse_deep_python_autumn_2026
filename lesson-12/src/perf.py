import ctypes
import time

import cffi

from fib_py_native import fib_native_rec, fib_native_iter
from fibutils_capi import fib_capi_rec, fib_capi_iter, fib_capi_iter_long
from fibutils_cy import fib_cyth_rec, fib_cyth_iter


def run_fib_native(n_rec, n_iter):
    t1 = time.time()
    res_rec = fib_native_rec(n_rec)
    t2 = time.time()

    t3 = time.time()
    res_iter = fib_native_iter(n_iter)
    t4 = time.time()

    t5 = time.time()
    res_iter_long = fib_native_iter(n_iter * 20000)
    t6 = time.time()

    print(f"[python-rec]  {res_rec=} time={t2 - t1}")
    print(f"[python-iter] {res_iter=} time={t4 - t3}")
    print(f"[python-iter-long] time={t6 - t5}")


def run_fib_ctypes(n_rec, n_iter):
    libfib = ctypes.CDLL("./fib_ctypes/libfibutils.so")

    libfib.fib_c_rec.argtypes = (ctypes.c_int,)
    libfib.fib_c_rec.restype = ctypes.c_int

    libfib.fib_c_iter.argtypes = (ctypes.c_int,)
    libfib.fib_c_iter.restype = ctypes.c_int

    t1 = time.time()
    res_rec = libfib.fib_c_rec(n_rec)
    t2 = time.time()

    t3 = time.time()
    res_iter = libfib.fib_c_iter(n_iter)
    t4 = time.time()

    print(f"[ctypes-rec]  {res_rec=} time={t2 - t1}")
    print(f"[ctypes-iter] {res_iter=} time={t4 - t3}")


def run_fib_cffi(n_rec, n_iter):
    ffi = cffi.FFI()
    lib = ffi.dlopen("./fib_ctypes/libfibutils.so")

    ffi.cdef("int fib_c_rec(int n);")
    ffi.cdef("int fib_c_iter(int n);")

    t1 = time.time()
    res_rec = lib.fib_c_rec(n_rec)
    t2 = time.time()

    t3 = time.time()
    res_iter = lib.fib_c_iter(n_iter)
    t4 = time.time()

    print(f"[cffi-rec]  {res_rec=} time={t2 - t1}")
    print(f"[cffi-iter] {res_iter=} time={t4 - t3}")


def run_fib_c_api(n_rec, n_iter):
    t1 = time.time()
    res_rec = fib_capi_rec(n_rec)
    t2 = time.time()

    t3 = time.time()
    res_iter = fib_capi_iter(n_iter)
    t4 = time.time()

    t5 = time.time()
    res_iter_long = fib_capi_iter_long(n_iter * 20000)
    t6 = time.time()

    print(f"[c-api-rec]  {res_rec=} time={t2 - t1}")
    print(f"[c-api-iter] {res_iter=} time={t4 - t3}")
    print(f"[c-api-iter-long] time={t6 - t5}")


def run_fib_cython(n_rec, n_iter):
    t1 = time.time()
    res_rec = fib_cyth_rec(n_rec)
    t2 = time.time()

    t3 = time.time()
    res_iter = fib_cyth_iter(n_iter)
    t4 = time.time()

    t5 = time.time()
    res_iter_long = fib_cyth_iter(n_iter * 20000)
    t6 = time.time()

    print(f"[cython-rec]  {res_rec=} time={t2 - t1}")
    print(f"[cython-iter] {res_iter=} time={t4 - t3}")
    print(f"[cython-iter-long] time={t6 - t5}")


def run():
    n_rec = 41
    n_iter = 40

    run_fib_native(n_rec, n_iter)
    print("------\n")

    run_fib_ctypes(n_rec, n_iter)
    print("------\n")

    run_fib_cffi(n_rec, n_iter)
    print("------\n")

    run_fib_c_api(n_rec, n_iter)
    print("------\n")

    run_fib_cython(n_rec, n_iter)
    print("------\n")

    nat_iter = fib_native_iter(n_iter * 20000)
    cyth_iter = fib_cyth_iter(n_iter * 20000)
    capi_iter = fib_capi_iter_long(n_iter * 20000)
    print(nat_iter == cyth_iter == capi_iter)


if __name__ == "__main__":
    run()
