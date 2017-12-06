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
    char key[] = "OKIWILLLETYOUKNOWWHATTHEKEYIS";
    char p, t, c = 0;
    int i = 0;
    while ((c = fgetc(input_file)) != EOF) {
        p=c-i*i+t-((key[i % strlen(key)] ^ t) ;

        t = p;
        i++;
        fputc(p,output_file);
    }
    return 0;
}