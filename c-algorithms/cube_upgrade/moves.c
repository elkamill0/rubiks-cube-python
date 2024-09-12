#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include "moves.h"
#include </usr/include/python3.10/Python.h>


struct element buff;
void swap90(struct element* a, struct element* b, struct element* c, struct element* d) {
    buff = *d;
    *d = *c;
    *c = *b;
    *b = *a;
    *a = buff;   
}

void swap180(struct element* a, struct element* b, struct element* c, struct element* d) {
    buff = *a;
    *a = *c;
    *c = buff;
    buff = *b;
    *b = *d;
    *d = buff;
}

void swap270(struct element* a, struct element* b, struct element* c, struct element* d) {
    buff = *a;
    *a = *b;
    *b = *c;
    *c = *d;
    *d = buff;
}

void R_e(struct element cube[]){
    swap90(&cube[3], &cube[19], &cube[11], &cube[21]);
}

void Rp_e(struct element cube[]){
    swap270(&cube[3], &cube[19], &cube[11], &cube[21]);
}

void R2_e(struct element cube[]){
    swap180(&cube[3], &cube[19], &cube[11], &cube[21]);
}

void L_e(struct element cube[]){
    swap90(&cube[7], &cube[23], &cube[15], &cube[17]);
}

void Lp_e(struct element cube[]){
    swap270(&cube[7], &cube[23], &cube[15], &cube[17]);
}

void L2_e(struct element cube[]){
    swap180(&cube[7], &cube[23], &cube[15], &cube[17]);
}

void U_e(struct element cube[]){
    swap90(&cube[1], &cube[3], &cube[5], &cube[7]);
}

void Up_e(struct element cube[]){
    swap270(&cube[1], &cube[3], &cube[5], &cube[7]);
}

void U2_e(struct element cube[]){
    swap180(&cube[1], &cube[3], &cube[5], &cube[7]);
}

void D_e(struct element cube[]){
     swap90(&cube[9], &cube[11], &cube[13], &cube[15]);
}

void Dp_e(struct element cube[]){
    swap270(&cube[9], &cube[11], &cube[13], &cube[15]);
}

void D2_e(struct element cube[]){
    swap180(&cube[9], &cube[11], &cube[13], &cube[15]);
}

void F_e(struct element cube[]){
    swap90(&cube[5], &cube[21], &cube[9], &cube[23]);
     cube[5].orientation =  cube[5].orientation ^ 1;
    cube[21].orientation = cube[21].orientation ^ 1;
     cube[9].orientation =  cube[9].orientation ^ 1;
    cube[23].orientation = cube[23].orientation ^ 1;
    
}

void Fp_e(struct element cube[]){
    swap270(&cube[5], &cube[21], &cube[9], &cube[23]);
     cube[5].orientation =  cube[5].orientation ^ 1;
    cube[21].orientation = cube[21].orientation ^ 1;
     cube[9].orientation =  cube[9].orientation ^ 1;
    cube[23].orientation = cube[23].orientation ^ 1;
}

void F2_e(struct element cube[]){
    swap180(&cube[5], &cube[21], &cube[9], &cube[23]);
}

void B_e(struct element cube[]){
    swap90(&cube[1], &cube[17], &cube[13], &cube[19]);
     cube[1].orientation =  cube[1].orientation ^ 1;
    cube[17].orientation = cube[17].orientation ^ 1;
    cube[13].orientation = cube[13].orientation ^ 1;
    cube[19].orientation = cube[19].orientation ^ 1;
}

void Bp_e(struct element cube[]){
     cube[1].orientation  = cube[1].orientation ^ 1;
    cube[17].orientation = cube[17].orientation ^ 1;
    cube[13].orientation = cube[13].orientation ^ 1;
    cube[19].orientation = cube[19].orientation ^ 1;
    swap270(&cube[1], &cube[17], &cube[13], &cube[19]);
}

