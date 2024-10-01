#include <stdio.h>
#include <stdbool.h>
#include </usr/include/python3.10/Python.h>
#include "moves.h"
#include "combinations.c"
#include "utils.c"

static PyObject* init(PyObject* self, PyObject* args){
    PyObject* list = NULL;
    if (!PyArg_ParseTuple(args, "|O", &list)){
        return NULL;
    }

    struct element* cube = (struct element*)malloc(26 * sizeof(struct element)); // odd-edges; even-corners,centers
    struct element* cube_copy = (struct element*)malloc(26 * sizeof(struct element));

    if (!cube || !cube_copy) {
        free(cube);
        free(cube_copy);
        return PyErr_NoMemory();  // Handle allocation failure
    }

    for (int i = 0; i < 26; ++i){
        cube[i].index = i;
        cube[i].orientation = 1;
        cube_copy[i].index = i;
        cube_copy[i].orientation = 1;
    }
    cube[17].index = 17; //another odd edges
    cube[19].index = 19;
    cube[21].index = 21;
    cube[23].index = 23;
    cube[16].index = 0; // centers
    cube[18].index = 1;
    cube[20].index = 2;
    cube[22].index = 3;
    cube[24].index = 4;
    cube[25].index = 5;
    cube_copy[17].index = 17; //another odd edges
    cube_copy[19].index = 19;
    cube_copy[21].index = 21;
    cube_copy[23].index = 23;
    cube_copy[16].index = 0; // centers
    cube_copy[18].index = 1;
    cube_copy[20].index = 2;
    cube_copy[22].index = 3;
    cube_copy[24].index = 4;
    cube_copy[25].index = 5;


    if (list != NULL) {     // set cube from user input scramble
        Py_ssize_t size = PyList_Size(list);   
        PyObject* item;
        for (Py_ssize_t i = 0; i < size; i++){
            item = PyList_GetItem(list, i);
            long value = PyLong_AsLong(item);
            input_scramble(cube, value);
        }
    }
    PyObject* capsule  = PyCapsule_New((void*)cube, "CubeArray", cube_destructor);
    PyObject* capsule2 = PyCapsule_New((void*)cube_copy, "CubeArrayCopy", cube_copy_destructor);

    if (!capsule || !capsule2) {
        if (cube) free(cube);
        if (cube_copy) free(cube_copy);
        Py_XDECREF(capsule);
        Py_XDECREF(capsule2);
        return PyErr_NoMemory();  // Return appropriate error
    }

    // Print pointers for debugging (fixed format specifier)
    // printf("cube_copy pointer: %p\n", (void*)cube_copy);
    // printf("cube pointer: %p\n", (void*)cube);

    PyObject* py_list = PyList_New(2);
    PyList_SET_ITEM(py_list, 0, capsule);
    PyList_SET_ITEM(py_list, 1, capsule2);
    return py_list;
}

static PyObject* print_cube_py(PyObject* self, PyObject* args){
    struct element* cube = decapsulation(self, args, "CubeArray");
    print_cube(cube);
    Py_RETURN_NONE;
}

static PyObject* combinations(PyObject* self, PyObject* args){
    int length;
    
    PyObject* capsule;
    PyObject* capsule2;

    if (!PyArg_ParseTuple(args, "iOO", &length, &capsule, &capsule2)) {
        return NULL;
    }
    
    struct element* cube = PyCapsule_GetPointer(capsule, "CubeArray");
    struct element* cube_copy = PyCapsule_GetPointer(capsule2, "CubeArrayCopy");


    PyObject* py_list = combinations_c(cube, cube_copy, length);
    return py_list;
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


static PyMethodDef CubeUpgradeMethods[] = {
    {"combinations", combinations, METH_VARARGS, "show combinations"},
    {"init", init, METH_VARARGS, "initialize cube"},
    {"print_cube", print_cube_py, METH_VARARGS, "show cube visualisation as number notation"},
    {"sequence", sequence, METH_VARARGS, "input moves and do it"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef cubeupgrade = {
    PyModuleDef_HEAD_INIT,
    "cube-upgrade",
    NULL,
    -1,
    CubeUpgradeMethods
};

PyMODINIT_FUNC PyInit_cube_upgrade(void) {
    return PyModule_Create(&cubeupgrade);
}



int main(){

    // for (int i = 0; i < 20; ++i){
    //     cube[i].index = i;
    //     cube[i].orientation = 1;
    //     printf("%d %d\n", cube[i].index, cube[i].orientation);
    // }
    // printf("%d", check_cross(cube));
    
    return 0;
}