#include "moves_edges.h"
#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include </usr/include/python3.10/Python.h>


// int cube[] = {0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5};
int buff;


void swap90_e(int* a, int* b, int* c, int* d){
    buff = *d;
    *d = *c;
    *c = *b;
    *b = *a;
    *a = buff;   
}

void swap180_e(int* a, int* b, int* c, int* d){
    buff = *a;
    *a = *c;
    *c = buff;
    buff = *b;
    *b = *d;
    *d = buff;
}

void swap270_e(int* a, int* b, int* c, int* d){
    buff = *a;
    *a = *b;
    *b = *c;
    *c = *d;
    *d = buff;
}

void rot90_e(int start_block, int* cube){
    swap90_e(&cube[start_block+1], &cube[start_block+5], &cube[start_block+7], &cube[start_block+3]);
}

void rot180_e(int start_block, int* cube){
    swap180_e(&cube[start_block+1], &cube[start_block+5], &cube[start_block+7], &cube[start_block+3]);
}

void rot270_e(int start_block, int* cube){
    swap270_e(&cube[start_block+1], &cube[start_block+5], &cube[start_block+7], &cube[start_block+3]);
}

void R_e(int cube[]){
    swap90_e(&cube[5], &cube[39], &cube[50], &cube[23]);
    rot90_e(27, cube);
}

void Rp_e(int cube[]){
    swap270_e(&cube[5], &cube[39], &cube[50], &cube[23]);
    rot270_e(27, cube);
}

void R2_e(int cube[]){
    swap180_e(&cube[5], &cube[39], &cube[50], &cube[23]);
    rot180_e(27, cube);
}

void L_e(int cube[]){
    swap90_e(&cube[3], &cube[21], &cube[48], &cube[41]);
    rot90_e(9, cube);
}

void Lp_e(int cube[]){
    swap270_e(&cube[3], &cube[21], &cube[48], &cube[41]);
    rot270_e(9, cube);
}

void L2_e(int cube[]){
    swap180_e(&cube[3], &cube[21], &cube[48], &cube[41]);
    rot180_e(9, cube);
}

void U_e(int cube[]){
    swap90_e(&cube[19], &cube[10], &cube[37], &cube[28]);
    rot90_e(0, cube);
}

void Up_e(int cube[]){
    swap270_e(&cube[19], &cube[10], &cube[37], &cube[28]);
    rot270_e(0, cube);
}

void U2_e(int cube[]){
    swap180_e(&cube[19], &cube[10], &cube[37], &cube[28]);
    rot180_e(0, cube);
}

void D_e(int cube[]){
    swap90_e(&cube[25], &cube[34], &cube[43], &cube[16]);
    rot90_e(45, cube);
}

void Dp_e(int cube[]){
    swap270_e(&cube[25], &cube[34], &cube[43], &cube[16]);
    rot270_e(45, cube);
}

void D2_e(int cube[]){
    swap180_e(&cube[25], &cube[34], &cube[43], &cube[16]);
    rot180_e(45, cube);
}

void F_e(int cube[]){
    swap90_e(&cube[7], &cube[30], &cube[46], &cube[14]);
    rot90_e(18, cube);
}

void Fp_e(int cube[]){
    swap270_e(&cube[7], &cube[30], &cube[46], &cube[14]);
    rot270_e(18, cube);
}

void F2_e(int cube[]){
    swap180_e(&cube[7], &cube[30], &cube[46], &cube[14]);
    rot180_e(18, cube);
}

void B_e(int cube[]){
    swap90_e(&cube[1], &cube[12], &cube[52], &cube[32]);
    rot90_e(36, cube);
}

void Bp_e(int cube[]){
    swap270_e(&cube[1], &cube[12], &cube[52], &cube[32]);
    rot270_e(36, cube);
}

void B2_e(int cube[]){
    swap180_e(&cube[1], &cube[12], &cube[52], &cube[32]);
    rot180_e(36, cube);
}

void x_e(int cube[]){
    swap90_e(&cube[1], &cube[43], &cube[46], &cube[19]);
    swap90_e(&cube[3], &cube[41], &cube[48], &cube[21]);
    swap90_e(&cube[4], &cube[40], &cube[49], &cube[22]);
    swap90_e(&cube[5], &cube[39], &cube[50], &cube[23]);
    swap90_e(&cube[7], &cube[37], &cube[52], &cube[25]);
    rot270_e(9, cube);
    rot90_e(27, cube);
}

void xp_e(int cube[]){
    swap270_e(&cube[1], &cube[43], &cube[46], &cube[19]);
    swap270_e(&cube[3], &cube[41], &cube[48], &cube[21]);
    swap270_e(&cube[4], &cube[40], &cube[49], &cube[22]);
    swap270_e(&cube[5], &cube[39], &cube[50], &cube[23]);
    swap270_e(&cube[7], &cube[37], &cube[52], &cube[25]);
    rot90_e(9, cube);
    rot270_e(27, cube);
}