void B2_e(struct element cube[]){
    swap180(&cube[1], &cube[17], &cube[13], &cube[19]);
}

bool check_cross(struct element cube[]){
    if(cube[9].index == 9 && cube[11].index == 11 && cube[13].index == 13 && cube[15].index == 15 && 
        cube[9].orientation && cube[11].orientation && cube[13].orientation && cube[15].orientation){
            return true;
    }
    return false;
}

void (*moving[])(struct element cube[]) = {R_e, L_e, U_e, D_e, F_e, B_e};

void rotate_corner(struct element *c1, struct element *c2, struct element *c3, struct element *c4){
    c1->orientation = (++c1->orientation % 3 + 3) % 3;
    c2->orientation = (--c2->orientation % 3 + 3) % 3;
    c3->orientation = (++c3->orientation % 3 + 3) % 3;
    c4->orientation = (--c4->orientation % 3 + 3) % 3;
}


void R(struct element cube[]){
    rotate_corner(&cube[4], &cube[2], &cube[12], &cube[10]);
    swap90(&cube[4], &cube[2], &cube[12], &cube[10]);
    R_e(cube);
}

void Rp(struct element cube[]){
    rotate_corner(&cube[4], &cube[2], &cube[12], &cube[10]);
    swap270(&cube[4], &cube[2], &cube[12], &cube[10]);
    Rp_e(cube);
}

void R2(struct element cube[]){
    swap180(&cube[4], &cube[2], &cube[12], &cube[10]);
    R2_e(cube);
}

void L(struct element cube[]){
    rotate_corner(&cube[0], &cube[6], &cube[8], &cube[14]);
    swap90(&cube[0], &cube[6], &cube[8], &cube[14]);
    L_e(cube);
}

void Lp(struct element cube[]){
    rotate_corner(&cube[0], &cube[6], &cube[8], &cube[14]);
    swap270(&cube[0], &cube[6], &cube[8], &cube[14]);
    Lp_e(cube);
}

void L2(struct element cube[]){
    swap180(&cube[0], &cube[6], &cube[8], &cube[14]);
    L2_e(cube);
}

void U(struct element cube[]){
    swap90(&cube[0], &cube[2], &cube[4], &cube[6]);
    U_e(cube);
}

void Up(struct element cube[]){
    swap270(&cube[0], &cube[2], &cube[4], &cube[6]);
    Up_e(cube);
}

void U2(struct element cube[]){
    swap180(&cube[0], &cube[2], &cube[4], &cube[6]);
    U2_e(cube);
}

void D(struct element cube[]){
     swap90(&cube[8], &cube[10], &cube[12], &cube[14]);
     D_e(cube);
}

void Dp(struct element cube[]){
    swap270(&cube[8], &cube[10], &cube[12], &cube[14]);
    Dp_e(cube);
}

void D2(struct element cube[]){
    swap180(&cube[8], &cube[10], &cube[12], &cube[14]);
    D2_e(cube);
}

void F(struct element cube[]){
    rotate_corner(&cube[6], &cube[4], &cube[10], &cube[8]);
    swap90(&cube[6], &cube[4], &cube[10], &cube[8]);
    F_e(cube);
}

void Fp(struct element cube[]){
    rotate_corner(&cube[6], &cube[4], &cube[10], &cube[8]);
    swap270(&cube[6], &cube[4], &cube[10], &cube[8]);
    Fp_e(cube);
}

void F2(struct element cube[]){
    swap180(&cube[6], &cube[4], &cube[10], &cube[8]);
    F2_e(cube);
}

void B(struct element cube[]){
    rotate_corner(&cube[2], &cube[0], &cube[14], &cube[12]);
    swap90(&cube[0], &cube[14], &cube[12], &cube[2]);
    B_e(cube);
}

void Bp(struct element cube[]){
    rotate_corner(&cube[2], &cube[0], &cube[14], &cube[12]);
    swap270(&cube[0], &cube[14], &cube[12], &cube[2]);
    Bp_e(cube);
}

