#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <time.h>
#include <stdbool.h>
#include <unistd.h>
#include <sys/resource.h>
// #include "dfs_concept.h"

int map_R(int i)
{
    switch (i)
    {
    case 5:
        return 33;
    case 9:
        return 17;
    case 17:
        return 5;
    case 33:
        return 9;
    case 69:
        return 97;
    case 73:
        return 81;
    case 81:
        return 69;
    case 97:
        return 73;
    default:
        return i;
    }
}

int map_Rp(int i)
{
    switch (i)
    {
    case 33:
        return 5;
    case 9:
        return 33;
    case 17:
        return 9;
    case 5:
        return 17;
    case 97:
        return 69;
    case 73:
        return 97;
    case 81:
        return 73;
    case 69:
        return 81;
    default:
        return i;
    }
}

int map_R2(int i)
{
    switch (i)
    {
    case 33:
        return 17;
    case 17:
        return 33;
    case 5:
        return 9;
    case 9:
        return 5;
    case 97:
        return 81;
    case 81:
        return 97;
    case 69:
        return 73;
    case 73:
        return 69;
    default:
        return i;
    }
}

int map_L(int i)
{
    switch (i)
    {
    case 6:
        return 18;
    case 18:
        return 10;
    case 10:
        return 34;
    case 34:
        return 6;
    case 70:
        return 82;
    case 82:
        return 74;
    case 74:
        return 98;
    case 98:
        return 70;
    default:
        return i;
    }
}

int map_Lp(int i)
{
    switch (i)
    {
    case 6:
        return 34;
    case 18:
        return 6;
    case 10:
        return 18;
    case 34:
        return 10;
    case 70:
        return 98;
    case 82:
        return 70;
    case 74:
        return 82;
    case 98:
        return 74;
    default:
        return i;
    }
}

int map_L2(int i)
{
    switch (i)
    {
    case 6:
        return 10;
    case 10:
        return 6;
    case 18:
        return 34;
    case 34:
        return 18;
    case 70:
        return 74;
    case 74:
        return 70;
    case 82:
        return 98;
    case 98:
        return 82;
    default:
        return i;
    }
}

int map_U(int i)
{
    switch (i)
    {
    case 36:
        return 5;
    case 5:
        return 20;
    case 20:
        return 6;
    case 6:
        return 36;
    case 100:
        return 69;
    case 69:
        return 84;
    case 84:
        return 70;
    case 70:
        return 100;
    default:
        return i;
    }
}

int map_Up(int i)
{
    switch (i)
    {
    case 36:
        return 6;
    case 6:
        return 20;
    case 20:
        return 5;
    case 5:
        return 36;
    case 100:
        return 70;
    case 70:
        return 84;
    case 84:
        return 69;
    case 69:
        return 100;
    default:
        return i;
    }
}

int map_U2(int i)
{
    switch (i)
    {
    case 36:
        return 20;
    case 20:
        return 36;
    case 5:
        return 6;
    case 6:
        return 5;
    case 100:
        return 84;
    case 84:
        return 100;
    case 69:
        return 70;
    case 70:
        return 69;
    default:
        return i;
    }
}

int map_D(int i)
{
    switch (i)
    {
    case 40:
        return 10;
    case 10:
        return 24;
    case 24:
        return 9;
    case 9:
        return 40;
    case 104:
        return 74;
    case 74:
        return 88;
    case 88:
        return 73;
    case 73:
        return 104;
    default:
        return i;
    }
}

int map_Dp(int i)
{
    switch (i)
    {
    case 40:
        return 9;
    case 9:
        return 24;
    case 24:
        return 10;
    case 10:
        return 40;
    case 104:
        return 73;
    case 73:
        return 88;
    case 88:
        return 74;
    case 74:
        return 104;
    default:
        return i;
    }
}

int map_D2(int i)
{
    switch (i)
    {
    case 40:
        return 24;
    case 24:
        return 40;
    case 10:
        return 9;
    case 9:
        return 10;
    case 104:
        return 88;
    case 88:
        return 104;
    case 74:
        return 73;
    case 73:
        return 74;
    default:
        return i;
    }
}

int map_F(int i)
{
    switch (i)
    {
    case 20:
        return 81;
    case 84:
        return 17;
    case 17:
        return 88;
    case 81:
        return 24;
    case 24:
        return 82;
    case 88:
        return 18;
    case 18:
        return 84;
    case 82:
        return 20;
    default:
        return i;
    }
}

int map_Fp(int i)
{
    switch (i)
    {
    case 84:
        return 18;
    case 20:
        return 82;
    case 82:
        return 24;
    case 18:
        return 88;
    case 88:
        return 17;
    case 24:
        return 81;
    case 81:
        return 20;
    case 17:
        return 84;
    default:
        return i;
    }
}

int map_F2(int i)
{
    switch (i)
    {
    case 20:
        return 24;
    case 24:
        return 20;
    case 17:
        return 18;
    case 18:
        return 17;
    case 84:
        return 88;
    case 88:
        return 84;
    case 81:
        return 82;
    case 82:
        return 81;
    default:
        return i;
    }
}

