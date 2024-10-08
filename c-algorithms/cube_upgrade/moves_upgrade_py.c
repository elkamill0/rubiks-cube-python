#include </usr/include/python3.10/Python.h>
#include "moves.h"
#include "utils.c"

static PyObject* R_move_export(PyObject* self, PyObject* args){
    struct element* cube = decapsulation(self, args, "CubeArray");
    R(cube);
    Py_RETURN_NONE;
}

static PyObject* R2_move_export(PyObject* self, PyObject* args){
    struct element* cube = decapsulation(self, args, "CubeArray");
    R2(cube);
    Py_RETURN_NONE;
}

static PyObject* Rp_move_export(PyObject* self, PyObject* args){
    struct element* cube = decapsulation(self, args, "CubeArray");
    Rp(cube);
    Py_RETURN_NONE;
}

static PyObject* L_move_export(PyObject* self, PyObject* args){
    struct element* cube = decapsulation(self, args, "CubeArray");
    L(cube);
    Py_RETURN_NONE;
}

static PyObject* L2_move_export(PyObject* self, PyObject* args){
    struct element* cube = decapsulation(self, args, "CubeArray");
    L2(cube);
    Py_RETURN_NONE;
}

static PyObject* Lp_move_export(PyObject* self, PyObject* args){
    struct element* cube = decapsulation(self, args, "CubeArray");
    Lp(cube);
    Py_RETURN_NONE;
}

static PyObject* U_move_export(PyObject* self, PyObject* args){
    struct element* cube = decapsulation(self, args, "CubeArray");
    U(cube);
    Py_RETURN_NONE;
}

static PyObject* U2_move_export(PyObject* self, PyObject* args){
    struct element* cube = decapsulation(self, args, "CubeArray");
    U2(cube);
    Py_RETURN_NONE;
}

static PyObject* Up_move_export(PyObject* self, PyObject* args){
    struct element* cube = decapsulation(self, args, "CubeArray");
    Up(cube);
    Py_RETURN_NONE;
}

static PyObject* D_move_export(PyObject* self, PyObject* args){
    struct element* cube = decapsulation(self, args, "CubeArray");
    D(cube);
    Py_RETURN_NONE;
}

static PyObject* D2_move_export(PyObject* self, PyObject* args){
    struct element* cube = decapsulation(self, args, "CubeArray");
    D2(cube);
    Py_RETURN_NONE;
}

static PyObject* Dp_move_export(PyObject* self, PyObject* args){
    struct element* cube = decapsulation(self, args, "CubeArray");
    Dp(cube);
    Py_RETURN_NONE;
}

static PyObject* F_move_export(PyObject* self, PyObject* args){
    struct element* cube = decapsulation(self, args, "CubeArray");
    F(cube);
    Py_RETURN_NONE;
}

static PyObject* F2_move_export(PyObject* self, PyObject* args){
    struct element* cube = decapsulation(self, args, "CubeArray");
    F2(cube);
    Py_RETURN_NONE;
}

static PyObject* Fp_move_export(PyObject* self, PyObject* args){
    struct element* cube = decapsulation(self, args, "CubeArray");
    Fp(cube);
    Py_RETURN_NONE;
}

static PyObject* B_move_export(PyObject* self, PyObject* args){
    struct element* cube = decapsulation(self, args, "CubeArray");
    B(cube);
    Py_RETURN_NONE;
}

static PyObject* B2_move_export(PyObject* self, PyObject* args){
    struct element* cube = decapsulation(self, args, "CubeArray");
    B2(cube);
    Py_RETURN_NONE;
}

static PyObject* Bp_move_export(PyObject* self, PyObject* args){
    struct element* cube = decapsulation(self, args, "CubeArray");
    Bp(cube);
    Py_RETURN_NONE;
}

