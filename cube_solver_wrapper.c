#define PY_SSIZE_T_CLEAN
#include <Python.h>

// Deklaracja funkcji z dfs_concept.c
void combinations(int depth, int* start_state, int* final_state);

// Wrapper dla funkcji combinations
static PyObject* py_combinations(PyObject* self, PyObject* args) {
    int depth;
    PyObject *start_obj, *end_obj;

    if (!PyArg_ParseTuple(args, "iOO", &depth, &start_obj, &end_obj)) {
        return NULL;
    }

    if (!PyList_Check(start_obj) || !PyList_Check(end_obj)) {
        PyErr_SetString(PyExc_TypeError, "start_state and final_state must be lists");
        return NULL;
    }

    if (PyList_Size(start_obj) != 4 || PyList_Size(end_obj) != 4) {
        PyErr_SetString(PyExc_ValueError, "start_state and final_state must have 4 elements");
        return NULL;
    }

    int start[4], end[4];
    for (int i = 0; i < 4; i++) {
        start[i] = (int) PyLong_AsLong(PyList_GetItem(start_obj, i));
        end[i] = (int) PyLong_AsLong(PyList_GetItem(end_obj, i));
    }

    combinations(depth, start, end);

    Py_RETURN_NONE;
}

static PyMethodDef CubeSolverMethods[] = {
    {"combinations", py_combinations, METH_VARARGS, "Solve cube cross with limited depth"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef cubesolvermodule = {
    PyModuleDef_HEAD_INIT,
    "cube_solver",
    "Module for solving Rubik's Cube cross using DFS",
    -1,
    CubeSolverMethods
};

PyMODINIT_FUNC PyInit_cube_solver(void) {
    return PyModule_Create(&cubesolvermodule);
}
