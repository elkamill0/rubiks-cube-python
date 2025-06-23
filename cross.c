#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <numpy/arrayobject.h>

static PyObject* inspect_cube(PyObject* self, PyObject* args) {
    PyObject *cube_obj;

    if (!PyArg_ParseTuple(args, "O", &cube_obj)) {
        return NULL;
    }

    PyObject *corners = PyObject_GetAttrString(cube_obj, "corners");
    PyObject *edges = PyObject_GetAttrString(cube_obj, "edges");
    PyObject *centers = PyObject_GetAttrString(cube_obj, "centers");

    if (!corners || !edges || !centers) {
        PyErr_SetString(PyExc_AttributeError, "Cube object missing corners, edges or centers.");
        return NULL;
    }

    PyArrayObject *arr_corners = (PyArrayObject *)PyArray_FROM_OTF(corners, NPY_INT8, NPY_ARRAY_IN_ARRAY);
    PyArrayObject *arr_edges = (PyArrayObject *)PyArray_FROM_OTF(edges, NPY_INT8, NPY_ARRAY_IN_ARRAY);
    PyArrayObject *arr_centers = (PyArrayObject *)PyArray_FROM_OTF(centers, NPY_UINT8, NPY_ARRAY_IN_ARRAY);

    Py_DECREF(corners);
    Py_DECREF(edges);
    Py_DECREF(centers);

    if (!arr_corners || !arr_edges || !arr_centers) {
        Py_XDECREF(arr_corners);
        Py_XDECREF(arr_edges);
        Py_XDECREF(arr_centers);
        PyErr_SetString(PyExc_TypeError, "Conversion to NumPy array failed.");
        return NULL;
    }

    printf("Corners:\n");
    for (int i = 0; i < 8; i++) {
        npy_int8 a = *(npy_int8 *)PyArray_GETPTR2(arr_corners, i, 0);
        npy_int8 b = *(npy_int8 *)PyArray_GETPTR2(arr_corners, i, 1);
        printf("  [%d, %d]\n", a, b);
    }

    printf("Edges:\n");
    for (int i = 0; i < 12; i++) {
        npy_int8 a = *(npy_int8 *)PyArray_GETPTR2(arr_edges, i, 0);
        npy_int8 b = *(npy_int8 *)PyArray_GETPTR2(arr_edges, i, 1);
        printf("  [%d, %d]\n", a, b);
    }

    printf("Centers:\n");
    for (int i = 0; i < 6; i++) {
        npy_uint8 val = *(npy_uint8 *)PyArray_GETPTR1(arr_centers, i);
        printf("  %d\n", val);
    }

    Py_DECREF(arr_corners);
    Py_DECREF(arr_edges);
    Py_DECREF(arr_centers);

    Py_RETURN_NONE;
}

static PyMethodDef Methods[] = {
    {"inspect_cube", inspect_cube, METH_VARARGS, "Print cube data from Python object"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef cross_c = {
    PyModuleDef_HEAD_INIT,
    "cross_c",
    "Module for inspecting Cube objects",
    -1,
    Methods
};

PyMODINIT_FUNC PyInit_cross_c(void) {
    import_array();
    return PyModule_Create(&cross_c);
}
