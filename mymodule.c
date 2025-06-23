#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <numpy/arrayobject.h>

// Funkcja mnożąca każdy element przez 2
static PyObject* double_array(PyObject* self, PyObject* args) {
    PyArrayObject *input_array;

    // Parsowanie argumentu: jedna tablica NumPy
    if (!PyArg_ParseTuple(args, "O!", &PyArray_Type, &input_array)) {
        return NULL;
    }

    // Upewniamy się, że to tablica 1D typu float64
    if (PyArray_NDIM(input_array) != 1 || PyArray_TYPE(input_array) != NPY_DOUBLE) {
        PyErr_SetString(PyExc_TypeError, "Expected a 1D NumPy array of float64");
        return NULL;
    }

    npy_intp size = PyArray_SIZE(input_array);
    double *data = (double *)PyArray_DATA(input_array);

    // Tworzymy nową tablicę do zwrócenia
    PyArrayObject *result = (PyArrayObject *)PyArray_SimpleNew(1, &size, NPY_DOUBLE);
    if (!result) return NULL;

    double *result_data = (double *)PyArray_DATA(result);

    for (npy_intp i = 0; i < size; ++i) {
        result_data[i] = data[i] * 2.0;
    }

    return (PyObject *)result;
}

static PyMethodDef Methods[] = {
    {"double_array", double_array, METH_VARARGS, "Double each element in a NumPy array"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef mymodule = {
    PyModuleDef_HEAD_INIT,
    "mymodule",
    "Example NumPy C extension",
    -1,
    Methods
};

PyMODINIT_FUNC PyInit_mymodule(void) {
    import_array();  // bardzo ważne!
    return PyModule_Create(&mymodule);
}
