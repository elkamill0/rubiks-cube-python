#ifndef MOVES_C
#define MOVES_C
#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <string.h>

struct element{
    int default_index;
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
void M(struct element cube[], struct element cube_copy[]);
void Mp(struct element cube[], struct element cube_copy[]);
void M2(struct element cube[], struct element cube_copy[]);
void E(struct element cube[], struct element cube_copy[]);
void Ep(struct element cube[], struct element cube_copy[]);
void E2(struct element cube[], struct element cube_copy[]);
void S(struct element cube[], struct element cube_copy[]);
void Sp(struct element cube[], struct element cube_copy[]);
void S2(struct element cube[], struct element cube_copy[]);
void x(struct element cube[], struct element cube_copy[]);
void xp(struct element cube[], struct element cube_copy[]);
void x2(struct element cube[], struct element cube_copy[]);
void y(struct element cube[], struct element cube_copy[]);
void yp(struct element cube[], struct element cube_copy[]);
void y2(struct element cube[], struct element cube_copy[]);
void z(struct element cube[], struct element cube_copy[]);
void zp(struct element cube[], struct element cube_copy[]);
void z2(struct element cube[], struct element cube_copy[]);
bool check_cross(struct element cube[], struct element cube_copy[]);
extern void (*moving[])(struct element cube[]);
void print_cube(struct element cube[]);

#endif