static PyObject* M_move_export(PyObject* self, PyObject* args){
    PyObject* capsule;
    PyObject* capsule2;
    if (!PyArg_ParseTuple(args, "OO", &capsule, &capsule2)) {
        return NULL;
    }
    struct element* cube = PyCapsule_GetPointer(capsule, "CubeArray");
    struct element* cube_copy = PyCapsule_GetPointer(capsule2, "CubeArrayCopy");
    M(cube, cube_copy);
    Py_RETURN_NONE;
}

static PyObject* Mp_move_export(PyObject* self, PyObject* args){
    PyObject* capsule;
    PyObject* capsule2;
    if (!PyArg_ParseTuple(args, "OO", &capsule, &capsule2)) {
        return NULL;
    }
    struct element* cube = PyCapsule_GetPointer(capsule, "CubeArray");
    struct element* cube_copy = PyCapsule_GetPointer(capsule2, "CubeArrayCopy");
    Mp(cube, cube_copy);
    Py_RETURN_NONE;
}

static PyObject* M2_move_export(PyObject* self, PyObject* args){
    PyObject* capsule;
    PyObject* capsule2;
    if (!PyArg_ParseTuple(args, "OO", &capsule, &capsule2)) {
        return NULL;
    }
    struct element* cube = PyCapsule_GetPointer(capsule, "CubeArray");
    struct element* cube_copy = PyCapsule_GetPointer(capsule2, "CubeArrayCopy");
    M2(cube, cube_copy);
    Py_RETURN_NONE;
}

static PyObject* E_move_export(PyObject* self, PyObject* args){
    PyObject* capsule;
    PyObject* capsule2;
    if (!PyArg_ParseTuple(args, "OO", &capsule, &capsule2)) {
        return NULL;
    }
    struct element* cube = PyCapsule_GetPointer(capsule, "CubeArray");
    struct element* cube_copy = PyCapsule_GetPointer(capsule2, "CubeArrayCopy");
    E(cube, cube_copy);
    Py_RETURN_NONE;
}

static PyObject* Ep_move_export(PyObject* self, PyObject* args){
    PyObject* capsule;
    PyObject* capsule2;
    if (!PyArg_ParseTuple(args, "OO", &capsule, &capsule2)) {
        return NULL;
    }
    struct element* cube = PyCapsule_GetPointer(capsule, "CubeArray");
    struct element* cube_copy = PyCapsule_GetPointer(capsule2, "CubeArrayCopy");
    Ep(cube, cube_copy);
    Py_RETURN_NONE;
}

static PyObject* E2_move_export(PyObject* self, PyObject* args){
    PyObject* capsule;
    PyObject* capsule2;
    if (!PyArg_ParseTuple(args, "OO", &capsule, &capsule2)) {
        return NULL;
    }
    struct element* cube = PyCapsule_GetPointer(capsule, "CubeArray");
    struct element* cube_copy = PyCapsule_GetPointer(capsule2, "CubeArrayCopy");
    E2(cube, cube_copy);
    Py_RETURN_NONE;
}

static PyObject* S_move_export(PyObject* self, PyObject* args){
    PyObject* capsule;
    PyObject* capsule2;
    if (!PyArg_ParseTuple(args, "OO", &capsule, &capsule2)) {
        return NULL;
    }
    struct element* cube = PyCapsule_GetPointer(capsule, "CubeArray");
    struct element* cube_copy = PyCapsule_GetPointer(capsule2, "CubeArrayCopy");
    S(cube, cube_copy);
    Py_RETURN_NONE;
}

static PyObject* Sp_move_export(PyObject* self, PyObject* args){
    PyObject* capsule;
    PyObject* capsule2;
    if (!PyArg_ParseTuple(args, "OO", &capsule, &capsule2)) {
        return NULL;
    }
    struct element* cube = PyCapsule_GetPointer(capsule, "CubeArray");
    struct element* cube_copy = PyCapsule_GetPointer(capsule2, "CubeArrayCopy");
    Sp(cube, cube_copy);
    Py_RETURN_NONE;
}

