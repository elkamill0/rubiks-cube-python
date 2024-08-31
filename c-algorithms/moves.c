#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include "moves.h"
#include </usr/include/python3.10/Python.h>

// int cube[] = {0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5};
int buff;

void swap90(int* a, int* b, int* c, int* d){
    buff = *d;
    *d = *c;
    *c = *b;
    *b = *a;
    *a = buff;   
}

void swap180(int* a, int* b, int* c, int* d){
    buff = *a;
    *a = *c;
    *c = buff;
    buff = *b;
    *b = *d;
    *d = buff;
}

void swap270(int* a, int* b, int* c, int* d){
    buff = *a;
    *a = *b;
    *b = *c;
    *c = *d;
    *d = buff;
}

void rot90(int start_block, int* cube){
    swap90(&cube[start_block], &cube[start_block+2], &cube[start_block+8], &cube[start_block+6]);
    swap90(&cube[start_block+1], &cube[start_block+5], &cube[start_block+7], &cube[start_block+3]);
}

void rot180(int start_block, int* cube){
    swap180(&cube[start_block], &cube[start_block+2], &cube[start_block+8], &cube[start_block+6]);
    swap180(&cube[start_block+1], &cube[start_block+5], &cube[start_block+7], &cube[start_block+3]);
}

void rot270(int start_block, int* cube){
    swap270(&cube[start_block], &cube[start_block+2], &cube[start_block+8], &cube[start_block+6]);
    swap270(&cube[start_block+1], &cube[start_block+5], &cube[start_block+7], &cube[start_block+3]);
}

void R(int cube[]){
    swap90(&cube[2], &cube[42], &cube[47], &cube[20]);
    swap90(&cube[5], &cube[39], &cube[50], &cube[23]);
    swap90(&cube[8], &cube[36], &cube[53], &cube[26]);
    rot90(27, cube);
}

void Rp(int cube[]){
    swap270(&cube[2], &cube[42], &cube[47], &cube[20]);
    swap270(&cube[5], &cube[39], &cube[50], &cube[23]);
    swap270(&cube[8], &cube[36], &cube[53], &cube[26]);
    rot270(27, cube);
}

void R2(int cube[]){
    swap180(&cube[2], &cube[42], &cube[47], &cube[20]);
    swap180(&cube[5], &cube[39], &cube[50], &cube[23]);
    swap180(&cube[8], &cube[36], &cube[53], &cube[26]);
    rot180(27, cube);
}

void L(int cube[]){
    swap90(&cube[0], &cube[18], &cube[45], &cube[44]);
    swap90(&cube[3], &cube[21], &cube[48], &cube[41]);
    swap90(&cube[6], &cube[24], &cube[51], &cube[38]);
    rot90(9, cube);
}

void Lp(int cube[]){
    swap270(&cube[0], &cube[18], &cube[45], &cube[44]);
    swap270(&cube[3], &cube[21], &cube[48], &cube[41]);
    swap270(&cube[6], &cube[24], &cube[51], &cube[38]);
    rot270(9, cube);
}

void L2(int cube[]){
    swap180(&cube[0], &cube[18], &cube[45], &cube[44]);
    swap180(&cube[3], &cube[21], &cube[48], &cube[41]);
    swap180(&cube[6], &cube[24], &cube[51], &cube[38]);
    rot180(9, cube);
}

void U(int cube[]){
    swap90(&cube[18], &cube[9], &cube[36], &cube[27]);
    swap90(&cube[19], &cube[10], &cube[37], &cube[28]);
    swap90(&cube[20], &cube[11], &cube[38], &cube[29]);
    rot90(0, cube);
}

void Up(int cube[]){
    swap270(&cube[18], &cube[9], &cube[36], &cube[27]);
    swap270(&cube[19], &cube[10], &cube[37], &cube[28]);
    swap270(&cube[20], &cube[11], &cube[38], &cube[29]);
    rot270(0, cube);
}