int map_B(int i)
{
    switch (i)
    {
    case 36:
        return 98;
    case 100:
        return 34;
    case 34:
        return 104;
    case 98:
        return 40;
    case 40:
        return 97;
    case 104:
        return 33;
    case 33:
        return 100;
    case 97:
        return 36;
    default:
        return i;
    }
}

int map_Bp(int i)
{
    switch (i)
    {
    case 36:
        return 97;
    case 100:
        return 33;
    case 33:
        return 104;
    case 97:
        return 40;
    case 40:
        return 98;
    case 104:
        return 34;
    case 34:
        return 100;
    case 98:
        return 36;
    default:
        return i;
    }
}

int map_B2(int i)
{
    switch (i)
    {
    case 36:
        return 40;
    case 40:
        return 36;
    case 34:
        return 33;
    case 33:
        return 34;
    case 100:
        return 104;
    case 104:
        return 100;
    case 98:
        return 97;
    case 97:
        return 98;
    default:
        return i;
    }
}

typedef struct SearchCube
{
    int *state;
    int path;
    struct SearchCube *parent;
    int depth;
} SearchCube;

typedef struct Stack
{
    SearchCube *items[100];
    int top;
} Stack;

void initStack(Stack *s)
{
    s->top = -1;
}

int isEmpty(Stack *s)
{
    return s->top == -1;
}

void push(Stack *s, SearchCube *cube)
{
    if (s->top < 100 - 1)
    {
        s->items[++(s->top)] = cube;
    }
}

SearchCube *pop(Stack *s)
{
    if (!isEmpty(s))
    {
        return s->items[(s->top)--];
    }
    return NULL;
}

SearchCube *peek(Stack *s)
{
    if (!isEmpty(s))
    {
        return s->items[s->top];
    }
    return NULL;
}

void printStack(Stack *s)
{
    printf("Stack contents (bottom to top):\n");
    for (int i = 0; i <= s->top; i++)
    {
        SearchCube *cube = s->items[i];
        printf("  Depth: %d, Path: %d, State: [%d %d %d %d]\n",
               cube->depth, cube->path,
               cube->state[0], cube->state[1], cube->state[2], cube->state[3]);
    }
    printf("elements on stack: %d\n", s->top);
}

typedef struct CubeMoves
{
    int *state;
    int *final_state;
    SearchCube **stack;
    int *stack_size;
} CubeMoves;

typedef int (*MoveFunc)(int);

MoveFunc move_funcs[] = {
    map_R, map_R2, map_Rp,
    map_L, map_L2, map_Lp,
    map_U, map_U2, map_Up,
    map_D, map_D2, map_Dp,
    map_F, map_F2, map_Fp,
    map_B, map_B2, map_Bp};

bool is_invalid(int one, int two, int three)
{
    return ((three == one) && ((two ^ 1) == one));
}

bool equal_arrays(int a[], int b[])
{
    for (int i = 0; i < 4; i++)
    {
        if (a[i] != b[i])
        {
            return false;
        }
    }
    return true;
}

int *move_cube(int move_number, int source[4])
{
    int *destination = malloc(sizeof(int) * 4);
    for (int i = 0; i < 4; i++)
    {
        destination[i] = move_funcs[move_number](source[i]);
    }
    return destination;
}

SearchCube *createNode(int *state, int path, SearchCube *parent, int depth)
{
    SearchCube *cube = malloc(sizeof(SearchCube));
    cube->state = state;
    cube->path = path;
    cube->parent = parent;
    cube->depth = depth;
    return cube;
}

// int casesCounter = 0;

void printSolution(SearchCube *node)
{
    while (node->parent != NULL)
    {
        printf("%d ", node->path);
        node = node->parent;
    }
    printf("%d\n", node->path);
    printf("----------\n");
    // casesCounter++;
    // free(node);
}

void printSolutionLast(SearchCube *node, int lastMove)
{
    printf("%d ", lastMove);
    while (node->parent != NULL)
    {
        printf("%d ", node->path);
        node = node->parent;
    }
    printf("%d\n", node->path);
    printf("----------\n");
    // casesCounter++;
    // free(node);
}

int *saveSolution(SearchCube *node)
{
    int *sol = malloc(sizeof(int) * (node->depth + 1));
    sol[node->depth] = -1;

    SearchCube *current = node;
    while (current->parent != NULL)
    {
        sol[current->depth - 1] = current->path;
        current = current->parent;
    }
    sol[0] = current->path;
    return sol;
}

int *saveSolutionLast(SearchCube *node, int lastMove)
{
    int *sol = malloc(sizeof(int) * (node->depth + 1));
    sol[node->depth] = -1;
    sol[node->depth - 1] = lastMove;
    SearchCube *current = node;
    while (current->parent != NULL)
    {
        sol[current->depth - 2] = current->path;
        current = current->parent;
    }
    sol[0] = current->path;
    return sol;
}

