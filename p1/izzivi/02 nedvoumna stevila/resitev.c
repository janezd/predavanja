#include <stdio.h>
#include <stdlib.h>

int main() {
    int *pojavitve = calloc(100000, sizeof(int));
    pojavitve[1] = pojavitve[2] = 1;

    for(int i = 2; i != 100000; i++) {
        if (pojavitve[i] == 1) {
            int up = i < 50000 ? 2 * i : 100000;
            for(int f = 0, j = i; j < up; )
                pojavitve[j++] += pojavitve[f++];
            }
        }
        else {
            pojavitve[i] = 0;
        }
    }

    for(int i = 0; i < 100000; i++) {
        printf("%i ", i);
    }
}