void U2(int cube[]){
    swap180(&cube[18], &cube[9], &cube[36], &cube[27]);
    swap180(&cube[19], &cube[10], &cube[37], &cube[28]);
    swap180(&cube[20], &cube[11], &cube[38], &cube[29]);
    rot180(0, cube);
}

void D(int cube[]){
    swap90(&cube[24], &cube[33], &cube[42], &cube[15]);
    swap90(&cube[25], &cube[34], &cube[43], &cube[16]);
    swap90(&cube[26], &cube[35], &cube[44], &cube[17]);
    rot90(45, cube);
}

void Dp(int cube[]){
    swap270(&cube[24], &cube[33], &cube[42], &cube[15]);
    swap270(&cube[25], &cube[34], &cube[43], &cube[16]);
    swap270(&cube[26], &cube[35], &cube[44], &cube[17]);
    rot270(45, cube);
}

void D2(int cube[]){
    swap180(&cube[24], &cube[33], &cube[42], &cube[15]);
    swap180(&cube[25], &cube[34], &cube[43], &cube[16]);
    swap180(&cube[26], &cube[35], &cube[44], &cube[17]);
    rot180(45, cube);
}

void F(int cube[]){
    swap90(&cube[6], &cube[27], &cube[47], &cube[17]);
    swap90(&cube[7], &cube[30], &cube[46], &cube[14]);
    swap90(&cube[8], &cube[33], &cube[45], &cube[11]);
    rot90(18, cube);
}

void Fp(int cube[]){
    swap270(&cube[6], &cube[27], &cube[47], &cube[17]);
    swap270(&cube[7], &cube[30], &cube[46], &cube[14]);
    swap270(&cube[8], &cube[33], &cube[45], &cube[11]);
    rot270(18, cube);
}

void F2(int cube[]){
    swap180(&cube[6], &cube[27], &cube[47], &cube[17]);
    swap180(&cube[7], &cube[30], &cube[46], &cube[14]);
    swap180(&cube[8], &cube[33], &cube[45], &cube[11]);
    rot180(18, cube);
}

void B(int cube[]){
    swap90(&cube[0], &cube[15], &cube[53], &cube[29]);
    swap90(&cube[1], &cube[12], &cube[52], &cube[32]);
    swap90(&cube[2], &cube[9], &cube[51], &cube[35]);
    rot90(36, cube);
}

void Bp(int cube[]){
    swap270(&cube[0], &cube[15], &cube[53], &cube[29]);
    swap270(&cube[1], &cube[12], &cube[52], &cube[32]);
    swap270(&cube[2], &cube[9], &cube[51], &cube[35]);
    rot270(36, cube);
}

void B2(int cube[]){
    swap180(&cube[0], &cube[15], &cube[53], &cube[29]);
    swap180(&cube[1], &cube[12], &cube[52], &cube[32]);
    swap180(&cube[2], &cube[9], &cube[51], &cube[35]);
    rot180(36, cube);
}

void rot90_e(int start_block, int* cube){
    swap90(&cube[start_block+1], &cube[start_block+5], &cube[start_block+7], &cube[start_block+3]);
}

void rot180_e(int start_block, int* cube){
    swap180(&cube[start_block+1], &cube[start_block+5], &cube[start_block+7], &cube[start_block+3]);
}

void rot270_e(int start_block, int* cube){
    swap270(&cube[start_block+1], &cube[start_block+5], &cube[start_block+7], &cube[start_block+3]);
}

void R_e(int cube[]){
    swap90(&cube[5], &cube[39], &cube[50], &cube[23]);
    rot90_e(27, cube);
}

void Rp_e(int cube[]){
    swap270(&cube[5], &cube[39], &cube[50], &cube[23]);
    rot270_e(27, cube);
}

void R2_e(int cube[]){
    swap180(&cube[5], &cube[39], &cube[50], &cube[23]);
    rot180_e(27, cube);
}

void L_e(int cube[]){
    swap90(&cube[3], &cube[21], &cube[48], &cube[41]);
    rot90_e(9, cube);
}

void Lp_e(int cube[]){
    swap270(&cube[3], &cube[21], &cube[48], &cube[41]);
    rot270_e(9, cube);
}

