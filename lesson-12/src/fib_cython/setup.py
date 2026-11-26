from setuptools import setup
from Cython.Build import cythonize


setup(
    name="fibcyth_custom",
    version="7.5.2",
    ext_modules=cythonize(["fibutils_cy.pyx"]),
)
