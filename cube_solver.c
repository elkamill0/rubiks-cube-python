#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include "dfs_concept.h"

// Python wrapper for combinations()
static PyObject* py_combinations(PyObject* self, PyObject* args) {
    int depth;
    PyObject *start_obj, *final_obj;

    if (!PyArg_ParseTuple(args, "iOO", &depth, &start_obj, &final_obj)) {
        return NULL;
    }

    if (!PySequence_Check(start_obj) || !PySequence_Check(final_obj)) {
        PyErr_SetString(PyExc_TypeError, "start_state and final_state must be sequences");
        return NULL;
    }

    int start_state[4], final_state[4];
    for (int i = 0; i < 4; i++) {
        PyObject *item_start = PySequence_GetItem(start_obj, i);
        PyObject *item_final = PySequence_GetItem(final_obj, i);

        if (!PyLong_Check(item_start) || !PyLong_Check(item_final)) {
            Py_XDECREF(item_start);
            Py_XDECREF(item_final);
            PyErr_SetString(PyExc_TypeError, "states must contain integers");
            return NULL;
        }

        start_state[i] = (int)PyLong_AsLong(item_start);
        final_state[i] = (int)PyLong_AsLong(item_final);

        Py_DECREF(item_start);
        Py_DECREF(item_final);
    }

    // reset solutions
    solution_count = 0;
    combinations(depth, start_state, final_state);

    // create Python list of solutions
    PyObject *result_list = PyList_New(solution_count);
    for (int i = 0; i < solution_count; i++) {
        Solution *sol = &solutions[i];
        PyObject *move_list = PyList_New(sol->length);
        for (int j = 0; j < sol->length; j++) {
            PyList_SetItem(move_list, j, PyLong_FromLong(sol->moves[j]));
        }
        PyList_SetItem(result_list, i, move_list);
        free(sol->moves);
    }

    return result_list;
}

// methods table
static PyMethodDef CubeSolverMethods[] = {
    {"combinations", py_combinations, METH_VARARGS, "Find cube move combinations."},
    {NULL, NULL, 0, NULL}
};

// module definition
static struct PyModuleDef cubesolvermodule = {
    PyModuleDef_HEAD_INIT,
    "cube_solver",
    "Cube Solver Extension",
    -1,
    CubeSolverMethods
};

PyMODINIT_FUNC PyInit_cube_solver(void) {
    return PyModule_Create(&cubesolvermodule);
}