void L2_e(int cube[]){
    swap180(&cube[3], &cube[21], &cube[48], &cube[41]);
    rot180_e(9, cube);
}

void U_e(int cube[]){
    swap90(&cube[19], &cube[10], &cube[37], &cube[28]);
    rot90_e(0, cube);
}

void Up_e(int cube[]){
    swap270(&cube[19], &cube[10], &cube[37], &cube[28]);
    rot270_e(0, cube);
}

void U2_e(int cube[]){
    swap180(&cube[19], &cube[10], &cube[37], &cube[28]);
    rot180_e(0, cube);
}

void D_e(int cube[]){
    swap90(&cube[25], &cube[34], &cube[43], &cube[16]);
    rot90_e(45, cube);
}

void Dp_e(int cube[]){
    swap270(&cube[25], &cube[34], &cube[43], &cube[16]);
    rot270_e(45, cube);
}

void D2_e(int cube[]){
    swap180(&cube[25], &cube[34], &cube[43], &cube[16]);
    rot180_e(45, cube);
}

void F_e(int cube[]){
    swap90(&cube[7], &cube[30], &cube[46], &cube[14]);
    rot90_e(18, cube);
}

void Fp_e(int cube[]){
    swap270(&cube[7], &cube[30], &cube[46], &cube[14]);
    rot270_e(18, cube);
}

void F2_e(int cube[]){
    swap180(&cube[7], &cube[30], &cube[46], &cube[14]);
    rot180_e(18, cube);
}

void B_e(int cube[]){
    swap90(&cube[1], &cube[12], &cube[52], &cube[32]);
    rot90_e(36, cube);
}

void Bp_e(int cube[]){
    swap270(&cube[1], &cube[12], &cube[52], &cube[32]);
    rot270_e(36, cube);
}

void B2_e(int cube[]){
    swap180(&cube[1], &cube[12], &cube[52], &cube[32]);
    rot180_e(36, cube);
}

void x_e(int cube[]){
    swap90(&cube[1], &cube[43], &cube[46], &cube[19]);
    swap90(&cube[3], &cube[41], &cube[48], &cube[21]);
    swap90(&cube[4], &cube[40], &cube[49], &cube[22]);
    swap90(&cube[5], &cube[39], &cube[50], &cube[23]);
    swap90(&cube[7], &cube[37], &cube[52], &cube[25]);
    rot270_e(9, cube);
    rot90_e(27, cube);
}

void xp_e(int cube[]){
    swap270(&cube[1], &cube[43], &cube[46], &cube[19]);
    swap270(&cube[3], &cube[41], &cube[48], &cube[21]);
    swap270(&cube[4], &cube[40], &cube[49], &cube[22]);
    swap270(&cube[5], &cube[39], &cube[50], &cube[23]);
    swap270(&cube[7], &cube[37], &cube[52], &cube[25]);
    rot90_e(9, cube);
    rot270_e(27, cube);
}

void x2_e(int cube[]){
    swap180(&cube[1], &cube[43], &cube[46], &cube[19]);
    swap180(&cube[3], &cube[41], &cube[48], &cube[21]);
    swap180(&cube[4], &cube[40], &cube[49], &cube[22]);
    swap180(&cube[5], &cube[39], &cube[50], &cube[23]);
    swap180(&cube[7], &cube[37], &cube[52], &cube[25]);
    rot180_e(9, cube);
    rot180_e(27, cube);
}

void y_e(int cube[]){
    swap90(&cube[10], &cube[37], &cube[28], &cube[19]);
    swap90(&cube[12], &cube[39], &cube[30], &cube[21]);
    swap90(&cube[13], &cube[40], &cube[31], &cube[22]);
    swap90(&cube[14], &cube[41], &cube[32], &cube[23]);
    swap90(&cube[16], &cube[43], &cube[34], &cube[25]);
    rot90_e(0, cube);
    rot270_e(45, cube);
}