void B2(struct element cube[]){
    swap180(&cube[0], &cube[14], &cube[12], &cube[2]);
    B2_e(cube);
}

void M(struct element cube[]){
    swap90(&cube[1], &cube[5], &cube[9], &cube[13]);
    swap90(&cube[16], &cube[20], &cube[25], &cube[24]);
}

void Mp(struct element cube[]){
    swap270(&cube[1], &cube[5], &cube[9], &cube[13]);
    swap270(&cube[16], &cube[20], &cube[25], &cube[24]);
}

void M2(struct element cube[]){
    swap180(&cube[1], &cube[5], &cube[9], &cube[13]);
    swap180(&cube[16], &cube[20], &cube[25], &cube[24]);
}

void E(struct element cube[]){
    swap90(&cube[23], &cube[21], &cube[19], &cube[17]);
    swap90(&cube[20], &cube[22], &cube[24], &cube[18]);
}   

void Ep(struct element cube[]){
    swap270(&cube[23], &cube[21], &cube[19], &cube[17]);
    swap270(&cube[20], &cube[22], &cube[24], &cube[18]);
}   

void E2(struct element cube[]){
    swap180(&cube[23], &cube[21], &cube[19], &cube[17]);
    swap180(&cube[20], &cube[22], &cube[24], &cube[18]);
}  

void S(struct element cube[]){
    swap90(&cube[7], &cube[3], &cube[11], &cube[15]);
    swap90(&cube[16], &cube[22], &cube[25], &cube[18]);
}   

void Sp(struct element cube[]){
    swap270(&cube[7], &cube[3], &cube[11], &cube[15]);
    swap270(&cube[16], &cube[22], &cube[25], &cube[18]);
}   

void S2(struct element cube[]){
    swap180(&cube[7], &cube[3], &cube[11], &cube[15]);
    swap180(&cube[16], &cube[22], &cube[25], &cube[18]);
}  

void x(struct element cube[]){
    swap90(&cube[4], &cube[2], &cube[12], &cube[10]);   // R
    R_e(cube);
    Mp(cube);
    swap270(&cube[0], &cube[6], &cube[8], &cube[14]); // Lp
    Lp_e(cube);
}

void xp(struct element cube[]){
    swap270(&cube[4], &cube[2], &cube[12], &cube[10]); // Rp
    Rp_e(cube);
    M(cube);
    swap90(&cube[0], &cube[6], &cube[8], &cube[14]); // L
    L_e(cube);
}

void x2(struct element cube[]){
    R2(cube);
    M2(cube);
    L2(cube);
}

void y(struct element cube[]){
    U(cube);
    Ep(cube);
    Dp(cube);
}

void yp(struct element cube[]){
    Up(cube);
    E(cube);
    D(cube);
}

void y2(struct element cube[]){
    U2(cube);
    E2(cube);
    D2(cube);
}

void z(struct element cube[]){
    swap270(&cube[0], &cube[14], &cube[12], &cube[2]); // Bp
    swap270(&cube[1], &cube[17], &cube[13], &cube[19]); // Bp_e
    S(cube);
    swap90(&cube[6], &cube[4], &cube[10], &cube[8]); // F
    swap90(&cube[5], &cube[21], &cube[9], &cube[23]); // F_e
}

void zp(struct element cube[]){
    swap90(&cube[0], &cube[14], &cube[12], &cube[2]); // B
    swap90(&cube[1], &cube[17], &cube[13], &cube[19]); // B_e
    Sp(cube);
    swap270(&cube[6], &cube[4], &cube[10], &cube[8]); // Fp
    swap270(&cube[5], &cube[21], &cube[9], &cube[23]); // Fp_e
}

void z2(struct element cube[]){
    B2(cube);
    S2(cube);
    F2(cube);
}



