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

void print_orientation(struct element* cube){
    printf("    %d %d %d\n", cube[0].orientation, cube[1].orientation, cube[2].orientation);
    printf("    %d   %d\n", cube[7].orientation, cube[3].orientation);
    printf("    %d %d %d\n\n", cube[6].orientation, cube[5].orientation, cube[4].orientation);
    printf("%d   %d   %d   %d\n\n", cube[17].orientation, cube[19].orientation, cube[21].orientation, cube[23].orientation);
    printf("    %d %d %d\n", cube[8].orientation, cube[9].orientation, cube[10].orientation);
    printf("    %d   %d\n", cube[15].orientation, cube[11].orientation);
    printf("    %d %d %d\n\n\n", cube[14].orientation, cube[13].orientation, cube[12].orientation);
    
}

void print_index(struct element* cube){
    printf("    %d %d %d\n", cube[0].index, cube[1].index, cube[2].index);
    printf("    %d    %d\n", cube[7].index, cube[3].index);
    printf("    %d %d %d\n\n", cube[6].index, cube[5].index, cube[4].index);
    printf("%d   %d   %d   %d\n\n", cube[17].index, cube[19].index, cube[21].index, cube[23].index);
    printf("    %d %d %d\n", cube[8].index, cube[9].index, cube[10].index);
    printf("    %d    %d\n", cube[15].index, cube[11].index);
    printf("    %d %d %d\n\n\n", cube[14].index, cube[13].index, cube[12].index);
}