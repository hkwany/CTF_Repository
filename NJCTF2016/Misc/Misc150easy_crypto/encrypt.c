#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char **argv) {
    if (argc != 3) {
        printf("USAGE: %s input_file output_file\n", argv[0]);
        return 0;
    }
    FILE* input_file  = fopen(argv[1], "rb");
    FILE* output_file = fopen(argv[2], "wb");
    if (!input_file || !output_file) {
        printf("Error\n");
        return 0;
    }
    char key[] = "XXXXXXXXXXXX";
    char p, t, c = 0;
    int i = 0;
    while ((p = fgetc(input_file)) != EOF) {
        c = ((key[i % strlen(key)] ^ t) + (p-t) + i*i ) & 0xff;
        t = p;
        i++;
        fputc(c, output_file);
    }
    return 0;
}
