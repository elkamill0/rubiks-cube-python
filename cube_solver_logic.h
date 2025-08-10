#ifndef CUBE_SOLVER_LOGIC_H
#define CUBE_SOLVER_LOGIC_H

#include <stdbool.h>

#define MAX_SOLUTIONS 1000

typedef struct {
    int *moves;
    int length;
} Solution;

extern Solution solutions[MAX_SOLUTIONS];
extern int solution_count;

void combinations(int depth, int* start_state, int* final_state);

#endif
