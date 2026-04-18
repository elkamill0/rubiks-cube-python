#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include "dfs_concept.h"

static PyObject* py_combinations(PyObject* self, PyObject* args) {
    int depth;
    PyObject* start_list;
    PyObject* final_list;

    if (!PyArg_ParseTuple(args, "iOO", &depth, &start_list, &final_list))
        return NULL;

    if (!PyList_Check(start_list) || !PyList_Check(final_list)) {
        PyErr_SetString(PyExc_TypeError, "start_state and final_state must be lists");
        return NULL;
    }

    int start_state[4];
    int final_state[4];
    for (int i = 0; i < 4; i++) {
        start_state[i] = (int)PyLong_AsLong(PyList_GetItem(start_list, i));
        final_state[i] = (int)PyLong_AsLong(PyList_GetItem(final_list, i));
    }

    int** solutions = combinations(depth, start_state, final_state);

    PyObject* py_solutions = PyList_New(0);
    for (int i = 0; solutions[i] != NULL; i++) {
        PyObject* py_sol = PyList_New(0);
        for (int j = 0; solutions[i][j] != -1; j++) {
            PyList_Append(py_sol, PyLong_FromLong(solutions[i][j]));
        }
        PyList_Append(py_solutions, py_sol);
    }

    // free_solutions(solutions);
    return py_solutions;
}

static PyMethodDef CubeSolverMethods[] = {
    {"combinations", py_combinations, METH_VARARGS, "Find cube move combinations"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef cube_solver_module = {
    PyModuleDef_HEAD_INIT,
    "cube",
    NULL,
    -1,
    CubeSolverMethods
};

PyMODINIT_FUNC PyInit_cube_solver(void) {
    return PyModule_Create(&cube_solver_module);
}
