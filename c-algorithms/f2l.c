#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include </usr/include/python3.10/Python.h>
#include "moves.h"


const char* int_to_moves(int move){
    switch(move){

        case 0:
            return "R ";
        case 1:
            return "R2 ";
        case 2:
            return "R' ";
        case 3:
            return "L ";
        case 4:
            return "L2 ";
        case 5:
            return "L' ";
        case 6:
            return "U ";
        case 7:
            return "U2 ";
        case 8:
            return "U' ";
        case 9:
            return "D ";
        case 10:
            return "D2 ";
        case 11:
            return "D' ";
        case 12:
            return "F ";
        case 13:
            return "F2 ";
        case 14:
            return "F' ";
        case 15:
            return "B ";
        case 16:
            return "B2 ";
        case 17:
            return "B' ";
        default: 
            return "Invalid";
    }
}

bool check_slot(int* cube){
    if(cube[13] == cube[14] && cube[16] == cube[17] && cube[21] == cube[22] && cube[24] == cube[25] & check_cross(cube)){
        return true;
    }
    return false;
}


char* combination_list[10000];
int combination_iterator = 0;
void loop(int depth, int* current_combination, int current_length, int* cube) {
    int ignored_move = current_combination[current_length - 1]/3;
    int opposite_move = current_combination[current_length - 2]/3; 
    
    
    if(check_slot(cube)){
        // print_combination(current_combination, current_length);
        char final[22] = "";
        for (int i = 0; i < current_length ; ++i) {
            strncat(final, int_to_moves(current_combination[i]), sizeof(final) - strlen(final) - 1);
        }

        combination_list[combination_iterator] = malloc(strlen(final) + 1);
        strcpy(combination_list[combination_iterator], final);
        // printf("%s\n", final);

        combination_iterator++;
        return;  
    }
    if (depth == 0) {
        return;
    }
    for (int i = 0; i < 6; ++i) {
        if (ignored_move == i || (opposite_move == i && ignored_move == i&1)){
            continue;
        }
        for (int j = 0; j < 3; ++j){
            moving_f2l[i](cube);
            current_combination[current_length] = i*3+j;
            loop(depth - 1, current_combination, current_length + 1, cube);
        }
        moving_f2l[i](cube);
    }
    
}

PyObject* combinations_c(int* cube, int length){
    int initial_combination[length];
    for (int i = 0; i < 6; ++i) {
        for (int j = 0; j < 3; ++j){
            moving_f2l[i](cube);
            initial_combination[0] = i*3+j;
            for (int k = 0; k < 6; ++k){
                if (i == k){
                    continue;
                }
                for (int l = 0; l < 3; ++l){
                    moving_f2l[k](cube);
                    initial_combination[1] = k*3+l;
                    loop(length - 2, initial_combination, 2, cube);
                }
                moving_f2l[k](cube);
            }
        }
        moving_f2l[i](cube);
    }

    PyObject *py_list = PyList_New(combination_iterator);

    if (!py_list) {
        return NULL;  // Return NULL if memory allocation fails
    }
    PyObject* str;
    for (int i = 0; i < combination_iterator; ++i){
        str = PyUnicode_FromString(combination_list[i]);
        PyList_SET_ITEM(py_list, i, str);
    }
    // printf("found solutions: %d\n", combination_iterator);

    return py_list;
    
}

static PyObject* check_f2l_pair(PyObject* self, PyObject* args){
    int length;
    PyObject* capsule;

    if (!PyArg_ParseTuple(args, "iO", &length, &capsule)) {
        return NULL;
    }
    int* cube = PyCapsule_GetPointer(capsule, "CubeArray");

    PyObject* py_list = combinations_c(cube, length);
    
    return py_list;
    // printf("%d", check_slot(cube));
    // Py_RETURN_NONE;
}


static PyMethodDef F2lMethods[] = {
    {"check_f2l_pair", check_f2l_pair, METH_VARARGS, "make f2l pair"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef f2lmodule = {
    PyModuleDef_HEAD_INIT,
    "f2l",
    NULL,
    -1,
    F2lMethods
};

PyMODINIT_FUNC PyInit_f2l(void) {
    return PyModule_Create(&f2lmodule);
}