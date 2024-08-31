#include </usr/include/python3.10/Python.h>
#include <stdio.h>



int* decapsulation(PyObject* self, PyObject* args){
    PyObject* capsule;
    
    if (!PyArg_ParseTuple(args, "O", &capsule)) {
        return NULL;
    }
    return (int*)PyCapsule_GetPointer(capsule, "CubeArray");
}

void cube_destructor(PyObject* capsule) {
    int* cube = (int*)PyCapsule_GetPointer(capsule, "CubeArray");
    if (cube) {
        free(cube);  // Free the allocated memory
    }
}

void setup(){
const char* moves_str[18] = {"R", "R2", "Rp", "L", "L2", "Lp","U", "U2", "Up","D", "D2", "Dp","F", "F2", "Fp","B", "B2", "Bp"};
    char** moves_ptr = (char**)malloc(17 * sizeof(char*));
    for (int i = 0; i < 17; i++){
        moves_ptr[i] = (char*)malloc((strlen(moves_str[i]) + 1) * sizeof(char));
        strcpy(moves_ptr[i], moves_str[i]);
    }
}