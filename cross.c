#include <stdio.h>
#include <stdbool.h>

#define MAX_MOVES 6
#define MAX_DEPTH 4

typedef struct {
    // stan twojego sześcianu
} Cube;

int iterator = 0;

// Symuluje ruch (1x, 2x, 3x)
void apply_move(Cube* cube, int move_index) {
    // np. cube->faces[...] = ...
}

// Cofnięcie ruchu: 3x ten sam daje odwrót
void undo_move(Cube* cube, int move_index) {
    for (int i = 0; i < 3; ++i)
        apply_move(cube, move_index);
}

// Czy dana kombinacja ruchów jest niedozwolona
bool is_invalid(int move, int prev1, int prev2) {
    // np. zakaz cofnięcia lub powtórki
    return false; // placeholder
}

// Rekurencyjny eksplorator
void explore(Cube* cube, int depth, int path[]) {
    if (depth == MAX_DEPTH) {
        iterator++;
        return;
    }

    for (int move = 0; move < MAX_MOVES; ++move) {
        if (depth >= 2 && is_invalid(move, path[depth - 1], path[depth - 2]))
            continue;
        if (depth >= 1 && move == path[depth - 1])
            continue;

        for (int times = 1; times <= 3; ++times) {
            for (int i = 0; i < times; ++i)
                apply_move(cube, move);

            path[depth] = move;
            explore(cube, depth + 1, path);

            for (int i = 0; i < times; ++i)
                undo_move(cube, move);
        }
    }
}
