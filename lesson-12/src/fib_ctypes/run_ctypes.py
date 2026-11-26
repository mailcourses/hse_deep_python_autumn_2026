import ctypes


def run_ctypes():
   libc = ctypes.CDLL(None)

   libc.strstr.argtypes = (ctypes.c_char_p, ctypes.c_char_p)
   libc.strstr.restype = ctypes.c_char_p

   print(f"{libc.strstr(b'qwerty', b'qw')=}")
   print(f"{libc.strstr(b'qwerty', b'y')=}")
   print(f"{libc.strstr(b'qwerty', b'er')=}")
   print(f"{libc.strstr(b'qwerty', b'123')=}")


if __name__ == "__main__":
    run_ctypes()
