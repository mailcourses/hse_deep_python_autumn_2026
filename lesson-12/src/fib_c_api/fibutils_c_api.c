#define PY_SSIZE_T_CLEAN
#include <Python.h>


int fib_c_rec_impl(int n)
{
    if (n <= 2)
        return 1;

    return fib_c_rec_impl(n - 1) + fib_c_rec_impl(n - 2);
}


int fib_c_iter_impl(int n)
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


static PyObject* fib_capi_rec(PyObject *self, PyObject *args)
{
    int n;

    if (!PyArg_ParseTuple(args, "i", &n))
        return NULL;

    if (n < 1)
    {
        PyErr_SetString(PyExc_ValueError, "n must be positive int");
        return NULL;
    }

    int res = fib_c_rec_impl(n);
    return PyLong_FromLong(res);
}


static PyObject* fib_capi_iter(PyObject *self, PyObject *args)
{
    int n;

    if (!PyArg_ParseTuple(args, "i", &n))
        return NULL;

    if (n < 1)
    {
        PyErr_SetString(PyExc_ValueError, "n must be positive int");
        return NULL;
    }

    int res = fib_c_iter_impl(n);
    return PyLong_FromLong(res);
}


static PyObject* fib_capi_iter_long(PyObject *self, PyObject *args)
{
    int n;

    if (!PyArg_ParseTuple(args, "i", &n))
        return NULL;

    if (n < 1)
    {
        PyErr_SetString(PyExc_ValueError, "n must be positive int");
        return NULL;
    }

    PyObject *a = PyLong_FromLong(0);
    if (!a)
        return NULL;

    PyObject *b = PyLong_FromLong(1);
    if (!b)
    {
        Py_DECREF(a);
        return NULL;
    }

    for (int i = 0; i < n; ++i)
    {
        PyObject *s = PyNumber_Add(a, b);
        if (!s)
        {
            Py_DECREF(a);
            Py_DECREF(b);
            return NULL;
        }

        Py_DECREF(a);
        a = b;
        b = s;
    }

    Py_DECREF(b);

    return a;
}


static PyMethodDef methods[] = {
    {"fib_capi_iter", fib_capi_iter, METH_VARARGS, "n-th fib number iter"},
    {"fib_capi_rec", fib_capi_rec, METH_VARARGS, "n-th fib number rec"},
    {"fib_capi_iter_long", fib_capi_iter_long, METH_VARARGS, "n-th fib number iter long"},
    {NULL, NULL, 0, NULL},
};


static struct PyModuleDef module_fibutils_capi = {
    PyModuleDef_HEAD_INIT, "fibutils_capi", NULL, -1, methods
};


PyMODINIT_FUNC PyInit_fibutils_capi()
{
    return PyModule_Create( &module_fibutils_capi );
}