void x2_e(int cube[]){
    swap180_e(&cube[1], &cube[43], &cube[46], &cube[19]);
    swap180_e(&cube[3], &cube[41], &cube[48], &cube[21]);
    swap180_e(&cube[4], &cube[40], &cube[49], &cube[22]);
    swap180_e(&cube[5], &cube[39], &cube[50], &cube[23]);
    swap180_e(&cube[7], &cube[37], &cube[52], &cube[25]);
    rot180_e(9, cube);
    rot180_e(27, cube);
}

void y_e(int cube[]){
    // swap90_e(&cube[9], &cube[36], &cube[27], &cube[18]);
    swap90_e(&cube[10], &cube[37], &cube[28], &cube[19]);
    swap90_e(&cube[12], &cube[39], &cube[30], &cube[21]);
    swap90_e(&cube[13], &cube[40], &cube[31], &cube[22]);
    swap90_e(&cube[14], &cube[41], &cube[32], &cube[23]);
    swap90_e(&cube[16], &cube[43], &cube[34], &cube[25]);
    rot90_e(0, cube);
    rot270_e(45, cube);
}

void yp_e(int cube[]){
    // swap90_e(&cube[9], &cube[36], &cube[27], &cube[18]);
    swap270_e(&cube[10], &cube[37], &cube[28], &cube[19]);
    swap270_e(&cube[12], &cube[39], &cube[30], &cube[21]);
    swap270_e(&cube[13], &cube[40], &cube[31], &cube[22]);
    swap270_e(&cube[14], &cube[41], &cube[32], &cube[23]);
    swap270_e(&cube[16], &cube[43], &cube[34], &cube[25]);
    rot270_e(0, cube);
    rot90_e(45, cube);
}

void y2_e(int cube[]){
    // swap90_e(&cube[9], &cube[36], &cube[27], &cube[18]);
    swap180_e(&cube[10], &cube[37], &cube[28], &cube[19]);
    swap180_e(&cube[12], &cube[39], &cube[30], &cube[21]);
    swap180_e(&cube[13], &cube[40], &cube[31], &cube[22]);
    swap180_e(&cube[14], &cube[41], &cube[32], &cube[23]);
    swap180_e(&cube[16], &cube[43], &cube[34], &cube[25]);
    rot180_e(0, cube);
    rot180_e(45, cube);
}

void z_e(int cube[]){
    // swap90_e(&cube[0], &cube[29], &cube[53], &cube[15]);
    swap90_e(&cube[1], &cube[32], &cube[52], &cube[12]);
    swap90_e(&cube[3], &cube[28], &cube[50], &cube[16]);
    swap90_e(&cube[4], &cube[31], &cube[49], &cube[13]);
    swap90_e(&cube[5], &cube[34], &cube[48], &cube[10]);
    swap90_e(&cube[7], &cube[30], &cube[46], &cube[14]);
    rot90_e(18, cube);
    rot270_e(36, cube);
}

void zp_e(int cube[]){
    // swap270_e(&cube[0], &cube[29], &cube[53], &cube[15]);
    swap270_e(&cube[1], &cube[32], &cube[52], &cube[12]);
    swap270_e(&cube[3], &cube[28], &cube[50], &cube[16]);
    swap270_e(&cube[4], &cube[31], &cube[49], &cube[13]);
    swap270_e(&cube[5], &cube[34], &cube[48], &cube[10]);
    swap270_e(&cube[7], &cube[30], &cube[46], &cube[14]);
    rot270_e(18, cube);
    rot90_e(36, cube);
}

void z2_e(int cube[]){
    // swap180_e(&cube[0], &cube[29], &cube[53], &cube[15]);
    swap180_e(&cube[1], &cube[32], &cube[52], &cube[12]);
    swap180_e(&cube[3], &cube[28], &cube[50], &cube[16]);
    swap180_e(&cube[4], &cube[31], &cube[49], &cube[13]);
    swap180_e(&cube[5], &cube[34], &cube[48], &cube[10]);
    swap180_e(&cube[7], &cube[30], &cube[46], &cube[14]);
    rot180_e(18, cube);
    rot180_e(36, cube);
}


bool check_cross(int cube[]){
    if (cube[46] == cube[49] && cube[48] == cube[49] && cube[50] == cube[49] && cube[52] == cube[49] &&
        cube[13] == cube[16] && cube[22] == cube[25] && cube[31] == cube[34] && cube[40] == cube[43]){
            return true;
        }
    return false;
}

void (*moving[])(int[54]) = {R_e, L_e, U_e, D_e, F_e, B_e};
int numMoving = sizeof(moving) / sizeof(moving[0]);


// void print_cube(int* cube){
//     printf("     %d\n", cube[1]);
//     printf("    %d%d%d\n", cube[3], cube[4], cube[5]);
//     printf("     %d\n", cube[7]);
//     printf(" %d   %d   %d   %d\n", cube[10],cube[19],cube[28],cube[37]);
//     printf("%d%d%d %d%d%d %d%d%d %d%d%d\n", cube[12],cube[13],cube[14],cube[21],cube[22],cube[23],cube[30],cube[31],cube[32],cube[39],cube[40],cube[41]);
//     printf(" %d   %d   %d   %d\n", cube[16],cube[25],cube[34],cube[43]);
//     printf("     %d\n", cube[46]);
//     printf("    %d%d%d\n", cube[48], cube[49], cube[50]);
//     printf("     %d\n", cube[52]);
// }

