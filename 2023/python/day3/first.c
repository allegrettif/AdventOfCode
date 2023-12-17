#include <stdio.h>
#include <stdlib.h>

int main()
{

    FILE *file = fopen("input.txt", "r");
    if (file == NULL)
    {
        exit(EXIT_FAILURE);
    }

    fread();

    exit(EXIT_SUCCESS);
}