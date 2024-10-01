#include </usr/include/python3.10/Python.h>
#include <stdio.h>



void print_value(int *value){
    printf("debug value: %d\n", &value);
}

struct element* decapsulation(PyObject* self, PyObject* args, char* pointer_name){
    PyObject* capsule;
    
    if (!PyArg_ParseTuple(args, "O", &capsule)) {
        return NULL;
    }
    return (struct element*)PyCapsule_GetPointer(capsule, pointer_name);
}

// int* decapsulation_two_cubes(PyObject* self, PyObject* args){
//     int* 
//     PyObject* capsule;
//     PyObject* capsule2;
//     if (!PyArg_ParseTuple(args, "OO", &capsule, &capsule2)) {
//         return NULL;
//     }    
//     return 
// }

void cube_destructor(PyObject* capsule) {
    struct element *cube = (struct element *)PyCapsule_GetPointer(capsule, "CubeArray");
    if (cube) {
        free(cube);  // Free the allocated memory
    }
}
void cube_copy_destructor(PyObject* capsule){
    struct element *cube = (struct element *)PyCapsule_GetPointer(capsule, "CubeArrayCopy");
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