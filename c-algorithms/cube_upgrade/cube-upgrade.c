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

    for (int i = 0; i < 26; ++i){
        cube[i].index = i;
        cube[i].orientation = 1;
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

static PyObject* print_cube_py(PyObject* self, PyObject* args){
    struct element* cube = decapsulation(self, args);
    print_cube(cube);
    Py_RETURN_NONE;
}

static PyObject* combinations(PyObject* self, PyObject* args){
    int length;
    
    PyObject* capsule;

    if (!PyArg_ParseTuple(args, "iO", &length, &capsule)) {
        return NULL;
    }
    
    struct element* cube = PyCapsule_GetPointer(capsule, "CubeArray");
    PyObject* py_list = combinations_c(cube, length);
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