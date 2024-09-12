#ifndef MOVES_C
#define MOVES_C
#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <string.h>

struct element{
    int index;
    int orientation;
};

extern struct element buff;
void swap90(struct element* a, struct element* b, struct element* c, struct element* d);
void swap180(struct element* a, struct element* b, struct element* c, struct element* d);
void swap270(struct element* a, struct element* b, struct element* c, struct element* d);
void R_e(struct element cube[]);
void Rp_e(struct element cube[]);
void R2_e(struct element cube[]);
void L_e(struct element cube[]);
void Lp_e(struct element cube[]);
void L2_e(struct element cube[]);
void U_e(struct element cube[]);
void Up_e(struct element cube[]);
void U2_e(struct element cube[]);
void D_e(struct element cube[]);
void Dp_e(struct element cube[]);
void D2_e(struct element cube[]);
void F_e(struct element cube[]);
void Fp_e(struct element cube[]);
void F2_e(struct element cube[]);
void B_e(struct element cube[]);
void Bp_e(struct element cube[]);
void B2_e(struct element cube[]);
 void R(struct element cube[]);
void Rp(struct element cube[]);
void R2(struct element cube[]);
 void L(struct element cube[]);
void Lp(struct element cube[]);
void L2(struct element cube[]);
 void U(struct element cube[]);
void Up(struct element cube[]);
void U2(struct element cube[]);
 void D(struct element cube[]);
void Dp(struct element cube[]);
void D2(struct element cube[]);
 void F(struct element cube[]);
void Fp(struct element cube[]);
void F2(struct element cube[]);
 void B(struct element cube[]);
void Bp(struct element cube[]);
void B2(struct element cube[]);
void M(struct element cube[]);
void Mp(struct element cube[]);
void M2(struct element cube[]);
void E(struct element cube[]);
void Ep(struct element cube[]);
void E2(struct element cube[]);
void S(struct element cube[]);
void Sp(struct element cube[]);
void S2(struct element cube[]);
void x(struct element cube[]);
void xp(struct element cube[]);
void x2(struct element cube[]);
void y(struct element cube[]);
void yp(struct element cube[]);
void y2(struct element cube[]);
void z(struct element cube[]);
void zp(struct element cube[]);
void z2(struct element cube[]);
bool check_cross(struct element cube[]);
extern void (*moving[])(struct element cube[]);
void print_cube(struct element cube[]);

#endif