void yp_e(int cube[]){
    swap270(&cube[10], &cube[37], &cube[28], &cube[19]);
    swap270(&cube[12], &cube[39], &cube[30], &cube[21]);
    swap270(&cube[13], &cube[40], &cube[31], &cube[22]);
    swap270(&cube[14], &cube[41], &cube[32], &cube[23]);
    swap270(&cube[16], &cube[43], &cube[34], &cube[25]);
    rot270_e(0, cube);
    rot90_e(45, cube);
}

void y2_e(int cube[]){
    swap180(&cube[10], &cube[37], &cube[28], &cube[19]);
    swap180(&cube[12], &cube[39], &cube[30], &cube[21]);
    swap180(&cube[13], &cube[40], &cube[31], &cube[22]);
    swap180(&cube[14], &cube[41], &cube[32], &cube[23]);
    swap180(&cube[16], &cube[43], &cube[34], &cube[25]);
    rot180_e(0, cube);
    rot180_e(45, cube);
}

void z_e(int cube[]){
    swap90(&cube[1], &cube[32], &cube[52], &cube[12]);
    swap90(&cube[3], &cube[28], &cube[50], &cube[16]);
    swap90(&cube[4], &cube[31], &cube[49], &cube[13]);
    swap90(&cube[5], &cube[34], &cube[48], &cube[10]);
    swap90(&cube[7], &cube[30], &cube[46], &cube[14]);
    rot90_e(18, cube);
    rot270_e(36, cube);
}

void zp_e(int cube[]){
    swap270(&cube[1], &cube[32], &cube[52], &cube[12]);
    swap270(&cube[3], &cube[28], &cube[50], &cube[16]);
    swap270(&cube[4], &cube[31], &cube[49], &cube[13]);
    swap270(&cube[5], &cube[34], &cube[48], &cube[10]);
    swap270(&cube[7], &cube[30], &cube[46], &cube[14]);
    rot270_e(18, cube);
    rot90_e(36, cube);
}

void z2_e(int cube[]){
    swap180(&cube[1], &cube[32], &cube[52], &cube[12]);
    swap180(&cube[3], &cube[28], &cube[50], &cube[16]);
    swap180(&cube[4], &cube[31], &cube[49], &cube[13]);
    swap180(&cube[5], &cube[34], &cube[48], &cube[10]);
    swap180(&cube[7], &cube[30], &cube[46], &cube[14]);
    rot180_e(18, cube);
    rot180_e(36, cube);
}

void (*moving[])(int[54]) = {R_e, L_e, U_e, D_e, F_e, B_e};
int numMoving = sizeof(moving) / sizeof(moving[0]);

void (*moving_f2l[])(int[54]) = {R, L, U, D, F, B};


void x(int cube[]){
    swap90(&cube[0], &cube[44], &cube[45], &cube[18]);
    swap90(&cube[1], &cube[43], &cube[46], &cube[19]);
    swap90(&cube[2], &cube[42], &cube[47], &cube[20]);
    swap90(&cube[3], &cube[41], &cube[48], &cube[21]);
    swap90(&cube[4], &cube[40], &cube[49], &cube[22]);
    swap90(&cube[5], &cube[39], &cube[50], &cube[23]);
    swap90(&cube[6], &cube[48], &cube[51], &cube[24]);
    swap90(&cube[7], &cube[37], &cube[52], &cube[25]);
    swap90(&cube[8], &cube[46], &cube[53], &cube[26]);
    rot270(9, cube);
    rot90(27, cube);
}

void xp(int cube[]){
    swap270(&cube[0], &cube[44], &cube[45], &cube[18]);
    swap270(&cube[1], &cube[43], &cube[46], &cube[19]);
    swap270(&cube[2], &cube[42], &cube[47], &cube[20]);
    swap270(&cube[3], &cube[41], &cube[48], &cube[21]);
    swap270(&cube[4], &cube[40], &cube[49], &cube[22]);
    swap270(&cube[5], &cube[39], &cube[50], &cube[23]);
    swap270(&cube[6], &cube[48], &cube[51], &cube[24]);
    swap270(&cube[7], &cube[37], &cube[52], &cube[25]);
    swap270(&cube[8], &cube[46], &cube[53], &cube[26]);
    rot90(9, cube);
    rot270(27, cube);
}

