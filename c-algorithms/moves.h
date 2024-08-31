#ifndef MOVES_C
#define MOVES_C
#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <string.h>

extern int buff;
void swap90(int* a, int* b, int* c, int* d);
void swap180(int* a, int* b, int* c, int* d);
void swap270(int* a, int* b, int* c, int* d);
void rot90(int start_block, int* cube);
void rot180(int start_block, int* cube);
void rot270(int start_block, int* cube);
void R(int cube[]);
void Rp(int cube[]);
void R2(int cube[]);
void L(int cube[]);
void Lp(int cube[]);
void L2(int cube[]);
void U(int cube[]);
void Up(int cube[]);
void U2(int cube[]);
void D(int cube[]);
void Dp(int cube[]);
void D2(int cube[]);
void F(int cube[]);
void Fp(int cube[]);
void F2(int cube[]);
void B(int cube[]);
void Bp(int cube[]);
void B2(int cube[]);

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
extern void (*moving_f2l[])(int[54]);
// void x(int cube[]);
// void xp(int cube[]);
// void x2(int cube[]);
// void y(int cube[]);
// void yp(int cube[]);
// void y2(int cube[]);
// void z(int cube[]);
// void zp(int cube[]);
// void z2(int cube[]);
bool check_cross(int cube[]);
void print_cube(int* cube);
void input_scramble(int* cube, long move);

#endif

