#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct SearchCube {
    int* state;
    int path;
    struct SearchCube* parent;
    int depth;
} SearchCube;

bool equal_arrays(int a[], int b[]) {
    for (int i = 0; i < 4; i++){
        if (a[i] != b[i]){
            return false;
        }
    }
    return true;
}

// Tu powinieneś dodać swoje implementacje move_cube itp.
// Na potrzeby przykładu zrobimy prostą funkcję kopiującą stan:
int* copy_state(int source[4]){
    int* dest = malloc(sizeof(int)*4);
    for(int i=0; i<4; i++){
        dest[i] = source[i];
    }
    return dest;
}

SearchCube* createNode(int *state, int path, SearchCube* parent, int depth){
    SearchCube* cube = malloc(sizeof(SearchCube));
    cube->state = state;
    cube->path = path;
    cube->parent = parent;
    cube->depth = depth;
    return cube;
}

int* saveSolution(SearchCube* node){
    int* sol = malloc(sizeof(int) * (node->depth+1));
    sol[node->depth] = -1;
    SearchCube* current = node;
    while (current->parent != NULL){
        sol[current->depth-1] = current->path;
        current = current->parent;
    }
    sol[0] = current->path;
    return sol;
}

static PyObject* py_combinations(PyObject* self, PyObject* args){
    int depth;
    PyObject *start_state_obj;
    PyObject *final_state_obj;

    if (!PyArg_ParseTuple(args, "iOO", &depth, &start_state_obj, &final_state_obj)){
        return NULL;
    }

    // Sprawdzamy, czy mamy listy długości 4:
    if (!PyList_Check(start_state_obj) || PyList_Size(start_state_obj) != 4){
        PyErr_SetString(PyExc_ValueError, "start_state musi być listą długości 4");
        return NULL;
    }
    if (!PyList_Check(final_state_obj) || PyList_Size(final_state_obj) != 4){
        PyErr_SetString(PyExc_ValueError, "final_state musi być listą długości 4");
        return NULL;
    }

    int start_state[4], final_state[4];
    for (int i=0; i<4; i++){
        PyObject* item = PyList_GetItem(start_state_obj, i);
        start_state[i] = (int)PyLong_AsLong(item);
        item = PyList_GetItem(final_state_obj, i);
        final_state[i] = (int)PyLong_AsLong(item);
    }

    // Dla przykładu, stwórzmy jedno rozwiązanie:
    // Tworzymy węzeł o depth równym 'depth', path = 0
    int* state_copy = copy_state(start_state);
    SearchCube* root = createNode(state_copy, 0, NULL, depth);

    // Zapisujemy rozwiązanie (tu tylko jeden, przykładowy)
    int* solution_c = saveSolution(root);

    // Tworzymy obiekt listy Pythona dla rozwiązania:
    PyObject* solution_list = PyList_New(depth+1);
    for (int i=0; i<depth; i++){
        PyList_SetItem(solution_list, i, PyLong_FromLong(solution_c[i]));
    }
    PyList_SetItem(solution_list, depth, PyLong_FromLong(-1));

    free(solution_c);
    free(state_copy);
    free(root);

    // Wracamy listę rozwiązań (tutaj tylko jedna):
    PyObject* solutions = PyList_New(1);
    PyList_SetItem(solutions, 0, solution_list);

    return solutions;
}

static PyMethodDef CubeMovesMethods[] = {
    {"combinations", py_combinations, METH_VARARGS, "Compute cube move combinations."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef cubemovesmodule = {
    PyModuleDef_HEAD_INIT,
    "cubemoves",
    "Module for cube move calculations",
    -1,
    CubeMovesMethods
};

PyMODINIT_FUNC PyInit_cubemoves(void) {
    return PyModule_Create(&cubemovesmodule);
}