void x2(int cube[]){
    swap180(&cube[0], &cube[44], &cube[45], &cube[18]);
    swap180(&cube[1], &cube[43], &cube[46], &cube[19]);
    swap180(&cube[2], &cube[42], &cube[47], &cube[20]);
    swap180(&cube[3], &cube[41], &cube[48], &cube[21]);
    swap180(&cube[4], &cube[40], &cube[49], &cube[22]);
    swap180(&cube[5], &cube[39], &cube[50], &cube[23]);
    swap180(&cube[6], &cube[48], &cube[51], &cube[24]);
    swap180(&cube[7], &cube[37], &cube[52], &cube[25]);
    swap180(&cube[8], &cube[46], &cube[53], &cube[26]);
    rot180(9, cube);
    rot180(27, cube);
}

void y(int cube[]){
    swap90( &cube[9], &cube[36], &cube[27], &cube[18]);
    swap90(&cube[10], &cube[37], &cube[28], &cube[19]);
    swap90(&cube[11], &cube[38], &cube[29], &cube[20]);
    swap90(&cube[12], &cube[39], &cube[30], &cube[21]);
    swap90(&cube[13], &cube[40], &cube[31], &cube[22]);
    swap90(&cube[14], &cube[41], &cube[32], &cube[23]);
    swap90(&cube[15], &cube[42], &cube[33], &cube[24]);
    swap90(&cube[16], &cube[43], &cube[34], &cube[25]);
    swap90(&cube[17], &cube[44], &cube[35], &cube[26]);
    rot90(0, cube);
    rot270(45, cube);
}

void yp(int cube[]){
    swap270( &cube[9], &cube[36], &cube[27], &cube[18]);
    swap270(&cube[10], &cube[37], &cube[28], &cube[19]);
    swap270(&cube[11], &cube[38], &cube[29], &cube[20]);
    swap270(&cube[12], &cube[39], &cube[30], &cube[21]);
    swap270(&cube[13], &cube[40], &cube[31], &cube[22]);
    swap270(&cube[14], &cube[41], &cube[32], &cube[23]);
    swap270(&cube[15], &cube[42], &cube[33], &cube[24]);
    swap270(&cube[16], &cube[43], &cube[34], &cube[25]);
    swap270(&cube[17], &cube[44], &cube[35], &cube[26]);
    rot270(0, cube);
    rot90(45, cube);
}

void y2(int cube[]){
    swap180( &cube[9], &cube[36], &cube[27], &cube[18]);
    swap180(&cube[10], &cube[37], &cube[28], &cube[19]);
    swap180(&cube[11], &cube[38], &cube[29], &cube[20]);
    swap180(&cube[12], &cube[39], &cube[30], &cube[21]);
    swap180(&cube[13], &cube[40], &cube[31], &cube[22]);
    swap180(&cube[14], &cube[41], &cube[32], &cube[23]);
    swap180(&cube[15], &cube[42], &cube[33], &cube[24]);
    swap180(&cube[16], &cube[43], &cube[34], &cube[25]);
    swap180(&cube[17], &cube[44], &cube[35], &cube[26]);
    rot180(0, cube);
    rot180(45, cube);
}

void z(int cube[]){
    swap90(&cube[0], &cube[29], &cube[53], &cube[15]);
    swap90(&cube[1], &cube[32], &cube[52], &cube[12]);
    swap90(&cube[2], &cube[35], &cube[51], &cube[9]);
    swap90(&cube[3], &cube[28], &cube[50], &cube[16]);
    swap90(&cube[4], &cube[31], &cube[49], &cube[13]);
    swap90(&cube[5], &cube[34], &cube[48], &cube[10]);
    swap90(&cube[6], &cube[27], &cube[47], &cube[17]);
    swap90(&cube[7], &cube[30], &cube[46], &cube[14]);
    swap90(&cube[8], &cube[33], &cube[45], &cube[11]);
    rot90(18, cube);
    rot270(36, cube);
}

