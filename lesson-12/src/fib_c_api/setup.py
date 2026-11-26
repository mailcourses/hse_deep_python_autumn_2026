from setuptools import setup, Extension


setup(
    name="fibutils_custom",
    version="9.5.1",
    ext_modules=[Extension("fibutils_capi", ["fibutils_c_api.c"]),]
)
