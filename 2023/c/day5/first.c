#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define SEEDS_SIZE 4
#define MAX_MAP_NAME_SIZE 50
#define MAX_NUM_SIZE 25
#define MAX_MAP_SIZE 7
#define MAX_MAP_VALUES_SIZE 50

#define TRUE 1
#define FALSE 0

enum MAP_VALUE
{
    DEST,
    SOURCE,
    RANGE
};

typedef struct MapValues
{
    size_t dest;
    size_t src;
    size_t range;
} MapValues;

typedef struct Map
{
    char name[MAX_MAP_NAME_SIZE];
    MapValues *values;
} Map;

typedef size_t Seed;
typedef unsigned short Bool;

int main()
{

    FILE *input_file = fopen("../../inputs/day5.txt", "r");
    if (input_file == NULL)
    {
        fprintf(stderr, "Error during file opening!\n");
        exit(EXIT_FAILURE);
    }

    size_t linecap = 0;
    ssize_t len;
    size_t curr_seed = 0;
    size_t curr_map_pos = 0;
    size_t curr_map_values_pos = 0;
    char *line = NULL;
    Seed seeds[SEEDS_SIZE] = {0};
    Bool is_map = FALSE;
    Map maps[MAX_MAP_SIZE];
    enum MAP_VALUE curr_map_value = DEST;

    while ((len = getline(&line, &linecap, input_file)) > 0)
    {
        if ((line[0] == '\r' || line[0] == '\n'))
        {
            fprintf(stdout, "%s\n", line);
            if (is_map)
            {
                is_map = FALSE;
                curr_map_pos++;
                curr_map_values_pos = 0;
            }
            continue;
        }

        char *pos;
#pragma region Seeds
        if ((pos = strstr(line, "seeds: ")) > 0)
        {
            size_t offset = (pos - line) + strlen("seeds: ");
            for (size_t i = offset; i < (size_t)len; i++)
            {
                if (isspace(line[i]))
                    continue;

                char ch;
                char num[MAX_NUM_SIZE];
                size_t curr_num_pos = 0;
                while (isnumber((ch = line[i])) && i < (size_t)len)
                {
                    num[curr_num_pos++] = ch;
                    i++;
                }

                num[curr_num_pos] = '\0';
                if (strlen(num) > 0)
                {
                    seeds[curr_seed] = atol(num);
                    curr_seed++;
                }
            }
        }
#pragma endregion

#pragma region Maps
        if ((pos = strstr(line, " map:")) > 0)
        {
            is_map = TRUE;
            char map_name[MAX_MAP_NAME_SIZE];
            size_t current_name_pos = 0;
            for (size_t i = 0; i < (pos - line); i++)
            {
                map_name[current_name_pos++] = line[i];
            }

            map_name[current_name_pos] = '\0';
            Map new_map;
            strcpy(new_map.name, map_name);
            maps[curr_map_pos] = new_map;
            continue;
        }

        if (is_map)
        {
            maps[curr_map_pos].values = realloc(maps[curr_map_pos].values, sizeof(MapValues) * (curr_map_values_pos + 1));
            MapValues values;
            for (size_t i = 0; i < strlen(line); i++)
            {
                if (isspace(line[i]))
                    continue;

                char ch;
                char num[MAX_NUM_SIZE];
                size_t curr_num_pos = 0;
                while (isnumber((ch = line[i])))
                {
                    num[curr_num_pos++] = ch;
                    i++;
                }

                num[curr_num_pos] = '\0';

                switch (curr_map_value)
                {
                case DEST:
                    values.dest = atol(num);
                    curr_map_value = SOURCE;
                    break;
                case SOURCE:
                    values.src = atol(num);
                    curr_map_value = RANGE;
                    break;
                default:
                    values.range = atol(num);
                    maps[curr_map_pos].values[curr_map_values_pos++] = values;
                    curr_map_value = DEST;
                    break;
                }
            }
        }
#pragma endregion
    }

    for (size_t i = 0; i < MAX_MAP_SIZE; i++)
    {
        Map curr = maps[i];
        fprintf(stdout, "Mappa: %s\n", curr.name);
        MapValues *values = curr.values;
        while (values++ != NULL)
        {
            fprintf(stdout, "\tDestination: %ld\n\tSource: %ld\n\tRange: %ld\n", (*values).dest, (*values).src, (*values).range);
        }
    }

    exit(EXIT_SUCCESS);
}