void zp(int cube[]){
    swap270(&cube[0], &cube[29], &cube[53], &cube[15]);
    swap270(&cube[1], &cube[32], &cube[52], &cube[12]);
    swap270(&cube[2], &cube[35], &cube[51], &cube[9]);
    swap270(&cube[3], &cube[28], &cube[50], &cube[16]);
    swap270(&cube[4], &cube[31], &cube[49], &cube[13]);
    swap270(&cube[5], &cube[34], &cube[48], &cube[10]);
    swap270(&cube[6], &cube[27], &cube[47], &cube[17]);
    swap270(&cube[7], &cube[30], &cube[46], &cube[14]);
    swap270(&cube[8], &cube[33], &cube[45], &cube[11]);
    rot270(18, cube);
    rot90(36, cube);
}

void z2(int cube[]){
    swap180(&cube[0], &cube[29], &cube[53], &cube[15]);
    swap180(&cube[1], &cube[32], &cube[52], &cube[12]);
    swap180(&cube[2], &cube[35], &cube[51], &cube[9]);
    swap180(&cube[3], &cube[28], &cube[50], &cube[16]);
    swap180(&cube[4], &cube[31], &cube[49], &cube[13]);
    swap180(&cube[5], &cube[34], &cube[48], &cube[10]);
    swap180(&cube[6], &cube[27], &cube[47], &cube[17]);
    swap180(&cube[7], &cube[30], &cube[46], &cube[14]);
    swap180(&cube[8], &cube[33], &cube[45], &cube[11]);
    rot180(18, cube);
    rot180(36, cube);
}

bool check_cross(int cube[]){
    if (cube[46] == cube[49] && cube[48] == cube[49] && cube[50] == cube[49] && cube[52] == cube[49] &&
        cube[13] == cube[16] && cube[22] == cube[25] && cube[31] == cube[34] && cube[40] == cube[43]){
            return true;
        }
    return false;
}

void print_cube(int cube[]){
    printf("    %d%d%d\n", cube[0], cube[1], cube[2]);
    printf("    %d%d%d\n", cube[3], cube[4], cube[5]);
    printf("    %d%d%d\n", cube[6], cube[7], cube[8]);
    printf("%d%d%d %d%d%d %d%d%d %d%d%d\n",  cube[9],cube[10],cube[11],cube[18],cube[19],cube[20],cube[27],cube[28],cube[29],cube[36],cube[37],cube[38]);
    printf("%d%d%d %d%d%d %d%d%d %d%d%d\n", cube[12],cube[13],cube[14],cube[21],cube[22],cube[23],cube[30],cube[31],cube[32],cube[39],cube[40],cube[41]);
    printf("%d%d%d %d%d%d %d%d%d %d%d%d\n", cube[15],cube[16],cube[17],cube[24],cube[25],cube[26],cube[33],cube[34],cube[35],cube[42],cube[43],cube[44]);
    printf("    %d%d%d\n", cube[45], cube[46], cube[47]);
    printf("    %d%d%d\n", cube[48], cube[49], cube[50]);
    printf("    %d%d%d\n", cube[51], cube[52], cube[53]);
    
}

void input_scramble(int* cube, long move){
    switch(move){
        case 0:
            R(cube);
            break;
        case 1:
            R2(cube);
            break;
        case 2:
            Rp(cube);
            break;
        case 3:
            L(cube);
            break;
        case 4:
            L2(cube);
            break;
        case 5:
            Lp(cube);
            break;
        case 6:
            U(cube);
            break;
        case 7:
            U2(cube);
            break;
        case 8:
            Up(cube);
            break;
        case 9:
            D(cube);
            break;
        case 10:
            D2(cube);
            break;
        case 11:
            Dp(cube);
            break;
        case 12:
            F(cube);
            break;
        case 13:
            F2(cube);
            break;
        case 14:
            Fp(cube);
            break;
        case 15:
            B(cube);
            break;
        case 16:
            B2(cube);
            break;
        case 17:
            Bp(cube);
            break;
        default:
            printf("Unknown move ");
            break;
    }
}

