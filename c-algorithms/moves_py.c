#include </usr/include/python3.10/Python.h>
#include "moves.h"
#include "utils.c"

static PyObject* R_move_export(PyObject* self, PyObject* args){
    int* cube = decapsulation(self, args);
    R(cube);
    Py_RETURN_NONE;
}

static PyObject* R2_move_export(PyObject* self, PyObject* args){
    int* cube = decapsulation(self, args);
    R2(cube);
    Py_RETURN_NONE;
}

static PyObject* Rp_move_export(PyObject* self, PyObject* args){
    int* cube = decapsulation(self, args);
    Rp(cube);
    Py_RETURN_NONE;
}

static PyObject* L_move_export(PyObject* self, PyObject* args){
    int* cube = decapsulation(self, args);
    L(cube);
    Py_RETURN_NONE;
}

static PyObject* L2_move_export(PyObject* self, PyObject* args){
    int* cube = decapsulation(self, args);
    L2(cube);
    Py_RETURN_NONE;
}

static PyObject* Lp_move_export(PyObject* self, PyObject* args){
    int* cube = decapsulation(self, args);
    Lp(cube);
    Py_RETURN_NONE;
}

static PyObject* U_move_export(PyObject* self, PyObject* args){
    int* cube = decapsulation(self, args);
    U(cube);
    Py_RETURN_NONE;
}

static PyObject* U2_move_export(PyObject* self, PyObject* args){
    int* cube = decapsulation(self, args);
    U2(cube);
    Py_RETURN_NONE;
}

static PyObject* Up_move_export(PyObject* self, PyObject* args){
    int* cube = decapsulation(self, args);
    Up(cube);
    Py_RETURN_NONE;
}

static PyObject* D_move_export(PyObject* self, PyObject* args){
    int* cube = decapsulation(self, args);
    D(cube);
    Py_RETURN_NONE;
}

static PyObject* D2_move_export(PyObject* self, PyObject* args){
    int* cube = decapsulation(self, args);
    D2(cube);
    Py_RETURN_NONE;
}

static PyObject* Dp_move_export(PyObject* self, PyObject* args){
    int* cube = decapsulation(self, args);
    Dp(cube);
    Py_RETURN_NONE;
}

static PyObject* F_move_export(PyObject* self, PyObject* args){
    int* cube = decapsulation(self, args);
    F(cube);
    Py_RETURN_NONE;
}

static PyObject* F2_move_export(PyObject* self, PyObject* args){
    int* cube = decapsulation(self, args);
    F2(cube);
    Py_RETURN_NONE;
}

static PyObject* Fp_move_export(PyObject* self, PyObject* args){
    int* cube = decapsulation(self, args);
    Fp(cube);
    Py_RETURN_NONE;
}

static PyObject* B_move_export(PyObject* self, PyObject* args){
    int* cube = decapsulation(self, args);
    B(cube);
    Py_RETURN_NONE;
}

static PyObject* B2_move_export(PyObject* self, PyObject* args){
    int* cube = decapsulation(self, args);
    B2(cube);
    Py_RETURN_NONE;
}

static PyObject* Bp_move_export(PyObject* self, PyObject* args){
    int* cube = decapsulation(self, args);
    Bp(cube);
    Py_RETURN_NONE;
}

static PyObject* x_move_export(PyObject* self, PyObject* args){
    int* cube = decapsulation(self, args);
    x(cube);
    Py_RETURN_NONE;
}

static PyObject* xp_move_export(PyObject* self, PyObject* args){
    int* cube = decapsulation(self, args);
    xp(cube);
    Py_RETURN_NONE;
}

static PyObject* x2_move_export(PyObject* self, PyObject* args){
    int* cube = decapsulation(self, args);
    x2(cube);
    Py_RETURN_NONE;
}

static PyObject* y_move_export(PyObject* self, PyObject* args){
    int* cube = decapsulation(self, args);
    y(cube);
    Py_RETURN_NONE;
}

static PyObject* yp_move_export(PyObject* self, PyObject* args){
    int* cube = decapsulation(self, args);
    yp(cube);
    Py_RETURN_NONE;
}

static PyObject* y2_move_export(PyObject* self, PyObject* args){
    int* cube = decapsulation(self, args);
    y2(cube);
    Py_RETURN_NONE;
}

static PyObject* z_move_export(PyObject* self, PyObject* args){
    int* cube = decapsulation(self, args);
    z(cube);
    Py_RETURN_NONE;
}

static PyObject* zp_move_export(PyObject* self, PyObject* args){
    int* cube = decapsulation(self, args);
    zp(cube);
    Py_RETURN_NONE;
}

static PyObject* z2_move_export(PyObject* self, PyObject* args){
    int* cube = decapsulation(self, args);
    z2(cube);
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
    "moves_py",
    NULL,
    -1,
    MovesMethods
};

PyMODINIT_FUNC PyInit_moves_py(void) {
    return PyModule_Create(&movesmodule);
}