#include </usr/include/python3.10/Python.h>
#include "moves.h"
#include <stdio.h>
#include "utils.c"
#include "combinations.c"


PyObject* lambda;
PyObject* result;

void print_combination(int* combination, int length) {
        for (int i = 0; i < length; ++i) {
            printf("%s", int_to_moves(combination[i]));
        }
        printf("\n");
    }

static PyObject* combinations(PyObject* self, PyObject* args){
    int length;
    PyObject* capsule;
    
    if (!PyArg_ParseTuple(args, "iO", &length, &capsule)) {
        return NULL;
    }
    int* cube = PyCapsule_GetPointer(capsule, "CubeArray");

    PyObject* py_list = combinations_c(cube, length);
    
    return py_list;

    // Py_RETURN_NONE;
}

static PyObject* print_cube_py(PyObject* self, PyObject* args){
    int* cube = decapsulation(self, args);
    print_cube(cube);
    Py_RETURN_NONE;
}

static PyObject* init(PyObject* self, PyObject* args){
    PyObject* list = NULL;
    if (!PyArg_ParseTuple(args, "|O", &list)){
        return NULL;
    }
    int* cube = memcpy(malloc(54 * sizeof(int)), (int[]){0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5}, 54 * sizeof(int));
    if (list != NULL) {     // set cube from user input scramble
        Py_ssize_t size = PyList_Size(list);   
        PyObject* item;
        for (Py_ssize_t i = 0; i < size; i++){
            item = PyList_GetItem(list, i);
            long value = PyLong_AsLong(item);
            input_scramble(cube, value);
        }
    }
    PyObject* capsule = PyCapsule_New((void*)cube, "CubeArray", cube_destructor);
    return capsule;
} 

static PyObject* sequence(PyObject* self, PyObject* args){
    PyObject* list;
    PyObject* capsule;
    
    if (!PyArg_ParseTuple(args, "OO", &list, &capsule)) {
        return NULL;
    }
    int* cube = PyCapsule_GetPointer(capsule, "CubeArray");
    Py_ssize_t size = PyList_Size(list);   
    PyObject* item;
    for (Py_ssize_t i = 0; i < size; i++){
        item = PyList_GetItem(list, i);
        long value = PyLong_AsLong(item);
        input_scramble(cube, value);
    }
    Py_RETURN_NONE;
}

static PyObject* f2l(PyObject* self, PyObject* args){
    
}



static PyMethodDef ScrambleMethods[] = {
    {"combinations", combinations, METH_VARARGS, "show combinations"},
    {"print_cube_py", print_cube_py, METH_VARARGS, "map numbers to moves"},
    {"init", init, METH_VARARGS, "initialize cube"},
    {"sequence", sequence, METH_VARARGS, "input moves and do it"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef scramblemodule = {
    PyModuleDef_HEAD_INIT,
    "scramble",
    NULL,
    -1,
    ScrambleMethods
};

PyMODINIT_FUNC PyInit_scramble(void) {
    return PyModule_Create(&scramblemodule);
}