static PyObject* S2_move_export(PyObject* self, PyObject* args){
    PyObject* capsule;
    PyObject* capsule2;
    if (!PyArg_ParseTuple(args, "OO", &capsule, &capsule2)) {
        return NULL;
    }
    struct element* cube = PyCapsule_GetPointer(capsule, "CubeArray");
    struct element* cube_copy = PyCapsule_GetPointer(capsule2, "CubeArrayCopy");
    S2(cube, cube_copy);
    Py_RETURN_NONE;
}

static PyObject* x_move_export(PyObject* self, PyObject* args){
    PyObject* capsule;
    PyObject* capsule2;
    if (!PyArg_ParseTuple(args, "OO", &capsule, &capsule2)) {
        return NULL;
    }
    struct element* cube = PyCapsule_GetPointer(capsule, "CubeArray");
    struct element* cube_copy = PyCapsule_GetPointer(capsule2, "CubeArrayCopy");
    x(cube, cube_copy);
    Py_RETURN_NONE;
}

static PyObject* xp_move_export(PyObject* self, PyObject* args){
    PyObject* capsule;
    PyObject* capsule2;
    if (!PyArg_ParseTuple(args, "OO", &capsule, &capsule2)) {
        return NULL;
    }
    struct element* cube = PyCapsule_GetPointer(capsule, "CubeArray");
    struct element* cube_copy = PyCapsule_GetPointer(capsule2, "CubeArrayCopy");
    xp(cube, cube_copy);
    Py_RETURN_NONE;
}

static PyObject* x2_move_export(PyObject* self, PyObject* args){
    PyObject* capsule;
    PyObject* capsule2;
    if (!PyArg_ParseTuple(args, "OO", &capsule, &capsule2)) {
        return NULL;
    }
    struct element* cube = PyCapsule_GetPointer(capsule, "CubeArray");
    struct element* cube_copy = PyCapsule_GetPointer(capsule2, "CubeArrayCopy");
    x2(cube, cube_copy);
    Py_RETURN_NONE;
}

static PyObject* y_move_export(PyObject* self, PyObject* args){
    PyObject* capsule;
    PyObject* capsule2;
    if (!PyArg_ParseTuple(args, "OO", &capsule, &capsule2)) {
        return NULL;
    }
    struct element* cube = PyCapsule_GetPointer(capsule, "CubeArray");
    struct element* cube_copy = PyCapsule_GetPointer(capsule2, "CubeArrayCopy");
    y(cube, cube_copy);
    Py_RETURN_NONE;
}

static PyObject* yp_move_export(PyObject* self, PyObject* args){
    PyObject* capsule;
    PyObject* capsule2;
    if (!PyArg_ParseTuple(args, "OO", &capsule, &capsule2)) {
        return NULL;
    }
    struct element* cube = PyCapsule_GetPointer(capsule, "CubeArray");
    struct element* cube_copy = PyCapsule_GetPointer(capsule2, "CubeArrayCopy");
    yp(cube, cube_copy);
    Py_RETURN_NONE;
}

static PyObject* y2_move_export(PyObject* self, PyObject* args){
    PyObject* capsule;
    PyObject* capsule2;
    if (!PyArg_ParseTuple(args, "OO", &capsule, &capsule2)) {
        return NULL;
    }
    struct element* cube = PyCapsule_GetPointer(capsule, "CubeArray");
    struct element* cube_copy = PyCapsule_GetPointer(capsule2, "CubeArrayCopy");
    y2(cube, cube_copy);
    Py_RETURN_NONE;
}

static PyObject* z_move_export(PyObject* self, PyObject* args){
    PyObject* capsule;
    PyObject* capsule2;
    if (!PyArg_ParseTuple(args, "OO", &capsule, &capsule2)) {
        return NULL;
    }
    struct element* cube = PyCapsule_GetPointer(capsule, "CubeArray");
    struct element* cube_copy = PyCapsule_GetPointer(capsule2, "CubeArrayCopy");
    z(cube, cube_copy);
    Py_RETURN_NONE;
}

