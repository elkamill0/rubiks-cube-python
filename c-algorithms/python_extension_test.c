#include </usr/include/python3.10/Python.h>
#include <stdio.h>


struct element* decapsulation(PyObject* self, PyObject* args){
    PyObject* capsule;
    
    if (!PyArg_ParseTuple(args, "O", &capsule)) {
        return NULL;
    }
    return (struct element*)PyCapsule_GetPointer(capsule, "CubeArray");
}
struct element* decapsulation_two_cubes(PyObject* self, PyObject* args){
    PyObject* capsule;
    PyObject* capsule2;
    struct element** result;
    if (!PyArg_ParseTuple(args, "OO", &capsule, &capsule2)) {
        return NULL;
    }
    struct element* cube = PyCapsule_GetPointer(capsule, "CubeArray");
    struct element* cube_copy = PyCapsule_GetPointer(capsule2, "CubeArrayCopy");
    
}

static PyObject* x_move_export(PyObject* self, PyObject* args){
    struct element* cube = decapsulation(self, args, "CubeArray");
    struct element* cube_copy = decapsulation(self, args, "CubeArrayCopy");
    x(cube, cube_copy);
    Py_RETURN_NONE;
}