void print_cube(struct element cube[]){

    int* corners = malloc(8 * 3 * sizeof(int)); // 24
    int* edges = malloc(12 * 2 * sizeof(int));  // 24
    int* corners_representation = (int *)malloc(8 * 3 * sizeof(int));
    int* edges_representation = (int *)malloc(12 * 2 * sizeof(int));

     corners_representation[0] = 1;
     corners_representation[1] = 0;
     corners_representation[2] = 4;
     corners_representation[3] = 4;
     corners_representation[4] = 0;
     corners_representation[5] = 3;
     corners_representation[6] = 3;
     corners_representation[7] = 0;
     corners_representation[8] = 2;
     corners_representation[9] = 2;
    corners_representation[10] = 0;
    corners_representation[11] = 1;
    corners_representation[12] = 1;
    corners_representation[13] = 5;
    corners_representation[14] = 2;
    corners_representation[15] = 2;
    corners_representation[16] = 5;
    corners_representation[17] = 3;
    corners_representation[18] = 3;
    corners_representation[19] = 5;
    corners_representation[20] = 4;
    corners_representation[21] = 4;
    corners_representation[22] = 5;
    corners_representation[23] = 1;

     edges_representation[0] = 0;
     edges_representation[1] = 4;
     edges_representation[2] = 0;
     edges_representation[3] = 3;
     edges_representation[4] = 0;
     edges_representation[5] = 2;
     edges_representation[6] = 0;
     edges_representation[7] = 1;
     edges_representation[8] = 5;
     edges_representation[9] = 2;
    edges_representation[10] = 5;
    edges_representation[11] = 3;
    edges_representation[12] = 5;
    edges_representation[13] = 4;
    edges_representation[14] = 5;
    edges_representation[15] = 1;
    edges_representation[16] = 4;
    edges_representation[17] = 1;
    edges_representation[18] = 4;
    edges_representation[19] = 3;
    edges_representation[20] = 2;
    edges_representation[21] = 3;
    edges_representation[22] = 2;
    edges_representation[23] = 1;

    int temp, temp_orientation;
    for (int i = 0; i < 8; i++){
        temp = ((cube[i*2].index / 2) * 3);
        temp_orientation = cube[i*2].orientation;
        for (int j = 0; j < 3; j++){
            corners[i*3 + j] = corners_representation[temp + ((temp_orientation % 3 + 3) % 3)];
            --temp_orientation;
        }
    }
    for (int i = 1; i < 24; i+=2){
        edges[i-1] = edges_representation[cube[i].index - cube[i].orientation];
        edges[i] = edges_representation[cube[i].index - (cube[i].orientation^1)];
    }

    printf("    %d%d%d\n", corners[0], edges[0], corners[3]);
    printf("    %d%d%d\n", edges[6], cube[16].index, edges[2]);
    printf("    %d%d%d\n", corners[9], edges[4], corners[6]);
    printf("%d%d%d %d%d%d %d%d%d %d%d%d\n", corners[1], edges[7], corners[11], corners[10], edges[5], corners[8], corners[7], edges[3], corners[5], corners[4], edges[1], corners[2]);
    printf("%d%d%d %d%d%d %d%d%d %d%d%d\n", edges[17], cube[18].index, edges[23], edges[22], cube[20].index, edges[20], edges[21], cube[22].index, edges[19], edges[18], cube[24].index, edges[16]);
    printf("%d%d%d %d%d%d %d%d%d %d%d%d\n", corners[23], edges[15], corners[13], corners[14], edges[9], corners[16], corners[17], edges[11], corners[19], corners[20], edges[13], corners[22]);
    printf("    %d%d%d\n", corners[12], edges[8], corners[15]);
    printf("    %d%d%d\n", edges[14], cube[25].index, edges[10]);
    printf("    %d%d%d\n\n", corners[21], edges[12], corners[18]);
}

void input_scramble(struct element* cube, long move){
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