static PyObject* zp_move_export(PyObject* self, PyObject* args){
    PyObject* capsule;
    PyObject* capsule2;
    if (!PyArg_ParseTuple(args, "OO", &capsule, &capsule2)) {
        return NULL;
    }
    struct element* cube = PyCapsule_GetPointer(capsule, "CubeArray");
    struct element* cube_copy = PyCapsule_GetPointer(capsule2, "CubeArrayCopy");
    zp(cube, cube_copy);
    Py_RETURN_NONE;
}

static PyObject* z2_move_export(PyObject* self, PyObject* args){
    PyObject* capsule;
    PyObject* capsule2;
    if (!PyArg_ParseTuple(args, "OO", &capsule, &capsule2)) {
        return NULL;
    }
    struct element* cube = PyCapsule_GetPointer(capsule, "CubeArray");
    struct element* cube_copy = PyCapsule_GetPointer(capsule2, "CubeArrayCopy");
    z2(cube, cube_copy);
    Py_RETURN_NONE;
}



static PyMethodDef MovesMethods[] = {
    {"R",  R_move_export, METH_VARARGS, "R move"},
    {"R2", R2_move_export, METH_VARARGS, "R2 move"},
    {"Rp", Rp_move_export, METH_VARARGS, "Rp move"},
    {"L",  L_move_export, METH_VARARGS,  "L move"},
    {"L2", L2_move_export, METH_VARARGS, "L2 move"},
    {"Lp", Lp_move_export, METH_VARARGS, "Lp move"},
    {"U",  U_move_export, METH_VARARGS,  "U move"},
    {"U2", U2_move_export, METH_VARARGS, "U2 move"},
    {"Up", Up_move_export, METH_VARARGS, "Up move"},
    {"D",  D_move_export, METH_VARARGS,  "D move"},
    {"D2", D2_move_export, METH_VARARGS, "D2 move"},
    {"Dp", Dp_move_export, METH_VARARGS, "Dp move"},
    {"F",  F_move_export, METH_VARARGS,  "F move"},
    {"F2", F2_move_export, METH_VARARGS, "F2 move"},
    {"Fp", Fp_move_export, METH_VARARGS, "Fp move"},
    {"B",  B_move_export, METH_VARARGS,  "B move"},
    {"B2", B2_move_export, METH_VARARGS, "B2 move"},
    {"Bp", Bp_move_export, METH_VARARGS, "Bp move"},
    {"M",  M_move_export, METH_VARARGS,  "M move"},
    {"M2", M2_move_export, METH_VARARGS, "M2 move"},
    {"Mp", Mp_move_export, METH_VARARGS, "Mp move"},
    {"E",  E_move_export, METH_VARARGS,  "E move"},
    {"E2", E2_move_export, METH_VARARGS, "E2 move"},
    {"Ep", Ep_move_export, METH_VARARGS, "Ep move"},
    {"S",  S_move_export, METH_VARARGS,  "S move"},
    {"S2", S2_move_export, METH_VARARGS, "S2 move"},
    {"Sp", Sp_move_export, METH_VARARGS, "Sp move"},
    {"x",  x_move_export, METH_VARARGS,  "x move"},
    {"xp", xp_move_export, METH_VARARGS, "xp move"},
    {"x2", x2_move_export, METH_VARARGS, "x2 move"},
    {"y",  y_move_export, METH_VARARGS,  "y move"},
    {"yp", yp_move_export, METH_VARARGS, "yp move"},
    {"y2", y2_move_export, METH_VARARGS, "y2 move"},
    {"z",  z_move_export, METH_VARARGS,  "z move"},
    {"zp", zp_move_export, METH_VARARGS, "zp move"},
    {"z2", z2_move_export, METH_VARARGS, "z2 move"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef movesmodule = {
    PyModuleDef_HEAD_INIT,
    "moves_upgrade_py",
    NULL,
    -1,
    MovesMethods
};

PyMODINIT_FUNC PyInit_moves_upgrade_py(void) {
    return PyModule_Create(&movesmodule);
}