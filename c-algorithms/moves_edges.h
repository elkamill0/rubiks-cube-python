#ifndef MOVES_EDGES_H
#define MOVES_EDGES_H
#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <string.h>

void swap90_e(int* a, int* b, int* c, int* d);
void swap180_e(int* a, int* b, int* c, int* d);
void swap270_e(int* a, int* b, int* c, int* d);
void rot90_e(int start_block, int* cube);
void rot180_e(int start_block, int* cube);
void rot270_e(int start_block, int* cube);
void R_e(int cube[]);
void Rp_e(int cube[]);
void R2_e(int cube[]);
void L_e(int cube[]);
void Lp_e(int cube[]);
void L2_e(int cube[]);
void U_e(int cube[]);
void Up_e(int cube[]);
void U2_e(int cube[]);
void D_e(int cube[]);
void Dp_e(int cube[]);
void D2_e(int cube[]);
void F_e(int cube[]);
void Fp_e(int cube[]);
void F2_e(int cube[]);
void B_e(int cube[]);
void Bp_e(int cube[]);
void B2_e(int cube[]);
void x_e(int cube[]);
void xp_e(int cube[]);
void x2_e(int cube[]);
void y_e(int cube[]);
void yp_e(int cube[]);
void y2_e(int cube[]);
void z_e(int cube[]);
void zp_e(int cube[]);
void z2_e(int cube[]);
extern void (*moving[])(int[54]);
extern int numMoving;
bool check_cross(int cube[]);
// void print_cube(int* cube);
// void input_scramble(int* cube, long move);

#endif