bool lastLoop(SearchCube *node, int *finalState, int **solutions, int *solution_count)
{
    for (int i = 0; i < 18; i += 3)
    {

        if (i / 3 == node->path / 3)
        {
            continue;
        }
        if (node->parent != NULL && is_invalid(i / 3, node->path / 3, node->parent->path / 3))
        {
            continue;
        }

        int *state = move_cube(i, node->state);
        if (!equal_arrays(state, node->state))
        {
            if (equal_arrays(state, finalState))
            {

                solutions[(*solution_count)++] = saveSolutionLast(node, i);
                // printSolutionLast(node, i);
                free(state);
                return true;
            }
            free(state);

            for (int j = 1; j < 3; j++)
            {
                int *state = move_cube(i + j, node->state);
                if (equal_arrays(state, finalState))
                {
                    solutions[(*solution_count)++] = saveSolutionLast(node, i + j);
                    // printSolutionLast(node, i+j);
                    free(state);
                    return true;
                }
                free(state);
            }
        }
        else
        {
            free(state);
        }
    }
    return false;
}

int missingCrossSlotsCounter(int *a, int *b)
{
    int sum = 0;
    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            if (a[i] == b[j])
            {
                sum++;
                break;
            }
        }
    }
    return sum;
}

int **combinations(int depth, int *start_state, int *final_state)
{
    int **solutions = malloc(sizeof(int *) * 10000);
    int solution_count = 0;

    Stack s;
    initStack(&s);
    for (int i = 0; i < 18; i += 3)
    {
        // printStack(&s);
        int *state = move_cube(i, start_state);
        if (!equal_arrays(state, start_state))
        {
            SearchCube *cube = createNode(state, i, NULL, 2);
            push(&s, cube);
            for (int j = 1; j < 3; j++)
            {
                SearchCube *cube = createNode(move_cube(i + j, start_state), i + j, NULL, 2);
                push(&s, cube);
            }
        }
        else
        {
            free(state);
        }
    }

    if (depth == 1)
    {
        while (!isEmpty(&s))
        {
            SearchCube *node = pop(&s);
            if (equal_arrays(node->state, final_state))
            {
                solutions[solution_count++] = saveSolution(node);
                // printSolution(node);
            }
            free(node->state);
            free(node);
        }
    }

    int crossSlots;

    while (!isEmpty(&s))
    {
        // printStack(&s);
        SearchCube *node = pop(&s);
        if (equal_arrays(node->state, final_state))
        {
            solutions[solution_count++] = saveSolution(node);
            free(node->state);
            free(node);
            continue;
        }

        if (node->depth == depth)
        {
            lastLoop(node, final_state, solutions, &solution_count);
            free(node->state);
            free(node);
            continue;
        }
        crossSlots = missingCrossSlotsCounter(node->state, final_state);

        if (node->depth + 3 - crossSlots > depth)
        {
            free(node->state);
            free(node);
            continue;
        }

        for (int i = 0; i < 18; i += 3)
        {
            if (i / 3 == node->path / 3)
            {
                continue;
            }
            if (node->parent != NULL && is_invalid(i / 3, node->path / 3, node->parent->path / 3))
            {
                continue;
            }
            int *state = move_cube(i, node->state);
            if (!equal_arrays(state, node->state))
            {
                SearchCube *cube = createNode(state, i, node, node->depth + 1);
                push(&s, cube);
                for (int j = 1; j < 3; j++)
                {
                    SearchCube *cube = createNode(move_cube(i + j, node->state), i + j, node, node->depth + 1);
                    push(&s, cube);
                }
            }
            else
            {
                free(state);
            }
        }
        free(node->state);
    }
    solutions = realloc(solutions, sizeof(int *) * (solution_count + 1));
    solutions[solution_count] = NULL;
    return solutions;
    // printf("cases counter: %d", casesCounter);
}

double get_memory_usage_mb()
{
    struct rusage usage;
    getrusage(RUSAGE_SELF, &usage);
    return usage.ru_maxrss / 1024.0; // ru_maxrss in KB, convert to MB
}

int main()
{
    // int start_state[4] = {20, 74, 100, 40};
    int start_state[4] = {104, 100, 98, 70};
    int final_state[4] = {40, 9, 24, 10};

    // double total_time = 0.0;
    // int times = 100;
    // for (int i = 0; i < times; i++) {
    //     clock_t start = clock();
    //     combinations(2, start_state, final_state);
    //     clock_t end = clock();
    //     total_time += (double)(end - start) / CLOCKS_PER_SEC;
    // }
    // printf("%.4f sekund\n", total_time / times);

    clock_t start = clock();
    int **solutions = combinations(7, start_state, final_state);
    clock_t stop = clock();
    double elapsed_time = (double)(stop - start) / CLOCKS_PER_SEC;
    printf("Czas dla combinations: %.4f sekund\n", elapsed_time);
    printf("Zużycie pamięci: %.2f MB\n", get_memory_usage_mb());

    for (int i = 0; solutions[i] != NULL; i++)
    {
        printf("Solution %d: ", i);
        for (int j = 0; solutions[i][j] != -1; j++)
        {
            printf("%d ", solutions[i][j]);
        }
        printf("\n");
    }
}

// 16
// 9
// 3
// 14
// 5
// 7
// -------